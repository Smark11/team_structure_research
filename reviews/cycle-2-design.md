# Cycle 2 — Design review (Reviewer D)

Reviewed 2026-08-30 against `site-plan.md` §3, `reviews/cycle-1-design.md` and the author's dispositions in `reviews/cycle-1-responses.md`. Desktop at 1440×1000 (Chrome, DPR 1; nav also probed at 1200/1100/1024/960/901/899 via iframe), mobile via a 390×844 iframe, dark via `data-theme="dark"`. Screenshots in `reviews/screenshots/cycle-2/` (15 files). Contrast ratios computed from the token hex values in `site.css`.

## Verdict

1. **Closer, but does not clear the bar yet.** At 1440 in light mode, six of the seven pages now read as an edited report: the rail floats into the margin without eating a row, the numerals in the rail and the running numbers on h2s exist, Figs 4.1, 4.2, 4.3, 5.1, 1.2 and 3.2 are genuinely good, hue means site ownership everywhere, and the citation runs collapse to "10–15". Twenty-eight of the thirty-four cycle-1 items are verified applied.
2. **The biggest remaining failure is that the site is still not readable on a phone.** The three index figures never got the scroll wrapper (labels render at 4px), Fig 5.1 renders at 5.8px, the wrapped figures bottom out at 7.6–8.3px, and the number-only mobile nav is clipped on its left edge so sections 1–4 and the current section's own name are cut off and unreachable (`09-mobile-390-index-nav-clipped.png`).
3. **A build bug has introduced a new site-wide typographic defect**: the citation-run collapse eats the space after the run, so 64 sentences now run together ("…ownership does its damage.⁶˒¹⁶The delivery measures", "block.⁴˒¹⁴⁷The analyst reasons"). On case-studies the chip is also placed before the full stop, which strands a "." at the start of a line.
4. The desktop nav still overflows silently at every width between 900 and ~1130px (a 1024–1100px laptop never sees "7 Sources"); the foundations "So what" rails float after the last paragraph of each section and the numbered h2's `clear: both` leaves 140–430px of empty column before eight headings; the Sources chips get both the quiet-inline and the full-chip rule sets and render as grey-on-black, zero-padding blocks.
5. The "generated" tells that remain are small but they are exactly the ones an editor would never ship: 542 straight double quotes and 319 straight apostrophes in Newsreader (four curly quotes on the whole site), a three-line hedge as the pull-quote attribution, a `favicon.ico` 404, and "6,188 words · 27 min" under every h1.

Blocking: D2-1, D2-2, D2-3, D2-4. Major: D2-5 to D2-12. Fix the four blockers and the site is a polish pass from the bar.

---

## Verification of cycle-1 items

