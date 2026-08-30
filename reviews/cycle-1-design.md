# Cycle 1 — Design review (Reviewer D)

Reviewed 2026-08-30 against `site-plan.md` §3 and `tools/COMPONENTS.md`. Desktop at 1440×1000 (Chrome, DPR 1), mobile via a 390px iframe, both themes. Screenshots in `reviews/screenshots/cycle-1/`.

## Verdict

1. **Does not clear the bar yet.** The bones are right — Newsreader/Archivo/JetBrains Mono are genuinely loading, the cool-paper neutrals, the numbered eyebrow, the hairline rules and the mono figure numbers all read as "edited report", not "generated". Nobody would mistake the type for a framework default.
2. **The single biggest failure is that the diagrams — the thing §3 says *is* the argument — do not hold their own system.** The two hues are supposed to mean US / India everywhere; on four of the twelve figures they mean something else (centralise/decentralise, capability/domain, tolerates/destroys, co-located/cross-site), a grey third colour appears, and Fig 4.2 has text drawn on top of boxes.
3. Every SVG renders its labels at **4–5 px on a 390px phone**. On mobile there is no figure on the site that can be read.
4. Two components are structurally broken at all widths: the marginalia rail pushes content down by its own height (a 200–270px hole after every case-study H2), and the learning-plan ranked list crams author and "Read:" into a 3rem number column.
5. The evidence chips are the loudest thing on case-studies.html — up to six solid ink blocks per paragraph — and become white blocks in dark mode. They are more visible than the headings.

Blocking: D1, D2, D3, D4, D5, D6. Fix those and the site is a strong major-fix pass away from the bar.

---

## Items

### Diagrams

**D1 · blocking — Fig 4.2 org topology overlaps itself** (applying-it.html, `figure:nth-of-type(2) svg`, viewBox 960×460). Screenshot `04-fig4.2-org-topology-overlaps-1440.jpg`, `07-mobile-390-fig4.2-org-topology.png`.
Problem: the three `fig-t2` lines at `x=20 y=315/330/345` ("Reporting lines: solid…") are drawn across the "Conversion funnels" (`y≈362–398`) and "US QoE liaison (1 seat)" (`y≈408–444`) boxes in the Commerce column at `x≈295–463`; the mono headcount line at `y≈430` runs through the liaison box; "Spine boxes are one reporting line…" (`y≈498`) collides with the `text-anchor=end` label "Team APIs · data contracts cross this line" at `x=748 y=440`. "Experimentation platform backend" and "Fraud & paid sharing — P3 candidate" both overrun their 178px boxes. The column headers "US DIRECTOR / data platform" are `fig-l` (ink-2) on the solid `--us` fill: 1.84:1 light, 1.87:1 dark — invisible.
Fix: grow the viewBox to `0 0 960 560`; move the two Commerce leaf boxes to `y=362` and `y=408` only if the note block moves to `y=480–525` below the lowest box; put the note in the empty right-of-spine area (`x=480 y=330–375`, where nothing is drawn) instead; set headers on solid fills to `class="fig-l fig-on"` (paper on us = 8.2:1); widen the India column boxes to 200px or shorten the two long labels ("Exp. platform backend", "Fraud & paid sharing · P3?"); put the "cross this line" label at `x=760 y=452` with `text-anchor=start`.

**D2 · blocking — all SVG text is 4–5 px on a 390px viewport** (every figure, all pages). Screenshots `06-mobile-390-fig2.1-timeline-unreadable.png`, `07-…`, plus measured `minSvgTextH: 4, medianSvgTextH: 5` on every page.
Problem: every figure is `viewBox="0 0 960 …"` with `width:100%`; at 390px the drawing is 350px wide (scale 0.365), so 11px labels render at 4px. Fig 2.1 (62 texts), 4.1, 4.2 and 3.1 are dense timelines/matrices that cannot survive this.
Fix (per figure, not one rule): (a) Fig 5.1, 5.2, 4.3, 1.2 — simple bar/band charts: give the figure `min-width: 640px` inside a `.fig-scroll { overflow-x: auto; }` wrapper on `max-width: 700px`, with a "scroll →" `fig-m` cue; (b) Fig 1.1, 3.2 — add a `<symbol>`-free second SVG with a mobile viewBox stacked (four models stacked 1-col, three rows of the ladder stacked) and swap via `@media (max-width: 700px) { .fig-desktop{display:none} .fig-mobile{display:block} }`; (c) Fig 2.1, 4.1, 4.2, 3.1, 1.3 — dense; add a `<details class="drill">`-style text-alternative table directly under the caption on mobile (the data is already in the prose/table on 2.1 and 4.1), and set the SVG `min-width: 760px` in a scroll wrapper. In all cases raise base label size in the SVG from 11px to 12px and `fig-l` from 10px to 11px so the desktop rendering is not also on the edge.

