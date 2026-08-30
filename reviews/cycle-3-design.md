# Cycle 3 — Design review (Reviewer D)

Reviewed 2026-08-30 against `reviews/cycle-2-design.md`, the dispositions in `reviews/cycle-2-responses.md`, and `site-plan.md` §3. Desktop at 1178×844 (Chrome, DPR 2; nav probed at 1280/1140/1100/1024/960/641/390 via iframe), mobile via a 390×844 iframe, dark via `data-theme="dark"`. Label sizes and SVG overflow measured programmatically (getBBox against each viewBox; rendered font-size × scale at 390). Contrast computed from the token hex values. Screenshots in `reviews/screenshots/cycle-3/` (10 files).

## Verdict

1. **Very close, but not zero-blocking yet: two clipped SVG text lines block, both introduced by cycle-2 fixes and both one-line repairs.** Fig 1.1's key (moved inside the SVG per D2-22) runs to x=1066 and x=1217 in a 960-unit viewBox and is cut mid-word — "QOE quality of experienc" — at every viewport; Fig 1.3's new legend (D2-18) runs to x=1096 and is cut the same way. Clipped text on the two figures a reader meets first cannot ship.
2. Everything that blocked cycle 2 is verified fixed: zero fused sentences (`</sup>[A-Za-z"(“]` = 0 site-wide), zero straight quotes in rendered text (0 double, 0 apostrophes; no misplaced curly), the mobile nav shows all seven numbers at 390 with nothing clipped, and the nav never overflows silently at 1280/1140/1100/1024/960/641 (numbers-only below 1140, hidden-scrollbar rules deleted).
3. The deferred items landed and read well: Fig 5.2 is now a rail — "Calendar time per work item / 2.5×" in Newsreader with two ink bars — beside the distributed-work section; Fig 3.1 has "The ladder as a table"; pull quotes with the marigolds opening mark sit on index, Case Studies and Foundations with one-line attributions. Dark mode holds on all seven pages including the striped overlap, the 5.1 hatching and the full-chip tables; dark `--ink-3` is 5.73:1.
4. One new markup bug: `tools/build.py` `entry_html` emits literal `class=&quot;who&quot;` and `class=&quot;q&quot;` (276 entities in sources.html), so every note ("— Tertiary") and qualifier renders unstyled in ink instead of the small sans treatment — visible on dozens of Sources entries (major, not blocking: same face, wrong colour/size). Fig 1.2's "G0" tick label collides with its header line (major). Minor: five mid-sentence chips still precede their citation; Fig 2.1 renders 8.5px labels at 390 against the 9px floor.
5. **The "generated" test now passes.** Smart quotes, hanging punctuation, the marigold pull marks, the rail numerals, "Section N of 7" instead of a word count, the favicon, the glyph-teaching key — nothing on the site reads templated any more; the two clipped lines read *broken*, not generated. Fix D3-2 and D3-3 (and ideally D3-1) and the site clears the bar.

Blocking: D3-2, D3-3. Major: D3-1, D3-4. Fix the two blockers — both are "shorten or wrap one line of SVG text" — and this reviewer ships it.

---

## Verification of cycle-2 items

