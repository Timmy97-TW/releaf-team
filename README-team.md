# ReLeaf team page

```
team.html                 the page: nav mount, group shot, section nav, profile view
assets/nav-data.js        site navigation: the five tabs and their sub-pages
assets/nav.js             nav renderer, 26 icons, open and close behaviour
assets/nav.css            nav styling
assets/logo.png           team badge at 200px, from 2026logo.png
assets/tab-icons/         drop the student drawings here (see the README inside)
assets/team-data.js       the roster. This is the file you edit.
assets/team.css           page styling
assets/team.js            card renderer, scroll-spy, profile view
assets/group.jpg          group shot at 2400px, 624 KB
assets/members/*.jpg      45 portraits, cropped 4:5 at 720x900, about 70 KB each
```

Open `team.html` in a browser. No build step, no dependencies, nothing loaded
from another server. Stylesheets and scripts carry `?v=21`; bump that number
after you edit them if the browser hands you a stale copy.

## Where the design came from

The layout and type follow iGEM Marburg 2024: Inter, a white page with tinted
card bodies, rounded corners, a portrait with an optional hover photo, a
`max-w-7xl` column. Two things differ because you asked for them, four cards to
a row instead of three, and a navbar at 68px instead of 80px.

The label system comes from Unicamp-Brazil, one colour-keyed pill per task on
every card.

## The label system

Task pills sit under each person's grade and school line, and they carry the
owner and member split from the 8/8 task table:

* **owner** gets a saturated fill, white text, a small dot and a soft shadow
* **member** gets the same hue washed back to a 16% tint, no shadow

The key explaining both sits at the very top of the page, above Project Leads,
under the subteam training definitions. There is no task filter.

**Three tasks outrank the rest.** Lab, Cloning and Bioreactor are the heaviest
jobs on the board, so they lead every card and their owner pills carry a
two-tone fill instead of a flat colour: indigo, garnet and deep teal. That comes
from `LABEL_GRADIENTS` in `team-data.js`, so promoting another label later is a
one-line change.

The other sixteen are flat, and coloured for what the work actually is: leaf
green for Plant, olive for Protectant, mint for Peptide Design, steel blue for
Model, copper for Hardware, paper for Lab Notebook, slate navy for Regulations,
warm orange for Outreach, amber for Education, rose for Art, plum grey for
Photography, cyan for Data Physicalization, and so on.

Nineteen labels in total. To add another, put one line in `LABELS` at the top of
`team-data.js`. Every card picks it up automatically.

## What each rank looks like

| | Card frame | Badge |
|---|---|---|
| Lead | boxed on all four sides, 3px dark green | filled green |
| Vice lead | top edge only, 3px light green | outlined green |
| Member | nothing | none |

Student Leaders is one grid, leads first, then vice leads. Each badge carries
its own title, Wet Lab Lead, Dry Lab Vice Lead, Cross-Team Lead and so on.

Student Members and Student Advisors run alphabetically, and so do the nine vice
leads. The six leads sit in a hand-set order (Abigail Lin, Abby Tsai, Abby Kao,
Anton Lin, then the rest alphabetically), so reorder those blocks in
`team-data.js` rather than sorting them. Instructors keep the order you set,
with Dr. Pak last.

## Subteam tracks

Every student also carries a subteam and a level, for example `Wet Lab · Major`
or `Dry Lab · Minor`. It sits on the same line as the lead title, to the right
of it, and it is styled to stay under the lead titles rather than beside them:
the role badge is brand green, the track badge is plain neutral grey, and a
minor is outlined where a major is filled. That gives the card three clear
tiers, role, then standing, then tasks.

To keep both badges on one line the track badge drops the subteam whenever the
role already names it, so a Wet Lab Lead reads `Wet Lab Lead` `Major`. It only
spells the subteam out when the two differ, which is exactly where it carries
information: Abby Kao reads `Cross-Team Lead` `Wet Lab · Major`, something the
lead title alone never told you.

The `team` field is gone. It said the same thing as the track badge, so the meta
line under each name is now just grade and school.

Counts: 15 Wet Lab majors, 6 Dry Lab majors, 4 Human Practices majors, 4 Wet Lab
minors, 2 Dry Lab minors. All 31 students are covered.

## The key at the top of the page

Three quiet columns under the heading "What a major means", one per subteam,
each led by a sample badge. Underneath, on a single hairline, the task owner and
task member definitions. No box around the whole thing beyond a soft off-white
panel, because it is meant to read as a light reminder of what the tags mean,
not as a policy.

There is deliberately no definition of a minor. The three columns say what a
major has done; anything else is a minor, and the page does not need to spell
that out.

## Open project lead seats

Project Leads shows four unclaimed seats rather than an empty box. Each is a
question mark behind a dashed outline with a Project Lead badge and nothing
else, wrapped in a 4px frame that runs a slow gradient from leaf green through
gold. A lead's frame is flat dark green, so an open seat reads hotter than a
held one, which is the point. Set `openSlots` on the section in `team-data.js`
to change the count, or remove it once someone takes the role.

## The profile view

Click any card. The panel is 940px wide over a dark backdrop, and two things on
it are generated from that person's own task list:

* the **frame** is a gradient built from their label colours in order
* the **sprig** watermarked into the panel carries one leaf per task, each in
  its task's colour

Abigail Lin runs indigo into garnet into green into rose into amber into purple.
Someone carrying six tasks ends up with a visibly richer frame than someone
carrying one, which is the point. Advisors with no tasks fall back to leaf
greens.

Bios are clamped to four lines on the card, with the browser's ellipsis and a
"Read more" cue. The profile view shows them in full.

