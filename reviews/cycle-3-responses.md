# Cycle 3 — responses to all four reviewers

**Date:** 2026-08-30. Cycle 3 was the first exit-criteria cycle. Verdicts: red team — 2 blocking; fact-check — 2 blocking; editor — 5 blocking; design — 2 blocking. All eleven were mechanical (v2 remnants, one arithmetic error, one build bug, two clipped SVG lines); every one is fixed below, along with every non-blocking major and most minors. The memo is v3.1 (v3 plus the red team's reservations, folded in). Cycle 4 runs as a verification round: the exit rule requires zero blocking from all four in the same cycle.

## Reviewer A — red team

| # | Sev | Disposition | Note |
|---|---|---|---|
| A3-1 | blocking | **Accepted** | Same finding as C3-4/C3-5; both pages fixed (Charter Evidence §5.5 gate now in heads with phase-relative vesting; Learning Plan Gate 2 row states the decommissioning gate). |
| A3-2 | blocking | **Accepted** | Headline is now the table's own subtraction: +$1.7–3.5M/yr vs the $2.4M MSA mix; +$0.1–1.9M vs the $4.0M boutique mix; the offset scenario "removes $1.1–1.8M of that." CFO sentence, constants, index §1.1 and Applying It §4.5 updated. |
| A3-3 | major | **Accepted** | "First fiscal-quarter boundary **at or after** G0 + 6"; the gloss corrected ("a one-month Gate 0 slip can cost three"); "happy path" relabelled "best case." |
| A3-4 | major | **Accepted** | Target restated as months 3–4 best case, modal 4–6; a second critical-path line added (to Gate 0: head → freeze → vendor release → offers → acceptances). |
| A3-5 | major | **Accepted** | Gate 1 failure rule added (failing criterion named; re-judged at the next quarter boundary; T11 mechanism applies to the announcement); T9's sentence covers "a freeze or a failed gate." |
| A3-6 | major | **Accepted** | The sub-line drawn once and applied to both walk-throughs: India decides scheduling and mechanics; the review gate decides validity, counted as the one hand-off. |
| A3-7 | minor | **Accepted** | Hand-off defined in writing beside the decision log; definition requests carry the SLA, schema extensions a committed-quarter answer; T4 measures both. |
| A3-8 | major | **Accepted** | The attestation names systems (player SDK, observability stack, third-party QoE service); "adopted" defined (≥ 1 metric change; each altered an SLO threshold, release gate or executive-reported number). |
| A3-9 | major | **Accepted** | The else-branch is conditional on the refusal being about decisioning rather than data transit; the component's legal score is unknown until the same review scopes transit; if the refusal is about the data, the component does not move. |
| A3-10 | minor | **Accepted** | Fraud-first branch closed out: the engine's on-site customer becomes the fraud team; DQ's first customers likewise; QoE-as-capability defined (US QoE team not dissolved); the acceptance gate restated in heads per the confirmed baseline; a late counsel answer moves the re-decision to G0 + 3. |
| A3-11 | minor | **Accepted** | The sentence added: the fifth criterion does not bind the first-domain choice because its downside is the costed Gate-2-failure landing; legal exposure has no such landing. |
| A3-12 | minor | **Accepted** | Unwind cost restated as what unwinding costs (re-formed US teams, vendor re-engagement, India severance — order $1.5–3M), not the remaining budget. |
| A3-13 | minor | **Accepted** | T12 subtotal built from the scenario's own lines: ≈ $5.0–6.3M plus two engineer-quarters for runbooks. |
| A3-14 | minor | **Accepted** | "If Gate 2 fails" adds: Gate 3 is then judged without the Gate 2 criterion, against the platform charter, with the platform-product roadmap in its place. |
| A3-15 | minor | **Accepted** | If the head starts after month 4, pre-start offers are limited to the two tech-lead seats and the clearly-safe half of the list. |
| A3-16 | minor | **Accepted** | The boutique-saving claim carries its margin assumption, with the consequence for the acceptance gate stated. |

## Reviewer B — fact-check

| # | Sev | Disposition | Note |
|---|---|---|---|
| B3-1 | blocking | **Accepted** | `entry_html` rewritten with real quotes (and de-f-stringed); rebuilt; zero `&quot;` in served markup; the note and qualifier spans style correctly (92 notes, 34 qualifier chips). |
| B3-2 | blocking | **Accepted** | The 7:1–8:1 clause now cites the Zinnov talent blog (C5-9), matching the §5.5 table. |
| B3-3 | minor | **Accepted** | The Conway pull restores "(in the broad sense used here)". |
| B3-4 | minor | **Accepted** | The "four other cases" clause now carries C2-28 (Sky) and C2-15 (Hotstar). |
| B3-5 | minor | **Accepted** | The cell softened to "Largest — the outcome a CFO noticed industry-wide in 2023–25" on the index, Applying It and in the memo. |
| B3-6 | minor | **Accepted** | The stray Target citation dropped from the §4.3 decision-rights cell. |
| B3-7 | minor | **Accepted (a); accepted-as-is (b)** | (a) The build strips a note's leading qualifier word so it renders once. (b) Straight quotes in source metadata are deliberate — titles and notes are verbatim records; noted here as the rule. |

## Reviewer C — editor

| # | Sev | Disposition | Note |
|---|---|---|---|
| C3-1 | blocking | **Accepted** | Both index locations name the v3 pair (QoE facilitating-mode window; T3's time-boxed narrowing); zero "definition contract" exception mentions remain. |
| C3-2 | blocking | **Accepted** | Foundations rail carries the month-3 re-decision and all three Phase 3 candidates. |
| C3-3 | blocking | **Accepted** | Kohavi entry states the v3 line (engine including the metric-definition schema and change process). |
| C3-4 | blocking | **Accepted** | Charter Evidence §5.5 states T2 as it exists (heads; G1 + 9 / G1 + 21 vesting) with the reviewer's supplied text. |
| C3-5 | blocking | **Accepted** | Learning Plan Gate 2 row states the decommissioning-plus-three-adopted-changes gate. |
| C3-6 | major | **Accepted** | Applying It's box reads "acceptable as a site, a failure of this memo's bet, costed in §4.5." |
| C3-7 | major | **Accepted** | The duplicate inline Conway quotation removed; the styled pull opens the Conway section. |
| C3-8 | major | **Accepted** | All six cuts applied (~60 words); the section lands at ≈ 520 prose words, ≈ 2:05 — accepted as the floor while it carries every red-team-mandated element, per the reviewer's own recommendation. |
| C3-9 | minor | **Accepted** | "this memo's position, not a sourced fact" on all six pages. |
| C3-10 | minor | **Accepted** | The dissolution milestone is phase-relative with the happy-path gloss. |
| C3-11 | minor | **Accepted** | The swimlane row reads "Fraud · ads · ML expansion" (all three candidates; fits the label column). |

## Reviewer D — design critic

| # | Sev | Disposition | Note |
|---|---|---|---|
| D3-1 | major | **Accepted** | Same as B3-1; fixed and rebuilt; the tertiary/Tertiary duplication resolved by the note-dedup rule. |
| D3-2 | blocking | **Accepted** | Fig 1.1's key split into three lines, all inside the viewBox (longest ≈ 810 units); viewBox height adjusted. |
| D3-3 | blocking | **Accepted** | Fig 1.3's legend wrapped to two lines inside the viewBox. |
| D3-4 | major | **Accepted** | Fig 1.2's header moved off the tick row. |
| D3 minors | minor | **Accepted in part** | Chip-before-citation second-pass rule added to the build (0 remaining); Fig 2.1 given a `w880` min-width class; Fig 3.2's alt summary retitled "The four tensions, in words." **Accepted-as-is:** five captions at 4–6 lines (each carries content the prose does not repeat; trimming them would re-create cycle-2's caption-vs-prose duplication) and the one dead CSS rule (harmless; removed opportunistically next time the file is edited). |

## Carried to cycle 4 (verification only)

Nothing new is queued. Cycle 4 verifies that the eleven blocking fixes hold and that no regression was introduced by them; the standing accepted-as-is items are: caption lengths (D3), verbatim straight quotes in source metadata (B3-7b), Applying It's length (C2-30 disposition), and the two-minute section at ≈ 2:05 (C3-8 disposition).