**D3 · blocking — the two-hue system changes meaning from figure to figure.** Screenshots `11-dark-fig2.1-timeline-third-colour.jpg`, `12-fig2.2-charter-map-1440.jpg`, `13-fig4.1-scoring-matrix-1440.jpg`, `17-fig5.1-gcc-maturity-1440.jpg`.
Problem: §3 says blue = US ownership, marigold = India ownership, "never a third colour". In practice: Fig 2.1 blue = centralisation, marigold = decentralisation/new site, **grey = M&A** (a third categorical hue); Fig 2.2 blue = capability charter, marigold = domain charter (all nine sites are remote sites, none is "US"); Fig 3.2 blue = "tolerates distance", grey = sequential, marigold = "destroys"; Fig 3.1 marigold dashed = "tension"; Fig 4.1 passes = solid blue dot (a unit that *passes* is one India gets, drawn in the US colour); Fig 5.2 blue = co-located, marigold = cross-site. A reader who has just learnt "marigold is India" from Fig 1.1 reads Fig 2.1 as "Spotify gave Echo Nest to India".
Fix: reserve the two hues strictly for site ownership. Categorical/valence encodings use ink weights and marks: Fig 2.1 — centralise = solid ink dot, decentralise = open ink circle, M&A = ink ring with a hairline tick, and colour only the *new-site* events that are genuinely India (Bengaluru, Hyderabad, India hub) in marigold; Fig 2.2 — draw both columns in ink/paper-2 and mark only India sites with a marigold left rule; Fig 3.2 — rows in `paper-2` with the "what distance does" cell in ink weight 400/600 and a ✓/✗ mark, no hue; Fig 3.1 — tension edges dashed ink-2, not marigold; Fig 4.1 — pass/partial/fail as ink solid / ink ring / ink-3 small; keep only the "First owner" pill in the site hue; Fig 5.2 — both bars ink, annotate 2.5× in `fig-m`. Add `stroke-dasharray` and marks so that no figure depends on hue alone (also fixes the colour-blind case).

**D4 · major — Fig 4.3 time-zone band labels fail contrast in both themes** (applying-it.html, third figure). Screenshot `08-dark-fig4.3-timezone-label-contrast.jpg`.
Problem: "09:00–18:00 local = UTC 16:00–01:00" on the Pacific bar is ink on solid `--us` (1.84:1 light / 1.87:1 dark); in dark mode the India bar label is ink on `--in` (1.85:1). The overlap window is a blended `--in-soft` rectangle — exactly the "blended third colour" §3 forbids for overlap.
Fix: labels on solid bars → `class="fig-t fig-on"`; or draw the bars as `-soft` fills with a 2px solid top rule and keep ink text (5.8:1 / 6.0:1). Draw the overlap window as interleaved 2px vertical stripes of `--us` and `--in` (`<pattern>`), not a tint. Wrap-around Pacific stub at UTC 00–01 needs its own tiny label ("→01:00") or a break glyph.

**D5 · major — Fig 3.1 edge labels are struck through by their own edges** (foundations.html). Screenshot `09-fig3.1-disagreement-map-labels-struck.jpg`.
Problem: "team floor vs / span ceiling" (`≈x 372–435, y 382–394`) and "stream-aligned bias / vs staffing reality" sit on the dashed marigold edge at `y=403`; "divisionalized form / = output control" sits on the Mintzberg–Data Mesh edge. No halo.
Fix: `paint-order: stroke; stroke: var(--paper); stroke-width: 4px; stroke-linejoin: round;` on `.fig-t2` and `.fig-l` inside figures (add to site.css), or break the edge into two segments with a 90px gap under each label. Also: Fig 3.2 appears before Fig 3.1 on the page — renumber.

