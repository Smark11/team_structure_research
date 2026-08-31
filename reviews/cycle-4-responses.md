# Cycle 4 — responses (verification round)

**Date:** 2026-08-30. Cycle 4 verified cycle 3's fixes. Verdicts: design — zero blocking, clears the bar; red team, fact-check and editor — not zero blocking, all three converging on one root cause: the cycle-3 fixes were fully applied in the memo and on the index, Charter Evidence and Learning Plan, **but the propagation to `docs/applying-it.html` never happened**, despite the cycle-3 responses log claiming it had. That log entry was wrong, and the verification round exists precisely to catch it. Four smaller mis-applications were also found. Every item below is now applied, rebuilt, and committed; cycle 5 re-verifies.

## Root cause, for the record

In cycle 3 the author fixed the memo directly and propagated the changes to the index by hand, deferring Applying It "to an agent" — which was never launched. The responses log then recorded the whole batch as applied. Three independent verifiers caught the gap within one cycle. The corrective habit adopted: no disposition is written as "applied" until the served HTML has been grepped for the new text.

## Dispositions

| # | Reviewer | Sev | Disposition | Note |
|---|---|---|---|---|
| A4-1 / B4-2 / C4-1 | A, B, C | blocking | **Accepted, fixed** | Applying It §4.5 now prints the memo's numbers: +$1.7–3.5M vs the $2.4M MSA mix; +$0.1–1.9M vs the $4.0M boutique mix; the corrected CFO sentence; T12 ≈ $5.0–6.3M from its own lines. Zero occurrences of the stale figures site-wide. Index T9's $1.5–3M **unwind cost** was left alone, as flagged. |
| A4-2 | A | blocking | **Accepted, fixed** | Walk-through (b) carries the validity sub-line (the review gate decides validity, counted as the one hand-off); T4's clause reads "definition SLA or committed-quarter answer"; the extension sentence matches. |
| A4-3 | A | blocking | **Accepted, fixed** | §4.7's else-branch is conditional on decisioning-vs-data-transit with the legal score unknown; the fraud-first branch names the engine's on-site customer, DQ's first customers, QoE-as-capability (US QoE team not dissolved), and the in-heads acceptance reading. |
| A4-4 / C4-2 | A, C | major | **Accepted, fixed** | §4.3/§4.5: "target months 3–4 at best, modal 4–6"; "first fiscal-quarter boundary at or after G0+6"; the two critical paths; the pre-start offer limit. |
| A4-5 | A | major | **Accepted, fixed** | Learning Plan gloss states the boundary-snap ("a one-month Gate 0 slip can cost three"). |
| A4-6 | A | minor | **Accepted, fixed** | Index Gate 3 carries the Gate-2-fails carve-out (judged against the platform charter). |
| A4-7 / C4-5 | A, C | minor/major | **Accepted, fixed** | "happy path" replaced by "best case" in the memo, index prose, Fig 1.2's SVG row label and alt text, Applying It, Charter Evidence and the Learning Plan — zero residue. |
| A4-8 | A | minor | **Accepted, fixed** | Memo status line reads v3.1. |
| B4-1 | B | blocking | **Accepted, fixed** | The 7:1–8:1 clause on Charter Evidence now cites the Zinnov talent blog (C5-9) alongside the VARINDIA source; the "5 Shifts" key removed from that clause. The cycle-3 script had matched a different C5-3 occurrence — exactly the class of error the greps now guard. |
| B4-3 | B | minor | **Accepted, fixed** | The "paid-sharing enforcement drove…" phrasing softened on Applying It too; zero occurrences site-wide. |
| C4-3 | C | major | **Accepted, fixed** | Charter Evidence §5.5 states the gate's purpose and the backfill pointer once each. |
| C4-4 | C | major | **Accepted, fixed** | The duplicated inline Conway blockquote removed; the sentence appears exactly once on Foundations, in the styled pull with the elision restored. |
| C4-6 | C | minor | **Accepted, fixed** | "decided at Gate 2." |
| D4 | D | — | **Zero blocking** | Fig 1.1/1.3 inside their frames at both sizes; Fig 1.2 header clear; Sources styled; chips ordered; Fig 2.1 ≥ 9px at 390; full regression sweep clean. |

Cycle 5 verifies the fixes above; its verdicts are in `cycle-5-*.md`.
