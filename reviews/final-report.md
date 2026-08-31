# Final report — how the recommendation evolved, and what remains uncertain

**Date:** 2026-08-30. Three full review cycles (four reviewers each: red team, fact-checker, editor, design critic) plus a verification round. This file is the narrative; the item-by-item record is in `cycle-N-*.md` and `cycle-N-responses.md`.

## The recommendation, before and after review

**v1 (pre-review).** "Platform-components-plus-one-domain hybrid": India owns three platform components and the *sessions-and-QoE* domain from day one; fraud/paid-sharing as a dated second graduation; eight tripwires. Headline statistics included "~27% of GCCs graduate within five years" and a claim the plan was "not a graduating extension."

**v2 (after cycle 1).** The red team's six blocking critiques and the fact-checker's source audit forced the largest changes of the project:
- The first domain narrowed to **quality of experience alone** — the reviewer showed the session fact table is the most reciprocally-read table in a streaming warehouse, so "sessions and QoE" failed the memo's own separability test. Sessionization stayed central.
- Phase 1 shrank from three components to two, with the staffing arithmetic shown (the third, data-quality tooling, was largely net-new and moved to Phase 2).
- The "27% graduate in five years" figure was retired as a base rate (it is a consultant's population snapshot; the number survives only as Zinnov's own attributed claim, method unpublished).
- Gates were given measurement systems and owners; DORA's four metrics were replaced by measures a data org can actually produce; tripwires grew from eight to twelve, with fallbacks rewritten so they never return work to a team the plan had already dissolved.
- A cost table, a sensitivity table (the first-domain choice is sensitive to *where* the contractors sit, not how many there are), a fraud-first steelman, an ads-measurement candidate and a Phase 0 legal review were added.

**v3 (after cycle 2).** The red team moved from the research to the plan and won again:
- The calendar became **phase-relative** (offsets from Gate 0 and Gate 1), after the reviewer showed the v2 plan could announce a US team's dissolution against the calendar while the transfer it depended on floated — re-creating the exact failure v2 claimed to fix.
- The **experimentation line moved**: v2's "India computes, the US defines" produced four hand-offs per change when walked through three realistic changes; v3 gives India the runtime *and* the metric-definition schema with a change process and SLAs, with the US analysis function as a customer that files requests.
- QoE was rescored **under the decision rights it would actually have** (India decides definitions, engineering consulted), and its test was given teeth: Gate 2 requires playback engineering to *decommission* its own QoE computation, and failure is named and costed rather than called acceptable.
- The cost table was rebuilt from the vendor rate up (derived conversion cost, backfill, wage inflation, retention, double-running, severance; the US backfill offset became a scenario with an owner and a decision date), and the CFO sentence changed from "roughly neutral" to "**not cheaper than the vendor**."
- A month-3 re-decision point was added: if counsel clears fraud and the contractors sit in commerce, fraud goes first.
- The memo stopped calling itself "not an extension" without qualification: Phase 0 *is* an extension and says so; Phase 1 is execution under US standards with the short list of what India decides unilaterally printed.

**v3.1 (after cycle 3).** Eleven blocking items across the four reviews, all mechanical: v2 sentences that had survived on pages the rebuild agents didn't re-touch, one arithmetic error (the cost headline was not the cost table's own subtraction — corrected to +$1.7–3.5M/yr), a build bug corrupting the Sources page's markup, and two clipped SVG text lines. Every non-blocking reservation was folded in as well: the fiscal-quarter definition of G1, the honest Gate-0 critical path ("target months 3–4 best case; modal 4–6"), a Gate-1 failure rule, the decommissioning attestation's named systems and a definition of "adopted," the else-branch's legal condition, the unwind cost stated as a cost rather than a savings line.

**Cycle 4** was a pure verification round against the exit criterion (zero blocking findings from all four reviewers in the same cycle); its verdicts are recorded in `cycle-4-*.md`.

## What the reviews changed that a reader should know about

1. **The strongest ideas in the final memo came from its attackers.** The decommissioning gate, the phase-relative calendar, the decision-rights scoring, the walk-throughs, the cost table's structure and the month-3 re-decision are all reviewer demands the author initially got wrong or omitted.
2. **The evidence base shrank as it hardened.** Roughly 230 source keys were collected; 217 survived verification; 200 are cited on the site; the rest are listed as consulted-but-uncited. Three quotations that no source contained were deleted; fourteen evidence tags were downgraded; two statistics were removed as unsupported and one (the 27%) demoted to an attributed claim.
3. **The voice was disciplined twice**: cycle 2 removed the memo's habit of arguing with its own drafts; cycle 3 removed the last of it from pages the agents had not re-touched.

## What remains uncertain (unchanged by any cycle, and said on the site)

- The headcount baseline and the contractor mix are assumed; the first-domain choice is sensitive to where the contractors sit and to the Phase 0 legal review.
- Everything about decision rights, budget ownership and on-call at India centres is consultant material; the memo's decision-rights tables are judgment.
- Cross-border personal data may rule out fraud as scoped, and touches QoE telemetry; only counsel can answer it.
- No source treats domain-vs-capability ownership at a remote site for *data* teams; the memo extrapolates from software-engineering distance research and centre snapshots.
- Attribution is weak everywhere: no company publishes outcome data tying structure to results. The recommendation rests on avoiding documented failure modes more than on copying documented successes.

## Standing reservations attached to the signature

From the cycle-3 red team, on record rather than resolved: the two-minute section reads at ~2:05, not 2:00; Applying It runs long because the mandated content outweighs the length target; five figure captions run four to six lines by design; the fifth criterion (re-homing robustness) binds only the Phase 3 choice, with the reason stated; and the plan's "best case" calendar is its best week, which the memo now says out loud.