**D6 · major — Fig 2.2 pill text overruns the pill** (case-studies.html). Screenshot `12-fig2.2-charter-map-1440.jpg`.
Problem: "Sky / Peacock UK whole streaming platform, reused for SkyShowtime, Showmax" runs ~20px past the 405px pill's right edge; the pills are `rx≈4` rounded soft-fill cards — the one place on the site that looks like a generic UI kit.
Fix: shorten to "whole streaming platform; reused by SkyShowtime, Showmax" on a second line at `fig-t2`, or widen the column to 440. Replace the rounded pills with the same flat rectangles + left rule used elsewhere (`rx="0"`, 2px `fig-stroke-us` on the left edge, `fig-paper2` fill) so the figures share one vocabulary.

**D7 · minor — Fig 1.3 decision-tree edges land on box corners.** (index.html, third figure.) "NO" edges run from the question's bottom centre to the *top-right corner* of the answer box; YES edges to the top-left. Reads as sketched. Fix: route edges orthogonally (down 20, across, down) or end them at the target's top-centre; keep the marigold highlight only on the sessions-and-QoE path (currently every YES edge is marigold, including the ones that lead to further questions).

**D8 · minor — Fig 1.2 has two legends.** The phase header row ("0 · 1 · PLATFORM · 2 · FIRST DOMAIN…") and the mono line "Phases: 0 Foundation · 1 Platform components…" say the same thing. Drop the mono line; put the phase names in the header. Left-edge inconsistency: the row labels start at x≈115 while every other wide element starts at the reading-column edge (x=92) — start labels at `x=0` with `text-anchor=start` or align the chart area to the column.

**D9 · minor — Fig 4.1 legend/footnote line runs the full 950px width at 10px.** Split: legend on the left (`y=466`), footnote as a second `fig-t2` line at `y=484` under it, max ~66ch.

**D10 · minor — Fig 2.1 label crowding 2023–2026.** Netflix: "Jan 2023 Warsaw hub / Feb 2026 CPTO" are stacked 12px apart; Disney and WBD have four labels within 120px. Fix: extend the axis to `x=1000→1040` (viewBox 1000 wide), use leader ticks and alternate above/below with a 3-level stagger, and drop the year where the month label already implies it.

**D11 · minor — figures' `<title>` naming is inconsistent.** Some begin "Fig. 2.1 —", most don't; `desc` exists on all 12 (good). Make all titles plain sentences; the figcaption carries the number.

### Layout & hierarchy

**D12 · blocking — the marginalia rail consumes a grid row.** (site.css `.body`, `.body > .rail`; case-studies ×8, applying-it ×2, learning-plan, charter-evidence.) Screenshots `03-case-studies-rail-gap-after-h2-1440.jpg`, `14-applying-it-table-rail-gap-1440.jpg`.
Problem: `.body` is `grid-template-columns: measure rail` with auto rows; a `.rail` placed after an `<h2>` shares the H2's row, so the row becomes 227–269px tall and the next `<h3>` starts 200px below the heading (measured `railH: 269, prevH: 39` on all eight case-study sections). After a `.wide` table the rail gets its own row with an empty left cell.
Fix: stop using grid rows for marginalia. `.body { display:block; padding-right: calc(var(--rail) + clamp(2rem,5vw,5rem)); } .body > .rail { float:right; clear:right; width:var(--rail); margin-right: calc(-1 * (var(--rail) + clamp(2rem,5vw,5rem))); }` (Tufte-CSS pattern), and `.body > .wide { clear:both; }`. Rails then sit beside the paragraph that follows them without affecting flow. Keep the ≤1100px inline fold as is.