| # | Cycle-2 disposition | Cycle-3 finding | Status |
|---|---|---|---|
| D2-1 | Accepted | Figs 1.1, 1.3, 1.2 are `figure.wide.scroll` with the cue; alt tables on 1.1 (fourteen units, opens correctly) and 1.3 (four questions); measured at 390: min 9.2px on all three (scale 0.833 × 11px). | **Applied** |
| D2-2 | Accepted | 390 iframe: seven numbers visible (7/7), first item left = 179 ≥ 0, last right = 370 ≤ 390; `flex-start` + `overflow: visible` in CSS (`09-mobile-390-index-nav.png`). | **Applied** |
| D2-3 | Accepted | `grep -o '</sup>[A-Za-z"(“]' docs/*.html \| wc -l` = 0. Collapse regex re-emits trailing whitespace. | **Applied** |
| D2-4 | Accepted | Breakpoint at 1140; measured 1280 (892/892 full names), 1140/1100/1024/960/641 (325/325 numbers + current name), 7/7 items in-viewport at every width; `scrollbar-width: none` and the webkit rule are gone. | **Applied** |
| D2-5 | Accepted | All eight foundations rails sit directly after their h2 (tops 1941…8148, no overlap with any `.wide`/table); h2 gaps 48–56px — the 187–481px stranded gaps are gone. `clear: both` removed from h2; `.body > .wide` keeps `clear: both` so no rail ever overlaps a wide block (checked on foundations, case-studies, applying-it: zero overlaps). | **Applied** |
| D2-6 | Accepted | `.src .tag, td .tag, .tag-key .tag` restore padding/fill and suppress `::before`; Sources chips render as full filled chips in both themes. | **Applied** |
| D2-7 | Accepted | 0 chips before the period (`</span>.` = 0); 98 of ~103 inline chips follow `.`/`;`/`:` or a closing `.”`. **Five mid-sentence chips precede their citation** ("…eighteen years ● documented¹³,") — the enforcement regex misses `chip + sup + comma` (D3-5). | **Applied, one gap** |
| D2-8 | Accepted | `figure.scroll svg { min-width: 800px }`; Fig 5.1 wrapped (390: 13.3px). 960-viewBox figures: 9.2px at 390 — above floor. **Fig 2.1 (1040 viewBox) got no 880px inline min-width: 8.5px at 390**, below the 9px floor (D3-6). | **Partial** |
| D2-9 | Accepted | Dark `--ink-3` #8A938F = 5.73:1 on paper, 5.19:1 on paper-2 (pass). `p .tag-judg` text ink-2 (7.07:1 light / 8.74:1 dark) with the marigold glyph (3.15:1 light — non-text, ≥3:1) and underline; glyphs 11px, ○ visible in dark. | **Applied** |
| D2-10 | Accepted | 0 straight `"` and 0 straight `'` in rendered text on all seven pages; 745 curly; no `“` at word end or `”` at word start; `hanging-punctuation: first` on `.pull` and `blockquote`. | **Applied** |
| D2-11 | Accepted | `.pull`: marigold opening mark, no rule, 26ch, attribution "Target's India president, 2026¹⁶" on one line; pulls added to Case Studies (Bryar & Carr) and Foundations. Blockquote keeps the rule device — the two are now distinct. | **Applied** |
| D2-12 | Accepted | Data-URI SVG favicon (marigold square) in the template `<head>`, present on all 7 pages; no console 404s. | **Applied** |
| D2-13 | Accepted | Programmatic overflow scan of case-studies and foundations SVGs: zero texts outside their viewBox. | **Applied** |
| D2-14 | Accepted | Qualifier field exists — but entry 1 still shows both "— Tertiary" (note) and "tertiary" (derived qualifier), and both render unstyled because of the `&quot;` bug (D3-1). | **Partial — see D3-1** |
| D2-15 | Accepted | Sources h2s numbered 7.1 "Cited on the site" and 7.2 "Consulted…". | **Applied** |
| D2-16 | Deferred → done | Fig 5.2 is now `<aside class="rail">` with `.big` "2.5×" in Newsreader and two `.bars` spans, beside the Herbsleb/Lucent prose (`08-charter-fig5.2-rail-light.jpg`). The old `figure.inline-rail` markup is gone (its CSS rule is now dead — D3-9). | **Applied** |
| D2-17 | Accepted | `h2 { font-size: clamp(var(--s3), 2.2vw + 1.1rem, var(--s4)) }`; the Galbraith heading is three lines at 390 (was four). | **Applied** |
| D2-18 | Accepted | Legend line exists under the tree — **but it overflows the viewBox and is clipped** (D3-3). | **Applied, with regression** |
| D2-19 | Accepted | Key shows the inline glyph next to each chip ("● in prose", ◐, ○, ◆). | **Applied** |
| D2-20 | Accepted | `.meta` = "Section N of 7 · Sources accessed 2026-08-29" on all pages; the word count is gone. | **Applied** |
| D2-21 | Deferred → done | Fig 3.1 has "The ladder as a table" (3 rows × 3 columns, opens and reads in dark). Fig 3.2's alt is still titled "Text alternative: the four tensions" — the UI-language nit stands (D3-8). | **Applied, one nit** |
| D2-22 | Accepted in part | Fig 1.1's key is inside the SVG — **and is the D3-2 blocker** (two mono lines longer than the viewBox). Index captions ≤3 lines; five captions on pages 2–5 are still 4–6 lines (D3-7). | **Partial** |
| D2-23 | Accepted | `sup.c a { padding: 0 }`, comma margin .1em; mobile caption runs read "6, 15, 18, 35, 45" with no stray space. | **Applied** |
| D2-24 | Accepted | `figure { margin-bottom: 2rem }`, `figure + h2 { margin-top: 3rem }`; measured 48px figure→h2 on applying-it and foundations (was 77). | **Applied** |
| D2-25 | pass | Re-checked by rule: no `outline: none`; global `:focus-visible` 2px `--focus`; `aria-describedby` set/removed in site.js lines 37/47; landmarks and reduced-motion rule in place; native summaries on `details.alt`. | **Pass** |