| # | Cycle-1 disposition | Cycle-2 finding | Status |
|---|---|---|---|
| D1 | Accepted | Fig 4.2 at 960×560: note block right of the spine, headers in paper on solid fills, no text over boxes, "cross this line" under the India column (`05-applying-it-fig4.2-1440.jpg`). | **Applied** |
| D2 | Modified | Label sizes raised (min rendered 11.2–12.1px at desktop). Scroll wrappers + cue on 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 4.3. **Not on 1.1, 1.3, 1.2 or 5.1** — index figures are `class="wide"` only and render at 350px wide with 4px text at 390; 5.1 at 5.8px. Wrapped figures at 720px min-width give 7.6px (2.1) / 8.3px (960-viewBox figures), below the 9px floor. | **Partial — blocking (D2-1, D2-8)** |
| D3 | Accepted | All twelve figures checked: `fig-us`/`fig-in` appear only on 1.1, 1.2, 1.3 (ownership), 2.1 (India rings), 2.2 (India left rule), 4.1 (owner pill only), 4.2 (site heads), 4.3 (site bars), 5.1 (India tiers, justified in caption). 3.1, 3.2, 5.2 have no hue. No hard-coded hex anywhere. | **Applied** |
| D4 | Accepted | Soft bars with solid top rule, ink text, interleaved `<pattern>` stripes for the overlap, "→01:00" stub labelled; holds in dark (`07-dark-fig4.3-stripes.jpg`). | **Applied** |
| D5 | Accepted | `paint-order: stroke` halo on all four text classes; 3.2 labels sit clear of edges; figures renumbered (3.1 ladder, 3.2 map). | **Applied** |
| D6 | Accepted | Flat `rx="0"` rectangles with a marigold left rule; Sky/Peacock on two lines. Google Zurich's second line runs ~2px past its box (D2-13). | **Applied** |
| D7 | Accepted | Orthogonal edges, marigold only on the QoE path. | **Applied** |
| D8 | Accepted | One legend; phase names in the header row; "0 · Foundation" in the gutter; chart at x=0. | **Applied** |
| D9 | Accepted | Legend left, footnote on two ≤66ch lines. | **Applied** |
| D10 | Accepted | 1040-wide viewBox, 3-level stagger with leader ticks. Still tight around Disney 2024–25 but readable. | **Applied** |
| D11 | Accepted | All twelve `<title>`s are plain sentences. | **Applied** |
| D12 | Accepted | Float-into-padding. Case-studies: h2→h3 gap 36px beside every rail (was 227–269). No rail overlaps a `.wide`. **New side effect on foundations** (D2-5). | **Applied, with regression** |
| D13 | Accepted | `.rank li > * { grid-column: 2 }`; all children at x=256, number spans rows. | **Applied** |
| D14 | Accepted | Fits at 1440 and 1280 (892/892). **Overflows 900–~1130px** with the hidden scrollbar still in place: 1100 = 892/870, 1024 = 892/800 (`13-nav-1024-sources-clipped.png`). | **Partial — blocking (D2-4)** |
| D15 | Modified | Number-only nav ≤900. **Clipped on the left** because `.site-nav ol { justify-content: flex-end }` inside an `overflow-x: auto` box puts the overflow on the unscrollable side (`09-mobile-390-index-nav-clipped.png`). | **Not working — blocking (D2-2)** |
| D16 | Accepted | One right edge: nav, page-head, body, every `.wide`, pager and footer content all end at x=1248 on all seven pages. | **Applied** |
| D17 | Accepted | Footer inner left = 192 = body left. | **Applied** |
| D18 | Accepted | `.k` right-aligned with `margin-left: auto`. | **Applied** |
| D19 | Accepted | Running numbers on every body h2 on six pages (7/7, 11/11, 12/12, 7/7, 6/6, 5/5). Sources' one h2 has none (D2-15). | **Applied** |
| D20 | pass | `.pull` exists on index only; attribution and styling issues in D2-11. | **Applied, see D2-11** |
| D21 | Accepted | Runs collapsed and sorted ("21–24", "19, 22, 42, 44, 50"), digits in ink-2. **The space after the run is dropped** (D2-3). | **Applied, with regression** |
| D22 | Accepted | Light `--ink-3` #68726E = 4.54:1 on paper (pass), 4.18:1 on paper-2 (fail). **Dark `--ink-3` unchanged at #6E7773 = 3.92:1.** `.judgment .label` and `.rank .when` now ink-2 (7.1:1) with a marigold rule — pass. Inline `◆ judgment` chip is `--in` at 10px = 3.15:1 light. | **Partial (D2-9)** |
| D23 | pass | Every token resolves in dark; no colour defined in one theme only. | **Pass** |
| D24 | Modified | Inline chips are glyph-first, unfilled, 10px. Solid blocks gone from prose; tables and key keep full chips. **Sources list gets both rule sets** (D2-6). Chip placed before the full stop on case-studies (D2-7). | **Applied, with two regressions** |
| D25 | Modified | `aria-describedby="cite-pop"` set while the preview is open and removed on hide (`site.js` lines 34–47). Focus ring 2px `--us` on citation links confirmed by keyboard. `details.alt > summary` inherits the global `:focus-visible` rule (no override). Landmarks: header, nav[Sections], main, aside×n, nav[Previous and next], footer. Reduced-motion rule present. | **Applied** |
| D26 | Accepted | sources.html at 390: `scrollWidth − 390 = 0`; no `.src li` extends past 390. | **Applied** |
| D27 | Accepted | h1 top at y=128 on 390 (was 145); header 54px. | **Applied** |
| D28 | Accepted | Per page load: one Google CSS fetch (preload + stylesheet share the URL, not double-fetched), four woff2 files. Gzipped HTML 15–29KB. `favicon.ico` 404 on every page (D2-12). | **Applied** |
| D29 | Modified | Rail numerals (index: "2.5 ×", "45–50"), flat rectangles, Fig 5.2 inline at 22rem, running numbers, citation runs, one pull on index. Key/TOC kept per author. | **Applied as modified; see D2-16, D2-20** |
| D30 | Accepted | Pager top rule 3px ink, pairs with `.answer`. | **Applied** |
| D31 | Accepted | En-dash markers on unclassed lists. | **Applied** |
| D32 | Accepted | `.judgment` is a left-rule block, no fill. | **Applied** |
| D33 | Accepted | 5.1: ink solid + ink hatch, marigold solid + marigold hatch; hatching reads in dark. | **Applied** |
| D34 | Accepted | "Analysts report to". | **Applied** |

