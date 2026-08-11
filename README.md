# ReLeaf, iGEM 2026 team page

**Live: https://timmy97-tw.github.io/releaf-team/**

The team page for *ReLeaf: a stress-responsive optogenetic bioreactor for
precision plant protection*, GEMS Taiwan, iGEM 2026. Forty-seven people with
photos, bios, subteam standing and task labels, plus the five-tab navigation the
rest of the wiki will use.

## Layout

```
index.html              the page. Open it in a browser, that is the whole setup.
assets/
  css/                  nav.css, team.css
  js/                   nav.js, team.js
  data/                 site-nav.js  the five tabs and their sub-pages
                        roster.js    the forty-seven people
  img/                  logo.png, group.jpg, members/, tab-icons/
  fonts/                inter-variable.ttf
build/bundle.py         folds the whole page into one file
docs/index.html         the bundle GitHub Pages serves
dist/                   the same bundle for emailing (not committed)
notes/                  design.md, publishing.md
_source/                originals, local only (not committed)
```

Four kinds of file, four folders. Content lives in `assets/data`, appearance in
`assets/css`, behaviour in `assets/js`, and everything the browser downloads as
a file in `assets/img` and `assets/fonts`.

## Working on it

Open `index.html`. No build step, no dependencies, nothing fetched from another
server.

The roster is one file, `assets/data/roster.js`. Everything else reads from it:
the cards, the colour-keyed task pills, the per-person frames in the profile
view. `notes/design.md` covers the design decisions and how to edit the data.

Adding a page later: put it beside `index.html`, or in a folder with `../assets/`
in front of the paths, and mount the same nav with the three lines in
`notes/design.md`.

## Publishing

```bash
python3 build/bundle.py
git add -A && git commit -m "Update the team page" && git push
```

The bundler inlines every photo, the logo, the stylesheets, the scripts and the
typeface, and refuses to write a file whose stylesheet came out malformed. Pages
rebuilds on its own within a minute or so. `notes/publishing.md` covers hosting
elsewhere.

## Before this moves to the iGEM wiki

The wiki blocks resources from other servers. Re-point the `photo:` paths in
`assets/data/roster.js` and the `@font-face` source in `assets/css/team.css` at
your `static.igem.wiki` uploads.
