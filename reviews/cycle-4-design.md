# Cycle 4 — Reviewer D (design), verification round

**Date:** 2026-08-30. Scope: render-and-verify only, per the cycle-3 dispositions. Site served from `docs/` at `http://localhost:8471/`, fresh tab, cache-busted loads. Desktop checks ran at a 1280×813 viewport (the display would not honor a 1440 resize; the layout is identical — single centered column, content max-width 1056px, no breakpoint between 1280 and 1440 — and every geometry check below is in SVG user units, which are viewport-independent). Mobile checks ran through an injected 390px iframe. Screenshots in `reviews/screenshots/cycle-4/`.

## Verification table

| Check | Item under verification | Method | Result |
|---|---|---|---|
| 1a | Fig 1.1 three-line key inside frame (D3-2) | `svg.getBBox()` vs viewBox (960×352) + screenshots, dark and light | **Pass.** Content bbox right edge −1.3 units inside, bottom −6.4 inside; worst text ("Everything else stays where its deciders sit.") ends 1.3 units short of the edge. Four-chip legend row plus all three key lines (TEL…/SES…/BRW…) fully visible in both themes. |
| 1b | Fig 1.3 two-line legend inside frame (D3-3) | `svg.getBBox()` vs viewBox (960×508) + screenshot | **Pass.** Content bbox right −47.9, bottom −10.4 inside; both legend lines ("solid blue = US owns · tint = never transfers · marigold = …" / "sessionization fails the last question and stays central") render whole. |
| 1c | Both figures at 390px via scroll wrapper | 390px iframe; wrapper metrics + screenshot | **Pass.** No page-level horizontal overflow (`docScrollW` 390 = viewport). All three index figures sit in `.wide.scroll` wrappers, `overflow-x: auto`, SVG rendered at 800px inside a 350px viewport with the "scroll →" hint; the key/legend is reachable by scrolling at full 800px scale. |
| 2 | Fig 1.2 header clear of tick row (D3-4) | Text bbox audit of every `<text>` in the SVG | **Pass.** Header ("Months after Gate 0 …") occupies y 4–16.7; the tick row (G0 / G1 = +6 / +15 / +27) starts at y 18.2 — 1.5 units clear, no intersection. The only bbox "overlaps" in the figure are the two calendar rows (Happy path y 331.2, T1 path y 346.2) whose 15.5-unit em-boxes touch by 0.5 units — em-box padding, no ink collision; visually confirmed clean. |
| 3 | sources.html notes and qualifier chips styled (D3-1 / B3-1) | DOM computed styles + screenshot | **Pass.** 217 entries; 92 note spans (second `.who`, 14px, muted `rgb(74,85,82)`, em-dash-prefixed, wrapping cleanly) and 34 qualifier chips (`.q`, 10px letter-spaced small caps under the evidence tag — "TERTIARY", "ABSTRACT ONLY"). Zero literal `&quot;` entities in rendered text. Note-dedup rule holds: 0 entries whose note re-leads with the chip's qualifier word. |
| 4 | Chip-before-citation build rule | Python scan of all seven built HTML files for `</span><sup class="c"` | **Pass.** 0 occurrences across all seven pages. |
| 5 | Fig 2.1 label size at 390 through `w880` wrapper | 390px iframe; rendered size = computed font × (svg width / viewBox width) | **Pass.** Fig 2.1 renders at 880px against a 1040-unit viewBox (scale 0.846); minimum rendered label 9.31px ("Centralization / consolidation" legend). Fig 2.2 minimum 9.17px. Both ≥ 9px. |
| 6 | Regression sweep, seven pages light + index dark | Forced `data-theme="light"` per page; per-SVG `getBBox()` containment; horizontal-overflow check; screenshots | **Pass.** All pages: horizontal overflow 0; every figure's content bbox inside its viewBox (case-studies 2 figs, foundations 2, applying-it 3, charter-evidence 1; learning-plan and sources have none). Index verified in dark (its default here): Figs 1.1–1.3 clean, nav/table/legend contrast intact. No new overlap, clipping or contrast break observed from the cycle-3 edits. |

## Regressions found

None. No D4-n items.

Notes for the record (not findings): the two calendar rows in Fig 1.2 sit at a 15-unit pitch with a 15.5-unit em-box — zero visual problem, but any future edit that enlarges that font by ≥ 1px will collide them; and desktop verification ran at 1280px for the environmental reason above.

## Screenshots

- `01-fig1.2-dark-desktop.jpg` — header/tick clearance, three-item legend
- `02-fig1.3-dark-desktop.jpg` — two-line legend inside frame
- `03-fig1.1-light-desktop.jpg` — three-line key, light theme
- `04-fig1.1-390px-scrollwrap.jpg` — 390px iframe, scroll wrapper with hint
- `05-fig2.1-light-desktop.jpg` — timeline with in-frame legend, light
- `06-sources-notes-chips-light.jpg` — entries with notes and qualifier chips

## Verdict

All six verification checks pass; the four cycle-3 dispositions under my remit (D3-1 through D3-4 and the accepted minors) hold as built, and the cycle-3 edits introduced no design regression.

**Clears the bar. Zero blocking.**