---

## Items

### Blocking

**D2-1 · blocking — the three index figures were never wrapped; 4px labels at 390.** (index.html, `figure.wide` ×3 — Figs 1.1, 1.3, 1.2.) Screenshot `10-mobile-390-fig1.1-unreadable.png`.
Problem: measured `minSvgText 4 / median 4` on index at 390; the SVGs are 350px wide. The first figure a phone reader meets is the one that carries the whole argument. Fig 1.3 (27 texts) and 1.2 (39 texts) are the same.
Fix: `<figure class="wide scroll">` on all three with the `<p class="cue">scroll →</p>` line, and `details.alt` on 1.1 (link to the §1 ownership table) and 1.3 (the four questions as a 4-row table). Fig 1.2 needs no alt (the phases ledger below it is the alt).

**D2-2 · blocking — the mobile nav is clipped on the left and cannot be scrolled.** (site.css `@media (max-width: 900px)`, all pages.) Screenshot `09-mobile-390-index-nav-clipped.png` ("ATION 2 3 4 5 6 7"); charter-evidence shows "5 CHARTER EVIDENCE 6 7" with 1–4 gone.
Problem: at 390 the nav box is ~213px but the list needs ~275 (current name + six numbers). `.site-nav ol { justify-content: flex-end }` inside `.site-nav { overflow-x: auto }` pushes the excess to the *start* edge, which browsers do not let you scroll to. `scrollWidth === clientWidth` (208/208) confirms the overflow is invisible to the layout engine too.
Fix: the eyebrow 60px below already carries the section name, so the header does not need it. `@media (max-width: 640px) { .site-nav a .t { display: none; } .site-nav a { padding: .9rem .45rem; } .site-nav ol { justify-content: flex-start; } .site-nav { overflow: visible; } }` — seven numbers at ~26px each = 182px, fits beside the brand at 390. Between 641 and the new desktop breakpoint (D2-4) keep the current-name variant but with `justify-content: flex-start` and `overflow: visible` so overflow can never be silent.

**D2-3 · blocking — sentences run together after collapsed citation runs.** (Build step; 64 instances: index 10, case-studies 19, foundations 9, applying-it 11, charter-evidence 15.) Screenshots `03-case-studies-chips-eaten-space-1440.jpg` ("…businesses ● DOCUMENTED.²¹˒²⁴˒⁴⁷˒⁴⁹˒⁵⁵The counter-examples"), `02-index-fig1.1-1440.jpg` caption of Fig 1.2 ("damage.⁶˒¹⁶The delivery measures").
Problem: HTML is `…</sup>The counter-examples` — the whitespace that followed the last of the merged `<sup>`s was dropped when adjacent sups were joined. `grep -o '</sup>[A-Za-z"(]' docs/*.html | wc -l` = 64.
Fix: in the collapse step, capture the whitespace after the final sup in the run and re-emit it after the merged `<sup>`; regression test: `</sup>[A-Za-z"(]` must return zero.