---

## Items

### Blocking

**D3-2 · blocking — Fig 1.1's in-SVG key is clipped mid-word at every viewport.** (index.html, Fig 1.1, the two `fig-m` key lines at the bottom of the SVG.) Screenshot: visible in any index capture; measured `getBBox`: line 1 x=10→1066, line 2 x=10→1217, viewBox width 960.
Problem: the two abbreviation-key lines ("TEL telemetry ingestion · … · QOE quality of experienc") extend 106 and 257 units past the right edge of the viewBox; SVG clips them, so the second line ends mid-word with no ellipsis at 1440, 1178 and 390 alike. This is the first figure on the site, and cycle 2's D2-22 moved the key here.
Fix: split the key across three shorter lines (≈300 units each fits: fourteen abbreviations at ~80 units), or drop the long-form expansions and keep `TEL · XP-E · DQ · WH · SES · COM · FRD · XP-A · BRW · SRC · QOE` with the expansions in the alt table (they are already in the fourteen-units table below it). Regression test: the getBBox scan (every `text` inside every figure SVG must satisfy `x ≥ 0` and `x + width ≤ viewBox.width`).

**D3-3 · blocking — Fig 1.3's legend line is clipped.** (index.html, Fig 1.3, the `fig-m` legend under the tree.) Screenshot `03-index-fig1.3-dark-legend-clip.jpg` ("…sessionization fails the last questi" cut at the figure edge); measured x=40→1096 in a 960 viewBox.
Problem: the D2-18 legend grew a second clause ("; sessionization fails the last question and stays central") and now loses its tail inside the SVG's clip at every width.
Fix: two lines — line 1 `solid blue = US owns · tint = never transfers · marigold = the QoE path`, line 2 (if kept) `sessionization fails the last question and stays central` — or move the sessionization clause into the caption, which already discusses the gate. Same regression test as D3-2.

### Major

**D3-1 · major — Sources notes and qualifiers render unstyled: the build emits HTML-escaped class attributes.** (tools/build.py `entry_html`, the two f-string fragments `" <span class=&quot;who&quot;>— " + note` and `"<span class=&quot;q&quot;>" + q`; 276 `&quot;` entities in docs/sources.html.) Screenshot `04-sources-quot-entry1-zoom.png` ("Wikipedia · Wikipedia · 2026 **— Tertiary**" in ink, and a naked serif-set "tertiary" under the DOCUMENTED chip).
Problem: the browser parses `class=&quot;who&quot;` as an unquoted attribute whose value is `"who"` (with literal quote characters), which matches no CSS rule — so every note and qualifier renders at the list's base size in full ink instead of the small `--ink-2`/`--ink-3` sans treatment. Dozens of entries in both themes and at 390. Entry 1 also shows the D2-14 duplication again ("— Tertiary" + "tertiary") because the note text still contains the qualifier word.
Fix: in `entry_html`, use real quotes — `f'<span class="who">— {note}</span>'` and `f'<span class="q">{q}</span>'` (the surrounding f-string uses single quotes, so no escaping is needed). For the duplication: when `qualifier(s)` derives from the note, suppress the qualifier if its word already appears in the rendered note (or vice versa).