**D13 · blocking — `.rank` grid mis-places `.by` and `.when`.** (site.css `.rank li`, learning-plan.html ×2 lists.) Screenshot `05-learning-plan-rank-grid-broken-1440.jpg`.
Problem: `grid-template-columns: 3rem 1fr` with children `::before, h3, .by, p, .when` auto-placed → `.by` ("Matthew Skelton & Manuel Pais · IT Revolution, 2025") and `.when` ("READ: MONTH 1 — BEFORE ANY ORG CHART IS DRAWN") land in the 3rem number column, one word per line.
Fix: `.rank li > * { grid-column: 2; } .rank li::before { grid-column: 1; grid-row: 1 / span 4; }` — or wrap the body in a `<div>` per COMPONENTS.md and update the two lists.

**D14 · major — the site nav overflows at 1440px.** Screenshot `01-index-1440-top.jpg` ("7 SOUR" clipped; measured `navScrollW 935 > clientW 897`).
Problem: 7 uppercase items at 12px + 0.08em tracking + brand tagline need ~1,020px; the `.brand em` only hides ≤1360px, so at the most common laptop width the last item is cut with no affordance (`scrollbar-width:none`).
Fix: hide the tagline ≤1500px, reduce nav letter-spacing to `.06em` and padding to `.45rem`, and on ≤1100px collapse to a "Contents ▾" `<details>` or a 2-row wrap. Never a hidden-scrollbar horizontal scroll for primary nav.

**D15 · major — mobile nav is a horizontally scrolling strip with no cue.** Screenshot `15-mobile-390-index-top-nav-clipped.jpg` ("RECOMMENDATION  CASE ST…").
Fix: as D14; at ≤640px show the section *number* only ("1 2 3 4 5 6 7", current one with the marigold rule) plus the current section's name — numbers are the plan's own navigation grammar.

**D16 · major — the page is left-stuck at desktop.** At 1440 the body grid is ~1,000px wide inside a 1,344px `.page`; header, footer and pager span the full 1,344 while text stops at x≈745 and the rail at x≈1,040, leaving a ~300px dead column on the right (`01-index-1440-top.jpg`). Fix: either cap `.page` at `calc(var(--measure) + var(--rail) + 5rem + 2*var(--gutter))` (≈72rem) so header/pager/footer align to the same right edge, or let `.wide` elements genuinely use the full 84rem. Pick one edge; today there are three (body ≈1,040, table ≈1,040, header 1,344).

**D17 · major — footer is 44px out of alignment.** `.site-footer .inner` left = 48px vs body left = 96px. Fix: `.site-footer { padding: 2rem 0 3rem } .site-footer .inner { padding: 0 var(--gutter); }`.

**D18 · minor — drill-down keys drift.** In `details.drill > summary` the `.k` ("1.6b") sits inline after short titles and at the far right of the measure after wrapping titles (flex + baseline). Fix: `margin-left:auto` on `.k` so it always right-aligns, or place it before the title in the mono column like the tripwire numbers.

**D19 · minor — h2s carry no running number** though the TOC and eyebrow do ("1.4 What it does to the whole org" in the TOC, plain "What it does to the whole org" as the heading). Add the mono number as `<span class="n">` in the h2 (Stripe Press-style), or remove it from the TOC.

### Typography

**D20 · pass with notes.** Fonts load (`document.fonts.check` true for all three; computed families confirm). Scale is the plan's 1.25 major-third; measure = 653px ≈ 66ch; body 18/1.55; `text-wrap: balance` on headings; h1 55px at 1440. Optical sizing works via the `opsz` axis (`font-optical-sizing:auto`). Hierarchy h1 → h2 (35) → h3 (22.5) → h4 (Archivo caps) reads cleanly.
Notes: (a) `.dek` at 22.5/1.4 in `--ink-2` is right; (b) nothing is centered — good; (c) the italic tagline in the brand is the only italic display use; pull-quotes/steelman heads per §3 are not italic anywhere — add `details.drill > summary em` or an `.steelman` style so the italic voice exists.

**D21 · major — citation superscripts are runs of unformatted numbers.** Screenshot `16-sup-citations-zoom.png` ("8 9 10 11 12", "44 50 19 22 42").
Problem: adjacent `<sup class="c">` elements are separated by a word-space and a blue mono digit each; five in a row is 40px of blue confetti after a sentence. Line-height is preserved (`line-height:0` — good).
Fix: build-step collapse of adjacent sups into one `<sup class="c">` with comma-separated links and ranges (`8–12`, `44, 50, 19, 22, 42` → sort → `19, 22, 42, 44, 50`); `sup.c a + a::before { content: ","; margin-right: .15em; color: var(--ink-3); }`. Colour the digits `--ink-2` not `--us`, so blue keeps meaning "US" in the figures.

