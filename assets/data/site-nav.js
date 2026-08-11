/* =============================================================================
   ReLeaf: site navigation
   -----------------------------------------------------------------------------
   Five tabs. Each opens a full-width panel: a title rail on the left, the
   sub-pages on the right, every one with its own icon and a one-line caption.

   To add a page:  drop an entry into the right tab's `pages` array.
   To add an icon: add a key to ICONS in nav.js (inner SVG markup, stroked,
                   24x24 viewBox) and reference it with `icon:`.
   Tab artwork:    each tab looks for assets/img/tab-icons/<id>.png (or .svg, set
                   `art:` to override). Missing files are skipped silently, so
                   the nav stays clean until the drawings arrive.
   ========================================================================== */

const NAV = [
  {
    id: "project",
    name: "Project",
    blurb: "The whole arc of the work, from the first sketch of the problem through the build cycles to the numbers we finished with.",
    pages: [
      { title: "Description",  href: "#", icon: "description",
        caption: "The problem we picked, the system we designed, and why it had to be alive." },
      { title: "Engineering",  href: "#", icon: "engineering",
        caption: "Every design, build, test and learn cycle we went through." },
      { title: "Contribution", href: "#", icon: "contribution",
        caption: "What we are leaving behind for the teams that come after us." },
      { title: "Results",      href: "#", icon: "results",
        caption: "What the system actually did on the bench." }
    ]
  },
  {
    id: "wetlab",
    name: "Wetlab",
    blurb: "Everything that happened at the bench: the runs and protocols, the parts we built and characterised, the plants we stressed, and how we measured and contained it all.",
    pages: [
      { title: "Experiments",  href: "#", icon: "experiments",
        caption: "Protocols, conditions and every run we made." },
      { title: "Parts",        href: "#", icon: "parts",
        caption: "What we built, what we characterised, what we registered." },
      { title: "Plants",       href: "#", icon: "plants",
        caption: "Working with the host, from seedling to stress." },
      { title: "Measurement",  href: "#", icon: "measurement",
        caption: "How we quantified expression and output." },
      { title: "Safety",       href: "#", icon: "safety",
        caption: "Containment, risk assessment and lab practice." },
      { title: "Notebook",     href: "#", icon: "notebook",
        caption: "The wet lab record, week by week." }
    ]
  },
  {
    id: "drylab",
    name: "Drylab",
    blurb: "The maths, the machine and the code. Reactor sizing, the model behind the light switch, our hardware and software, and the peptide designed to go with them.",
    pages: [
      { title: "Model (Math)",            href: "#", icon: "model",
        caption: "The equations behind sensing, expression and release." },
      { title: "Bioreactor Calculations", href: "#", icon: "bioreactor",
        caption: "Sizing, flow and mass transfer for the vessel." },
      { title: "Hardware",                href: "#", icon: "hardware",
        caption: "Enclosure, optics and electronics." },
      { title: "Software",                href: "#", icon: "software",
        caption: "Control code, analysis and tooling." },
      { title: "Peptide Design",          href: "#", icon: "peptide",
        caption: "Choosing and refining the protectant sequence." },
      { title: "Drylab Notebook",         href: "#", icon: "notebook",
        caption: "The computational record, week by week." }
    ]
  },
  {
    id: "engagement",
    name: "Engagement",
    blurb: "The world the project has to survive in. Who we talked to, what we taught, the rules we would have to meet, and where the need for this actually sits.",
    pages: [
      { title: "IHP",                  href: "#", icon: "ihp",
        caption: "The people who changed the project, and what they changed about it." },
      { title: "Education",            href: "#", icon: "education",
        caption: "What we taught, who we taught it to, and what stuck." },
      { title: "Sustainability",       href: "#", icon: "sustainability",
        caption: "Measuring ReLeaf against the SDGs." },
      { title: "Legal",                href: "#", icon: "legal",
        caption: "Regulation, approval routes and compliance." },
      { title: "GIS",                  href: "#", icon: "gis",
        caption: "Mapping where plant stress actually bites." },
      { title: "Data physicalization", href: "#", icon: "physical",
        caption: "Our data, rebuilt as objects you can pick up." },
      { title: "Entrepreneurship",     href: "#", icon: "entrepreneurship",
        caption: "The business case, what it costs, and how it would reach a field." }
    ]
  },
  {
    id: "team",
    name: "Team",
    blurb: "The forty-seven of us, a record of who did which part, and the photographs from a year of it.",
    pages: [
      { title: "Members",     href: "index.html", icon: "members", current: true,
        caption: "The students, advisors and instructors who built ReLeaf." },
      { title: "Attribution", href: "#", icon: "attribution",
        caption: "Who did what, and who helped us do it." },
      { title: "Gallery",     href: "#", icon: "gallery",
        caption: "Photographs from the bench, the field and the road to Paris." }
    ]
  }
];
