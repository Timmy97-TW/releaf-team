#!/usr/bin/env python3
"""
Bundle the team page into one self-contained HTML file.

Every photo, the logo, the stylesheets, the scripts and the Inter typeface are
inlined as data URIs, so the result opens with no folder beside it and nothing
fetched from another server. Email it, AirDrop it, or publish it.

    python3 build-share.py

Writes:
    share/ReLeaf-team.html          full page, double-click to open
    docs/index.html                 same page, what GitHub Pages serves
    share/_artifact-body.html       same page without the <html>/<head>/<body>
                                    wrapper, for hosts that supply their own

Re-run it after editing anything under assets/.
"""

import base64, mimetypes, pathlib, re, sys

ROOT   = pathlib.Path(__file__).parent
SHARE  = ROOT / "share"
FONT   = ROOT / "assets" / "inter-variable.ttf"     # optional, see below

def data_uri(path: pathlib.Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return "data:%s;base64,%s" % (mime, base64.b64encode(path.read_bytes()).decode())

def read(rel: str) -> str:
    return (ROOT / rel).read_text()

def inline_assets(text: str) -> str:
    """Swap every assets/... reference for the file's own bytes."""
    def sub(m):
        rel = m.group(1)
        f = ROOT / rel
        if not f.exists():
            print("  ! missing, left as-is:", rel)
            return m.group(0)
        return m.group(0).replace(rel, data_uri(f))
    return re.sub(r'(assets/[A-Za-z0-9_\-/.]+\.(?:jpg|jpeg|png|webp|svg|gif))', sub, text)

def check(path: pathlib.Path):
    """Catch a malformed bundle before it ships."""
    t = path.read_text()
    style = re.search(r"<style>(.*?)</style>", t, re.S)
    if not style:
        sys.exit("FAILED %s: no closed <style> block" % path.name)
    for tag in ("</head>", "<body>", "</body>"):
        if tag in style.group(1):
            sys.exit("FAILED %s: %s ended up inside the stylesheet" % (path.name, tag))
    for token in ("--nv-h:", "--nav-h:", "--leaf-700:"):
        if token not in style.group(1):
            sys.exit("FAILED %s: %s missing from the stylesheet" % (path.name, token))
    if t.count("<script>") != 1 or t.count("</script>") != 1:
        sys.exit("FAILED %s: expected exactly one script block" % path.name)


def main():
    SHARE.mkdir(exist_ok=True)

    css = read("assets/nav.css") + "\n\n" + read("assets/team.css")

    # the typeface: inline it if we have a copy, otherwise fall back to the
    # system stack rather than leaving a request that a strict host will block
    if FONT.exists():
        css = re.sub(r'src: url\("https://static\.igem\.wiki[^"]*"\) format\("truetype"\);',
                     'src: url("%s") format("truetype");' % data_uri(FONT), css)
        print("  font: inlined %.0f KB" % (FONT.stat().st_size / 1024))
    else:
        css = re.sub(r'@font-face \{[^}]*static\.igem\.wiki[^}]*\}', '', css, flags=re.S)
        print("  font: no local copy, using the system stack")
        print("        (drop a .ttf at assets/inter-variable.ttf to embed it)")

    # the page must not inherit a dark ground from whatever is hosting it
    css = ':root { color-scheme: light; }\nhtml, body { background: #ffffff; }\n\n' + css

    nav_js = read("assets/nav.js").replace(
        '      const art = document.createElement("img");\n'
        '      art.className = "sitenav__railart";\n'
        '      art.src = tab.art || "assets/tab-icons/" + tab.id + ".png";\n'
        '      art.alt = "";\n'
        '      art.onerror = () => art.remove();\n'
        '      rail.appendChild(art);\n',
        '      if (tab.art) {\n'
        '        const art = document.createElement("img");\n'
        '        art.className = "sitenav__railart";\n'
        '        art.src = tab.art;\n'
        '        art.alt = "";\n'
        '        rail.appendChild(art);\n'
        '      }\n')

    js = "\n".join(inline_assets(x) for x in
                   [read("assets/nav-data.js"), nav_js,
                    read("assets/team-data.js"), read("assets/team.js")])

    page = read("team.html")
    title = re.search(r"<title>(.*?)</title>", page, re.S).group(1).strip()
    body  = re.search(r"<body>(.*?)</body>", page, re.S).group(1)
    body  = re.sub(r'\s*<link rel="stylesheet"[^>]*>', '', body)
    body  = re.sub(r'\s*<script src="[^"]*"></script>', '', body)
    body  = inline_assets(body).strip()

    # Keep head and body as separate strings. An earlier version split the
    # assembled string on its first blank line, which put </head><body> inside
    # the stylesheet the moment the CSS itself contained one.
    head_html = '<title>%s</title>\n<style>\n%s\n</style>' % (title, css)
    body_html = '%s\n\n<script>\n%s\n</script>' % (body, js)

    (SHARE / "_artifact-body.html").write_text(head_html + "\n\n" + body_html + "\n")
    (SHARE / "ReLeaf-team.html").write_text(
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8" />\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        + head_html + '\n</head>\n<body>\n' + body_html + '\n</body>\n</html>\n')

    # docs/index.html is what GitHub Pages publishes. noindex keeps a draft page
    # of students out of search results; delete that meta line when you want it
    # found.
    pub = ROOT / "docs"
    pub.mkdir(exist_ok=True)
    (pub / "index.html").write_text(
        (SHARE / "ReLeaf-team.html").read_text().replace(
            '<meta name="viewport"',
            '<meta name="robots" content="noindex, nofollow" />\n<meta name="viewport"', 1))

    for f in (SHARE / "ReLeaf-team.html", pub / "index.html", SHARE / "_artifact-body.html"):
        check(f)
        print("  %-24s %5.1f MB  ok" % (f.relative_to(ROOT), f.stat().st_size / 1024 / 1024))

if __name__ == "__main__":
    print("Bundling the team page...")
    main()
    print("Done. share/ReLeaf-team.html opens on its own with nothing beside it.")