**D22 · minor — small-text contrast.** Measured: `--ink-3` on paper 2.88:1 light / 3.92:1 dark; `--in` on paper 3.15:1 light. `--ink-3` is used for 11–12px text (`.meta`, `.eyebrow .num`, `figcaption .fig`, `.fig-m`, `.phases .ph`, `.src .acc`, `.toc .n`, `.tripwires li::before`); `--in` is used for `.rank .when` and `.judgment .label` at 12px. All fail AA (4.5:1).
Fix: darken `--ink-3` to `#6F7975` (4.2 → use `#68726E` for 4.6:1) in light and `#8A938F` in dark; give `.judgment .label` and `.rank .when` `color: var(--ink-2)` with a marigold left rule instead of marigold text. Large text uses of `--in` (thesis "India site" at 28–35px) pass at 3:1.

### Palette & dark theme

**D23 · pass with notes.** Every token resolves in dark; body 15.06:1; `--us` 8.0:1; `--in` 8.15:1; tags resolve (dark `tag-doc` is paper-on-ink = white block, see D25). The cool green-grey bias is present and does distinguish it from cream-and-terracotta. Selection colour, focus ring and progress hairline all use `--us` — correct per §3. Issues are D3/D4 (hue meaning), not the palette itself.

### Evidence chips

**D24 · blocking — chips dominate case-studies.** Screenshots `02-case-studies-chip-density-1440.jpg`, `10-dark-case-studies-chips.jpg`. 295 chips on one page; the opening paragraph has six solid `tag-doc` blocks inline; in dark mode they become bright white bars and are the highest-contrast element on the page.
Fix: (1) `tag-doc` is the *default* state — do not draw it at all inside prose; draw only `inferred` (outline) and `folklore` (dashed) inline, and state in the key "unmarked = documented". That removes ~70% of chips. (2) Make the remaining inline chips glyph-first: `◌ inferred` / `◌ folklore` at 10.5px in `--ink-2`, no fill, so they read as annotation not UI. (3) On table cells and the Sources list keep the full chips — there they are a column, not an interruption. (4) `judgment` stays as the marigold-outline chip but moves to the start of the paragraph only (it already mostly does).
The three shapes are distinct at desktop and in dark mode (`10-…jpg`); the outline vs dashed distinction is lost below ~100% zoom, which (1) also mitigates.

### Accessibility

**D25 · pass with notes.** One h1 per page; landmarks present (`header, nav×2, main, aside, footer`); skip link appears on focus (`18-…` verified); focus ring visible on nav links and `<summary>` (2px `--us`, offset 3px); `<details>` open with Enter/Space; every table has `<th>`; every SVG has `role="img"` + `title` + `desc`; `prefers-reduced-motion` kills transitions and smooth scroll.
Gaps: (a) colour is the only carrier in Figs 2.1, 3.2, 4.1, 5.2 (see D3); (b) `sup.c a` focus previews appear on focus but the tooltip is not `aria-describedby`-linked — add `aria-describedby` to the link while open; (c) `aria-current="page"` present — good; (d) the `.progress` bar has `aria-hidden` — good.

### Mobile

**D26 · major — sources.html has 7px horizontal overflow at 390px** (`scrollWidth 397 > 390`). Other six pages: no overflow; tables scroll inside `.tbl-wrap` (663/350, 469/350 measured); tripwires collapse to 2 columns and phases to 1 column correctly (`33-`, `34-` zooms). Fix: find the offending `.src li` (likely a long unbroken URL in `.url` on a row where `.tg` sits in col 2 with `gap:1rem`) — add `overflow-wrap:anywhere` to `.src li > *` and `overflow-x: clip` on `main`.

**D27 · minor — sticky header is 54px on a 390×844 screen (6.4%).** Acceptable; the brand serif at 18px is fine. But the eyebrow's hairline `::after` and the `page-head` 4rem top padding push the h1 to y=145 on mobile — reduce `.page-head` padding to `2.5rem 0 2rem` ≤640px.