## Sections

Project Leads, Student Leaders, Student Members, Student Advisors, Support Team,
Instructors. Only Project Leads, Student Advisors and Support Team carry a
caption; the rest run straight from heading into grid. Dr. Pak sits at the end
of the Instructors grid, badged Project Advisor.

A section with a caption shows the caption instead of an empty-state box.

## The site navigation

Five tabs, Project, Wetlab, Drylab, Engagement and Team, each opening a
full-width panel. It takes the mega-menu idea from Marburg and then goes its own
way:

| Marburg | ReLeaf |
|---|---|
| Three anonymous columns of links | A title rail on the left carrying your own artwork, a heading and a blurb, so a tab reads as a chapter |
| Filled purple circle with an icon-font glyph | Line art at 1.7px stroke in a soft rounded tile |
| The whole row floods solid purple on hover | Pale leaf wash, the tile inverts to dark green, and a green bar grows down the left edge |
| Purple 600 and 900 | Four steps of leaf green |
| | A 3px green gradient across the top of the open panel, matching the one under the group shot |

Every sub-page has its own icon and a one-line caption. All 26 icons are inline
SVG in `nav.js`, so nothing is fetched from outside.

**Tab artwork.** Each tab looks for `assets/tab-icons/<id>.png`, so
`project.png`, `wetlab.png`, `drylab.png`, `engagement.png`, `team.png`. Missing
files remove themselves, so the nav stays clean until the drawings land. Full
guidance is in `assets/tab-icons/README.txt`.

**To put the nav on another page**, add three things:

```html
<link rel="stylesheet" href="assets/nav.css" />
<div id="site-nav" data-tab="wetlab" data-home="index.html" data-logo="assets/logo.png"></div>
<div class="sitenav-spacer"></div>
...
<script src="assets/nav-data.js"></script>
<script src="assets/nav.js"></script>
```

`data-tab` marks which tab the page belongs to, and that tab keeps a green
underline. Mark the exact page with `current: true` on its entry in
`nav-data.js`. Every `href` is a `#` placeholder except `team.html`, so fill
them in as pages go live.

Below 940px the tabs collapse into a burger drawer where each tab is an
accordion, icons and captions intact.

## Editing the roster

Everything is in `SECTIONS` in `assets/team-data.js`:

```js
{ name: "Abby Tsai", role: "Wet Lab Lead",
  photo: "assets/members/abby-tsai.jpg",
  funPhoto: "assets/members/abby-tsai-fun.jpg",   // optional, shown on hover
  grade: "Freshman", school: "KCIS",
  track: "Wet Lab", level: "Major",
  bio:  "...",
  own: ["Plant","Art","Video"], mem: ["Cloning","Education"] }
```

Leave `photo` empty and an initials tile is generated, so the page never looks
broken. Portraits are cropped 4:5 from the top so heads sit high in frame. To
add one:

```bash
magick "individual photos/NAME.jpg" -auto-orient -resize 720x900^ -gravity north -extent 720x900 -strip -quality 82 assets/members/name.jpg
```

## Things to check

1. **The "Minor" definition is my wording.** You defined the three major tracks
   but not the minor, so the key currently reads "Works inside the subteam and
   contributes to its tasks without having gone through the full training run."
   Rewrite it in `legend()` in `team.js` if you want it put differently. It is
   the one line on the page that describes people by what they have not done, so
   it is worth a second read.
2. **"Ryan" for the Video task.** You wrote Ryan without a surname and there are
   two, so I gave it to Ryan Yuan. Ryan Wei has Protectant only.
3. **Dr. Pak has no photo and no bio**, so the card shows an initials tile.
4. **Ian Cheng is in.** He was not on your list of nine advisors, but you
   uploaded his photo and the spreadsheet has him as an advisor with a bio.
   Delete his block from `team-data.js` if that was a stray upload.
5. **`Q` (Sophomore, TAS)** is the one spreadsheet advisor still left out. That
   row has no real bio, just the word "Advisor". Who is it?
6. **Bruce Tsai** is the only person with no photo. Neo Su, Katherine Chen and
   Elizabeth Wong have photos but no bio text.
7. **Name merges** across the task table and the intro spreadsheet: Jac to
   Jacquelyn Inocencio, Sophie L to Sophie Liu, Sophie H to Sophie Huang,
   Audrey H to Audrey Hsieh, Ryan Y to Ryan Yuan, Abby T to Abby Tsai, Abby K to
   Abby Kao. The spreadsheet settled two others for me: bare "Sophia" in
   Outreach and Education is Sophia Lin, who is on human practices, not Sophia
   Yeh, who is wet lab; and bare "Olivia" is Olivia Du for the same reason.
8. **Bruce and Neo are advisors, not students**, despite appearing in the task
   table, so they sit under Student Advisors with their task pills kept.

Roster: 15 student leaders, 16 student members, 10 student advisors,
6 instructors. 47 people.

**Cloning is owners only now.** Abigail Lin, Chloe Wu and Sophie Chen hold it,
and nobody carries it as a member. The broader bench work moved to the new
**Lab** label, 6 owners and 13 members.

## Before this goes on the iGEM wiki

The wiki blocks resources from other servers. `team.css` currently pulls Inter
from Marburg's upload slot, so swap that `@font-face` source for your own team's
static URL and re-point the `photo:` paths at `static.igem.wiki`.

Cards are rendered in JavaScript, which is by far the easiest way to maintain a
47-person roster. If the iGEM validator or an accessibility review pushes back
on that, the same data can be pre-rendered into static markup. Say the word and
I will add a generator.
