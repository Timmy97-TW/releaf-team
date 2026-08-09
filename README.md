# ReLeaf, iGEM 2026 team page

**Live page: https://timmy97-tw.github.io/releaf-team/**

The team page for *ReLeaf: a stress-responsive optogenetic bioreactor for
precision plant protection*, GEMS Taiwan, iGEM 2026. Forty-seven people with
photos, bios, subteam standing and task labels, plus the five-tab site
navigation the rest of the wiki will use.

## Working on it

Open `team.html` in a browser. No build step, no dependencies, nothing fetched
from another server.

The roster lives in one file, `assets/team-data.js`. Everything else reads from
it: the cards, the colour-keyed task pills, the per-person frames in the profile
view. `README-team.md` explains the design decisions and how to edit the data.

## Publishing

`docs/index.html` is the whole page bundled into a single file, with every
photo, the logo, the stylesheets, the scripts and the typeface inlined. That is
what GitHub Pages serves. Rebuild it after any edit:

```bash
python3 build-share.py
```

Then commit and push. `share/ReLeaf-team.html` is the same bundle as a
double-clickable file for emailing to people who would rather not follow a link.

## Before this moves to the iGEM wiki

The wiki blocks resources from other servers, so re-point the `photo:` paths in
`assets/team-data.js` and the `@font-face` source in `assets/team.css` at your
`static.igem.wiki` uploads.