### Performance

**D28 · pass with notes.** HTML: index 83KB (22KB gz), case-studies 124KB (31KB gz), sources 141KB (24KB gz), others 57–76KB; CSS 18KB (4.4KB gz); JS 2.3KB. Two pages exceed the plan's 120KB HTML+CSS budget uncompressed; both are the pages that *should* be long (219 source entries; 8 case studies) and they gzip to <32KB — justified, note it in the plan. Fonts: the Google CSS declares 21 `@font-face` blocks / 15 files across subsets, but a Latin page fetches 4: Newsreader variable regular 132KB (shared by 400 and 500), Newsreader italic 63KB, Archivo variable 35KB (400+600 in one file), JetBrains Mono 21KB — ~251KB, within the ≤6-file budget; `display=swap` and both `preconnect`s present. The Google CSS `<link>` is render-blocking (standard); consider `<link rel="preload" as="font">` for the Newsreader regular file to shorten the swap flash on the h1. No console errors on any page. Transfer for index.html ≈ 22KB HTML + 4.4KB CSS + 1KB JS + 251KB fonts.

### The "generated" test

**D29 · major — what gives it away, and what a studio would do.**
1. *Every figure is a 960-wide box in the same slot with the same caption block.* Studio move: vary scale with content — Fig 5.2 (two bars) should be a 40%-width inline figure in the rail; Fig 1.1 should bleed to the full 84rem; Fig 2.1 should be tall, not wide.
2. *Rounded soft-fill cards in Figs 2.2/3.2/4.2 (`rx=4`, tinted fills, thin border)* — this is the Figma-default node style. Studio move: flat rectangles, one hairline, labels set in the type system, ownership shown by a 3px rule not a tinted fill.
3. *Chips everywhere.* A studio would render evidence status as a single glyph in the margin (D24).
4. *Every page opens with the identical TOC-then-key block.* Move the tag key into the footer of the first section on each page or the site footer; keep the TOC only on pages with >6 sections.
5. *The right third of the desktop page is empty.* (D16.) Annual reports use that space: pull the key numbers (27%, 2.5×, 44%) into the rail as `--s5` Newsreader numerals with a mono caption — the "numbers set with dignity" §3 promises and nowhere delivers.
6. *Headings with no running numbers while the TOC has them* (D19) — small, but it is exactly what a template does and an editor doesn't.
7. *Citation runs "8 9 10 11 12"* (D21).
8. *No italic display voice, no pull-quote, no drop-anything.* The typography has one register. One italic Newsreader pull-quote per page (the Target "ownership of outcomes rests…" line on index; the Bryar & Carr line on case-studies) would give each page a single moment.

What is *not* generated-looking and should be protected: the cool paper, the numbered eyebrow with hairline, the mono `Fig. 1.1` labels, the phases/tripwires ledgers, the sources list, the `+ / −` drill-downs, and Figs 1.1 and 1.2 — those two are the design system working.

### Minor / polish

**D30 · minor** — `.answer` border-top is 3px ink while everything else is 1px: keep (it is the one heavy rule) but match with a 3px rule above the pager so it reads as a deliberate pair.
**D31 · minor** — `li::marker` in mono at 85% makes unordered bullets tiny grey dots; set `ul li::marker { content: "– "; }` or an en dash in `--ink-3`.
**D32 · minor** — `.judgment` box on applying-it is a full-width `paper-2` slab (`13-fig4.1-…jpg`, bottom); give it the same left-rule treatment as `.note` and drop the fill, or keep the fill only on the answer page.
**D33 · minor** — Fig 5.1 uses `#8A938F`-grey for Outpost and `paper-2` for Satellite: two neutrals plus marigold plus a paler marigold = four steps for a 4-category scale that is really 2 (execution vs ownership). Draw execution stages as two hatched ink tints, ownership as marigold solid + marigold hatched.
**D34 · minor** — case-study table header "DOMAIN ANALYSTS / SCIENTISTS REPORT TO" wraps three lines at 12px caps; shorten to "ANALYSTS REPORT TO".