**D2-4 · blocking — desktop nav still overflows silently from 900 to ~1130px.** (site.css `.site-nav`, `@media (max-width: 900px)`.) Screenshot `13-nav-1024-sources-clipped.png` ("7 SOURCES" absent at 1024).
Problem: measured 1100 → 892/870, 1024 → 892/800, 960 → 892/741, 901 → 892/687; 899 → 318/318. `scrollbar-width: none` hides the only affordance. A 13" laptop with a sidebar or a 1024 tablet in landscape never sees the Sources link.
Fix: raise the number-only breakpoint: `@media (max-width: 1140px)` instead of 900 (nav at 1140 needs 892 ≤ 1140 − 96 − 113 − 24 = 907: fits). Delete `.site-nav { overflow-x: auto; scrollbar-width: none }` and the `::-webkit-scrollbar` rule entirely; if it ever overflows again it must show.

### Major

**D2-5 · major — foundations' "So what" rails strand an empty column before every h2.** (foundations.html ×8; site.css `h2 { clear: both }`.) Screenshot `04-foundations-stranded-rail-gap-1440.jpg`.
Problem: each rail is placed after the section's last paragraph. A right float placed after a block starts *below* that block, so the rail sits beside nothing; the next h2 clears it, and the reading column is empty for the rail's height: gaps of 334, 292, 292, 250, 229, 187, 481 and 271px between the last paragraph and the next heading (measured prev-bottom → h2-top). On applying-it and case-studies the rails follow an h2 or sit mid-section, so they are fine.
Fix (content): move each `<aside class="rail">` to *before* the paragraph it comments on (the section's opening paragraph, as on case-studies). Fix (CSS, if the order must stay): `.body > .rail + h2 { clear: none; }` is not acceptable (a 35px heading wrapping beside a rail); instead convert the eight to in-flow `.judgment` blocks on this page only. The content fix is the right one.

**D2-6 · major — Sources list chips get both rule sets.** (site.css: `p .tag, li .tag, …` vs `.src .tag-doc`.) Screenshot `06-sources-chip-broken-zoom.png`.
Problem: `.src li` is an `li`, so `li .tag` strips padding, sets 10px, colours the text `--ink-3` and adds the "●" glyph; then `.src .tag-doc { background: var(--ink) }` re-applies the fill. Computed: `bg rgb(22,33,31)`, `color rgb(104,114,110)` (2.5:1), `padding 0`, `::before "●"`. 216 chips plus the 13 consulted entries.
Fix: scope the quiet-chip rules so they cannot reach the list: replace every `li .tag` selector with `li:not(.src li) .tag` (and the `::before` variants), or simpler, add after the chip block: `.src .tag, td .tag, .tag-key .tag { padding: .3em .5em .28em; font-size: 10.5px; letter-spacing: .08em; color: inherit; } .src .tag::before, td .tag::before, .tag-key .tag::before { content: none; } .src .tag-doc, td .tag-doc, .tag-key .tag-doc { color: var(--paper); border-color: var(--ink); }`.

**D2-7 · major — chip placed before the full stop on case-studies; orphaned "." at line start.** (Build; 139 `</span>.` on case-studies, 1 each on index and charter-evidence.) Screenshot `08-dark-chips-period-orphan-zoom.png` ("…home base for ML ● DOCUMENTED" / ".⁸⁴ By 2022").
Problem: case-studies emits `claim <span class="tag">documented</span>.<sup>…</sup>`; index emits `claim.<sup>…</sup> <span class="tag">`. The chip is `white-space: nowrap` and 60–80px wide, so it wraps as a unit and leaves the full stop on the next line.
Fix: one order everywhere — *period, citation run, space, chip*: `claim.<sup class="c">…</sup> <span class="tag …">`. Also give the chip `margin-left: .35em` only (already) and never a preceding space inside the sentence.

**D2-8 · major — scroll-wrapped figures still fall below the 9px floor on a phone; Fig 5.1 not wrapped.** (site.css `figure.scroll svg { min-width: 720px }`; charter-evidence Fig 5.1.) Screenshots `11-mobile-390-fig2.1-scroll.png` (7.6px labels), `12-mobile-390-fig5.1-small.png` (5.8px).
Problem: 720/960 = 0.75 → `fig-l` 11px renders at 8.3, `fig-m` 11.5 at 8.6; Fig 2.1 at 720/1040 = 0.69 → 7.6px. Fig 5.1 (viewBox 720, `figure.wide` only) scales to 350 → 5.8px for "Outpost 13%".
Fix: `figure.scroll svg { min-width: 800px; }` and for Fig 2.1 an inline `style="min-width: 880px"` (both give ≥ 9.2px for `fig-l`); wrap 5.1 in `figure.wide.scroll` (renders at 1:1 = 12px) — or, better for a two-segment bar, stack the four labels under the bar in two rows so it survives at 350 without scrolling. The `scroll →` cue is visible and reads well where present.

**D2-9 · major — small-text contrast, second pass.** (site.css tokens and chip colours.)
Problem, computed: dark `--ink-3` #6E7773 on #121716 = **3.92:1** (unchanged; cycle 1 asked for #8A938F). Light `--ink-3` on `--paper-2` = 4.18:1 (table stripes, `fig-paper2` fills under `fig-m` text). Inline `p .tag-judg { color: var(--in) }` = **3.15:1** at 10px in light. `○ folklore` glyph at 9px in ink-3 is invisible in dark (`08-dark-chips-period-orphan-zoom.png`).
Fix: dark `--ink-3: #8A938F` (5.5:1); `p .tag-judg … { color: var(--ink-2); } p .tag-judg::before … { color: var(--in); }` (marigold stays on the glyph and the underline); glyph size 11px (`::before { font-size: 11px }`) so ◐ and ○ are distinguishable; `.fig-m` inside `paper-2` fills → use `fig-ink2`.

**D2-10 · major — straight quotes throughout.** (All pages; counted on rendered text after stripping tags: 542 straight `"`, 319 straight apostrophes, 4 curly.) Screenshot `01-index-pull-quote-1440.jpg` (`"…ownership of outcomes`), `02-index-fig1.1-1440.jpg` (`Why "whole components,"` in a 22px Newsreader heading).
Problem: this is the single most reliable "generated" tell in a serif setting, and it hits the pull quote, the h3s in the drill-downs, the Fig 1.1 caption and every quoted source phrase.
Fix: a smart-quotes pass in the build on text nodes only (skip `<code>`, `.url`, `<template>`, SVG `<text>` attributes): `"x` → `“x`, `x"` → `x”`, `'` between letters → `’`, leading `'` → `‘`. Add `hanging-punctuation: first` on `.pull` and `blockquote`.

**D2-11 · major — the pull quote does not yet earn its place.** (index.html line 63; site.css `.pull`.) Screenshot `01-index-pull-quote-1440.jpg`.
Problem: (a) the attribution is a 45-word editorial hedge set in 14px sans over three lines — the hedge belongs in the prose, not under the quotation; (b) `.pull` and `blockquote` are the same device (marigold left rule, italic), so the page's one display moment looks like another callout; (c) only index has a pull; the plan promised one per page and the Bryar & Carr line on case-studies is still inline.
Fix: `.who` → "Target's India president, 2024¹⁷" and move the sentence "one executive's sentence in one interview…" into the paragraph above. CSS: `.pull { border-left: 0; padding-left: 0; margin: 3rem 0; font-size: var(--s3); hanging-punctuation: first; max-width: 26ch; } .pull::before { content: "“"; display: block; font-size: var(--s5); line-height: .6; color: var(--in); margin-bottom: .2em; }` — the marigold opening mark replaces the rule. Add one pull to case-studies and foundations.

**D2-12 · major — `favicon.ico` 404 on every load.** (All pages.)
Fix: in `tools/page-template.html` `<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' fill='%23F4F5F1'/%3E%3Crect x='3' y='3' width='10' height='10' fill='%23C27A1E'/%3E%3C/svg%3E">` — the marigold square is the site's own mark.

### Minor

**D2-13 · minor — text overruns boxes by 2–6px in Figs 2.2 and 3.1.** Fig 2.2 "~5,000 people; analytics function not documented as Zurich-owned (inferred)" (x=514, box ends at 1148 in screen px) and Fig 3.1 "cross-site items take about 2.5x as long" (`15-case-studies-fig2.2-1440.jpg`; foundations screenshot). Fix: shorten to "~5,000 people; analytics not documented as Zurich-owned" and "cross-site items take ~2.5× as long", or widen the two right-hand columns by 12 units.

**D2-14 · minor — Sources entry 1 says "tertiary" twice** ("— Tertiary" after the year and "tertiary" under the chip); 13 entries carry the suffix. Keep one: the suffix on the meta line, delete the label under the chip.

**D2-15 · minor — the Sources "Consulted in the research, not cited on the site" h2 is the only un-numbered h2 on the site** and the page has no TOC. Number it (`<span class="n">7.2</span>`, with the cited list as 7.1) or, since Sources is a list not an essay, keep both un-numbered and drop the eyebrow number as well. Pick one rule. The section itself is right: same list grammar, numbered after 203, one sentence of intro.

**D2-16 · minor — Fig 5.2 inline is a stub, not a figure.** (charter-evidence, `figure.inline-rail`.) Two bars at 22rem in the reading column, "1×" at 11.5px mono ink-3, and the 2.5× set in JetBrains Mono while the rail numerals elsewhere are Newsreader. A studio would put it in the rail beside "Herbsleb and Mockus (2003)": `<aside class="rail"><span class="label">Calendar time per item</span><span class="big">2.5<small>×</small></span> …two bars…</aside>` — same voice as the index rail. If it stays inline, set the 2.5× in `--serif` at `--s4` and drop the mono.

**D2-17 · minor — h2 is fixed at 35px on mobile.** "Galbraith: the Star Model and the information-processing view" is four lines at 390 (foundations screenshot). Fix: `h2 { font-size: clamp(var(--s3), 2.2vw + 1.1rem, var(--s4)); }`. The running number does not collide with long headings — verified on all 49 h2s.

**D2-18 · minor — Fig 1.3 uses two blues without saying why.** "Stays US-anchored" is solid `--us` with paper text; "Do not transfer. Run as an extension" is `--us-soft` with ink text. Both mean "US keeps it"; the soft one means "not even transferred". Add a two-item legend line under the tree (`fig-m`): "solid = US owns · tint = never transfers", or make both solid.

**D2-19 · minor — the tag key teaches the wrong chips.** `.tag-key` shows the full filled chips, but a reader meets the glyph forms (● ◐ ○ ◆) in every paragraph; the key never shows a glyph. Add the inline form to each key item: `<span><span class="tag tag-doc">documented</span> <small>● in prose</small></span>` — or render the key with the glyph form and keep the filled form only in tables.

**D2-20 · minor — "6,188 words · 27 min" under every h1** is a blog-template convention; Stripe Press and annual reports do not count words at you. Replace `.meta` with "Section 1 of 7 · Sources accessed 2026-08-29" or drop the count and keep the access date.

**D2-21 · minor — Fig 3.1 has a scroll wrapper but no `details.alt`**; it is a 3×3 grid and the easiest alt table on the site. Add it (rows: pooled/sequential/reciprocal; columns: mechanism, what the gap does). Fig 3.2's alt is prose ("the four tensions") with 0 rows — fine, but title it "The four tensions, in words" rather than "Text alternative: …", which is UI language.

**D2-22 · minor — figure captions are paragraphs.** Fig 4.3's caption is eight lines; 1.1's is seven (it carries the key). A caption of that length under a `Fig. 4.3` mono label is a report template's habit. Cap captions at three lines: the argument ("This is why the interface between sites must be a contract…") belongs in the prose beside the figure; the key for 1.1 belongs in a `fig-m` line inside the SVG.

**D2-23 · minor — `sup.c a + a::before` comma.** Reads "8, 16" — fine at desktop; at mobile the `.05em` padding plus `.12em` margin makes "21 , 24" (`11-mobile-390-fig2.1-scroll.png` caption). Set `sup.c a { padding: 0 }` and `sup.c a + a::before { margin-right: .1em }`.

**D2-24 · minor — one 77px gap above an h2 on applying-it** (h2 after a figure: 2.5rem figure margin + 3.5rem h2 margin collapse incompletely because the figure has `details.alt` inside). Set `figure { margin-bottom: 2rem }` and `figure + h2 { margin-top: 3rem }`.

**D2-25 · minor — keyboard automation note.** Synthetic Tab events in the Chrome tooling do not move focus, so the `details.alt` summary was verified by rule only: it is a native `<summary>`, there is no `outline: none` anywhere in `site.css`, and the global `:focus-visible` (2px `--us`, offset 3px) applies. Citation links were verified by real keyboard focus (ring + preview + `aria-describedby`). No item raised.

### The "generated" test, second pass

What now reads as edited: the rail numerals ("2.5 ×", "45–50" in Newsreader at 44px with a caps label), the running numbers, the one right edge, Figs 4.1/4.2/4.3/5.1 as a family (flat rectangles, ink marks, hue only for ownership, halo'd labels), the collapsed citation runs, the `.judgment` and `.note` left-rule blocks, the pager's 3px rule pairing with the answer block, and dark mode holding every figure including the striped overlap and the hatching.

What still gives it away, in order: (1) straight quotes in a serif face (D2-10); (2) sentences fused to their citations (D2-3); (3) the phone experience (D2-1, D2-2, D2-8); (4) the word-count/read-time line and the eight-line captions (D2-20, D2-22); (5) the pull quote's hedge and its sameness with `blockquote` (D2-11); (6) one pull on one page — the italic register exists but is not a habit; (7) no favicon; (8) the key teaching chips the reader never sees inline (D2-19).

What a studio would do in the next pass, after the blockers: smart quotes and `hanging-punctuation`; a pull on every essay page; captions to three lines with the argument moved into prose; Fig 5.2 into the rail; h2 fluid on mobile; delete the read-time; and consider giving the four ownership figures (1.1, 1.2, 4.1, 4.2) a shared 2-line legend component rendered from one template so the legends stop drifting in wording ("US owns" vs "US · —" vs "US owns, India contributes").

Screenshots: `reviews/screenshots/cycle-2/01-index-pull-quote-1440.jpg`, `02-index-fig1.1-1440.jpg`, `03-case-studies-chips-eaten-space-1440.jpg`, `04-foundations-stranded-rail-gap-1440.jpg`, `05-applying-it-fig4.2-1440.jpg`, `06-sources-chip-broken-zoom.png`, `07-dark-fig4.3-stripes.jpg`, `08-dark-chips-period-orphan-zoom.png`, `09-mobile-390-index-nav-clipped.png`, `10-mobile-390-fig1.1-unreadable.png`, `11-mobile-390-fig2.1-scroll.png`, `12-mobile-390-fig5.1-small.png`, `13-nav-1024-sources-clipped.png`, `14-applying-it-fig4.3-1440.jpg`, `15-case-studies-fig2.2-1440.jpg`.
