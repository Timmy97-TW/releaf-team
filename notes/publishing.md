# Putting the team page on a public URL

`docs/index.html` is the whole page in one file. Every photo, the logo,
the stylesheets, the scripts and the typeface are inside it, so any host that
can serve a static file can serve this. Nothing to build, nothing to configure.

Pick one of the three below. All give a URL that opens with no login.

---

## 1. GitHub Pages (recommended)

Free, permanent, and you will want the repo anyway once the rest of the wiki
starts. Roughly three minutes, all in the browser, no command line.

1. Sign in at **github.com** and click **New repository**.
2. Name it something like `releaf-team`, set it to **Public**, tick
   *Add a README file*, and create it.
3. On the repo page click **Add file → Upload files**, drag in
   `docs/index.html`, and commit.
4. Go to **Settings → Pages**. Under *Build and deployment*, set Source to
   **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
5. Wait about a minute and refresh. The URL appears at the top:
   `https://<your-username>.github.io/releaf-team/`

To update later, upload the new `index.html` over the old one. The URL does not
change.

---

## 2. Cloudflare Pages

Also free and permanent, and the upload is a single drag.

1. Sign in at **dash.cloudflare.com**, then **Workers & Pages → Create →
   Pages → Upload assets**.
2. Name the project, drag in the `docs` folder, and deploy.
3. You get `https://<project>.pages.dev`.

---

## 3. Netlify Drop (fastest, least durable)

1. Go to **app.netlify.com/drop**.
2. Drag the `docs` folder onto the page.
3. A public URL appears straight away. Claim it with a free account or it
   expires.

---

## Two things worth knowing

**The page is set to noindex.** `docs/index.html` carries
`<meta name="robots" content="noindex, nofollow">`, so search engines will not
list it. Anyone with the link can still open it. That felt like the right
default for a page carrying forty-odd students' photos, names, schools and
bios while it is still a draft. Delete that one line when you want it found,
or leave it, since the real iGEM wiki will carry the public version anyway.

**Re-run the bundler after any edit.**

```bash
python3 build/bundle.py
```

Then commit and push, or re-upload `docs/index.html` by hand. The bundler re-reads every file under
`assets/` and rebuilds all three outputs, so photos and roster changes carry
through on their own.