**D3-4 · major — Fig 1.2's "G0" tick label collides with the axis header.** (index.html, Fig 1.2 header row.) Screenshot `02-index-fig1.2-g0-collision-light.jpg` ("MONTHS AFTER GATE 0 (C**G0**ENDAR ROWS BELOW)").
Problem: measured at y≈18–20: the header "Months after Gate 0 (calendar rows below)" spans x=0–313, the "G0" tick label sits at x=163–177 — on top of the word "calendar" — and "G1 = +6" starts at x=314, one unit after the header ends. The halo makes the collision legible but it is text over text on the index's central figure.
Fix: drop the "G0" tick label (the header already says "after Gate 0" and the gate column below is labelled "Gate 0"), or shorten the header to "Months after Gate 0" and right-align it clear of the ticks; give "G1 = +6" a ≥16-unit gap.

### Minor

**D3-5 · minor — five mid-sentence chips precede their citation run.** (case-studies ×4 prose + drill-down, e.g. "Google Zurich grew into product ownership over roughly eighteen years ● documented¹³, Sky's…", "…came from ◐ inferred⁵⁹,"; screenshot `07-case-studies-dark-chip-order.jpg`.) The D2-7 order is *punctuation, citation, space, chip*; these read *chip, citation, punctuation* because build.py line 118's regex requires the punctuation to immediately follow the chip. Fix: extend it to `\s*(<span class="tag tag-[a-z]+">[^<]*</span>)(<sup class="c">.*?</sup>)?([.,;:])` → emit punctuation + sup + space + chip; regression: `grep -c '</span><sup class="c">' docs/*.html` = 0.

**D3-6 · minor — Fig 2.1 renders 8.5px labels at 390.** (case-studies, 1040-unit viewBox at the shared 800px min-width = 0.769 scale.) Screenshot `10-mobile-390-fig2.1-scroll.png`. Every other figure measures ≥9.2px; the D2-8 fix specified an inline `style="min-width: 880px"` for this one figure (→ 9.3px) and it was not applied. One attribute.

**D3-7 · minor — five captions are still 4–6 lines** (Fig 2.1 477 chars, 4.2 411, 4.3 400, 5.1 392, 3.1 342 — the D2-22 "full pass" that was queued for cycle 3 only reached the index). Cap at ~260 chars; the argument sentences ("That is why the interface…") belong in the prose.

**D3-8 · minor — Fig 3.2's alt summary still reads "Text alternative: the four tensions"** (foundations line 267) — UI language; D2-21 asked for "The four tensions, in words". The other summaries ("The ladder as a table", "Timeline as a table", "The fourteen units as a table") have the right voice.

**D3-9 · nit — dead CSS.** `figure.inline-rail` (site.css line 261) no longer matches anything now that Fig 5.2 is a rail; delete the rule.

### The "generated" test, final pass

What reads as edited now: curly quotes throughout a Newsreader setting with hanging punctuation; three pull quotes with the marigold opening mark and one-line attributions; the rail numerals (including the new 2.5× rail with its two bars); running numbers 1.1–7.2 with a numbered Sources page; the glyph-teaching tag key; "Section N of 7 · Sources accessed" instead of a word count; the favicon; chips that follow the full stop; citation runs that collapse and keep their sentence spacing; dark mode holding every figure, chip and table; and a phone experience that actually works — full nav, scroll-wrapped figures at ≥9.2px (one at 8.5), in-flow rails.

What remains, in order: (1) the two clipped SVG lines (D3-2, D3-3) — these read *broken*, which is worse than generated; (2) the unstyled "— Tertiary"/"tertiary" fragments on Sources (D3-1); (3) the G0 collision (D3-4); (4) the long captions (D3-7). None of it is templated-ness; it is finish. The one true remaining template-tell is in the data, not the design: entries like "Wikipedia · Wikipedia · 2026" repeat author as venue — the editor may want `entry_html` to drop the venue when it equals the author.

Screenshots: `reviews/screenshots/cycle-3/01-index-pull-1178-light.jpg`, `02-index-fig1.2-g0-collision-light.jpg`, `03-index-fig1.3-dark-legend-clip.jpg`, `04-sources-quot-entry1-zoom.png`, `05-applying-it-fig4.3-dark.jpg`, `06-case-studies-pull-light.jpg`, `07-case-studies-dark-chip-order.jpg`, `08-charter-fig5.2-rail-light.jpg`, `09-mobile-390-index-nav.png`, `10-mobile-390-fig2.1-scroll.png`.
