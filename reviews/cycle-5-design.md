# Cycle 5 — Reviewer D (regression check)

Verified: Fig 1.2 renders cleanly at 1440 with the new "Best case" / "T1 path" calendar rows — 49 SVG text nodes, zero bounding-box overlaps (`screenshots/cycle-5/fig-1-2-best-case-1440.jpg`).
Verified: applying-it (cost table, schedule/deliverables table) and charter-evidence (§5.5 table and prose) show no new layout break at 1440 or 1280; horizontal overflow is 0 on both, and 0 at 390 for applying-it (`screenshots/cycle-5/applying-it-390-iframe.jpg`).
Regression found: `docs/charter-evidence.html` line 133 — the §5.5 judgment paragraph ends with leftover markup from the citation edit, rendered as visible page text: `…absorbs normal churn.html”>Applying It</a> §4.5).` (stray `</a>` plus an orphaned href fragment). Text corruption on the live page, introduced by the cycle-5 fix.

**Verdict: not zero blocking** (one blocker: the broken citation markup in charter-evidence §5.5; layout is otherwise clean).
