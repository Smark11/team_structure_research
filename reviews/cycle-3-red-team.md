# Cycle 3 — Reviewer A, red team on the recommendation (v3)

**Reviewer persona:** VP who ran a ~150-person data org and stood up an India site.
**Inputs read:** `research/recommendation.md` (v3), `docs/index.html`, `docs/applying-it.html`, `docs/charter-evidence.html`, `docs/learning-plan.html` (rendered text), `reviews/cycle-2-red-team.md`, `reviews/cycle-2-responses.md` (Reviewer A section), `research/synthesis.md`.
**Date:** 2026-08-30. **Exit-criteria cycle:** same strictness as cycles 1–2.

## Verdict

1. **I would sign v3 once two blocking items are fixed, and not before.** Both are small: v2 text still standing on two site pages, and a headline cost delta that its own rebuilt table does not produce. Neither requires re-thinking anything; both violate this cycle's rules as written.
2. The plan is now internally consistent where v2 was not: the T1 path (G0 = 6) walks clean end to end — G1 = 12, announcement at 9, retention to 15, Gate 2 at 21, Gate 3 at 33, vesting at 21/33 — and the calendar can no longer strand a US team by construction. The five cycle-2 blocking items are substantively applied.
3. The remaining majors are second-order: an unhandled branch (Gate 1 fails after the G1 − 3 announcement), gameable edges on Gate 2, one decision-boundary contradiction inside the experimentation walk-throughs, a happy-path target the plan's own lead times cannot hit, and a legal blind spot in the 60-in-commerce else-branch. They are reservations I would attach to a signature, not conditions of it.
4. **Blocking items: A3-1, A3-2.** Everything else below is major or minor and non-blocking.
5. This is what a third pass should look like: the research holds, the plan holds, and what is left is copy-editing the plan against itself.

---

## Part 1 — Verification of cycle-2 dispositions

"Memo" = `research/recommendation.md` v3; "site" = the four docs pages read.

| Item | Disposition | Applied? | Note |
|---|---|---|---|
| A2-1 | Accepted (b) | **Yes** | Gate 0 = two searches with shortlists; Gate 1 = both started; player-coach period stated (G0+3 to G0+5); vocabulary defined in the memo baseline, Applying It 4.1 and glossed on Charter Evidence 5.3. Internally consistent on both calendars. |
| A2-2 | Accepted | **Yes, substantively** | Phase-relative everywhere that decides anything; two calendars on memo, Fig 1.2, ownership table, Learning Plan header. Residues: the G1 definition's ambiguity (A3-3) and "month-18 decision" happy-path shorthand in prose (index 1.1/1.2f, Applying It 4.2, Learning Plan intro) — cosmetic where glossed. |
| A2-3 | Accepted | **Yes** | T4 narrows then returns computation only to a *re-formed* US team on a six-month hire; T6 excludes re-transfer to the duplicator. Memo §4 and index 1.5 agree. |
| A2-4 | Accepted (b) | **Yes in memo/index/Applying It; stale on Learning Plan** | Decommissioning gate, three adopted changes, failure named and costed, NBCU dropped as template. But the Learning Plan milestone table still states Gate 2 as "QoE tables drive playback SLOs" — the pre-fix attestation criterion. **→ A3-1 (blocking).** |
| A2-5 | Accepted | **Yes** | Ingestion-to-landing-schema / QoE-downstream line in memo §3, index 1.2e, ownership table. |
| A2-6 | Accepted | **Yes** | Line redrawn; three walk-throughs on Applying It with hand-off counts; Gate 1 measures P1 hours-to-resolve; QoE team named as on-site customer. Attacked at the edges in A3-6/A3-7. |
| A2-7 | Accepted | **Yes** | Derivation from bill rate → margin → premium → 1.3× load; today's line as a range by mix; both directions stated. |
| A2-8 | Accepted | **Yes** | Offset is a scenario with owner (data executive) and date (G1); base case leads everywhere; "roughly the same as today" gone. |
| A2-9 | Accepted | **Yes, but the restated delta is wrong** | All missing lines added (backfill, wage inflation, both retentions, double-running tied to T12, severance, LTI). The year-3 delta was restated to +$1.5–3.0M, which the table does not produce. **→ A3-2 (blocking).** |
| A2-10 | Accepted | **Yes** | Else-branch with costs; "usually sit" deleted on both memo and site. The else-branch's legal blind spot is new: A3-9. |
| A2-11 | Accepted | **Yes** | Row 2 states the decision (platform-only 15–20; vendor-stay alternative); "robust" reworded to the honest split. |
| A2-12 | Accepted | **Yes** | T9: enforcer above the sponsor; 60-day continue/freeze/unwind; "base case is a platform site." Unwind-cost definition is sloppy (A3-12). |
| A2-13 | Accepted | **Yes** | T11: announcement withdrawn and US team re-confirmed, costed $0.1–0.2M/quarter; below-five facilitating engineer. |
| A2-14 | Accepted | **Yes** | Negotiators named from month 0; +12–18 months; runbook contingency budgeted. The $6.8M T12 total is a naive swap (A3-13). |
| A2-15 | Accepted | **Yes** | Re-decision point in Gate 0; fraud scored under bands; QoE-first justified on the assumed baseline and says so. |
| A2-16 | Accepted | **Yes, with one gap** | Fifth criterion named and in the scoring table; ads precondition stated; "leverage" gone. Sessions/engagement carries "—" on the fifth criterion rather than a score — defensible since it fails Test 3 outright, but the response claimed "applied to all four." Noted, not blocking. |
| A2-17 | Accepted | **Yes** | Phase 0 plan with owners, lead times, critical path on memo and Applying It; freeze at head + 30 or month 4. Residuals: the target-3 arithmetic and the true Gate-0 critical path (A3-4), the dead veto on the T1 path (A3-15). |
| A2-18 | Accepted | **Yes** | Facilitating window G1−3 to G1+3 as a stated exception; US QoE retention in the table; announcement tied to G1. |
| A2-19 | Accepted | **Yes** | Baseline assumption stated; Phase 2(c) is a transfer plus build-out; the US check-runners' seats in the offset scenario; first customers named. |
| A2-20 | Accepted | **Yes** | "After Gate 0" qualifier on memo §1 and the index masthead; unilateral-decisions list in §3 and the ownership-table column; Phase 1 named as execution under US standards. |
| A2-21 | Accepted | **Yes** | 27% appears on index 1.2c and Charter Evidence 5.1 only; not in 1.1. Matches the constants. |
| A2-22 | Accepted | **Yes in memo/index; contradicted on Charter Evidence** | Gates in heads (≥ 10 of 16; ≤ 2; ≤ 3), T2 fires below 10 of 16 by month 6. But Charter Evidence 5.5 still says "The Recommendation's gate is therefore … at or below 25% annualized and not rising quarter over quarter … vesting at months 18 and 30" — the v2 percentage gate and absolute months, presented as the current recommendation. **→ A3-1 (blocking).** |
| A2-23 | Accepted | **Yes** | Interim at G1, confirmed at Gate 3; consistent across T10, Gate 3, Applying It 4.6. |
| A2-24 | Accepted | **Yes** | Field owned by the US platform director in Phase 0 with a written definition, handed to the site head; gate in relative form (halved between G0+3 and G0+6 readings). |

**Verification failures:** the two page-level residues in A2-4 and A2-22 (both site-side), and A2-9's restated delta. Folded into A3-1 and A3-2, blocking under this cycle's rule.

---

## Part 2 — Attacks on v3

### A3-1 — v2 gate language still stands on two site pages

**Severity:** blocking (verification rule: accepted items must be applied on the site, substantively)
**Claim under attack:** Charter Evidence 5.5: "The Recommendation's gate is therefore at the market and directional — regretted attrition of the converted cohort at or below 25% annualized and not rising quarter over quarter — with retention grants vesting at months 18 and 30 as the instrument behind it." Learning Plan milestone table, Gate 2→3 row: "QoE tables drive playback SLOs; the decision … is made."
**The attack:** Both sentences describe the recommendation v3 no longer makes. The 25%-annualized directional gate was replaced by heads-based gates (A2-22: ≤ 2 by G1, ≤ 3 in year one) precisely because percentages on a cohort of ten are a coin flip — and Charter Evidence, the page that argues *for* heads-based measures ("expect 12–18 departures … regardless"), attributes the coin-flip gate to the Recommendation. "Vesting at months 18 and 30" is the absolute-calendar residue (v3: G1+9 and G1+21). The Learning Plan's Gate 2 row states the gate as the dashboard-reference attestation — the exact criterion A2-4 established is an afternoon's work to satisfy — with the decommissioning requirement, the thing that makes the gate a test, omitted. A reader who works from the Learning Plan's milestone table (its stated purpose) carries the gameable gate into execution.
**What would satisfy me:** Charter Evidence 5.5 restated in heads with phase-relative vesting; the Learning Plan Gate 2 row restated as "playback engineering's own QoE computation decommissioned; ≥ 3 India-authored definition changes adopted; Phase 3 decision made." Two sentences, one pass.

### A3-2 — The headline cost deltas are not the table's numbers

**Severity:** blocking (A2-9's "year-3 delta restated" was restated to a number the rebuilt table does not produce; the delta is in the constants and on every page)
**Claim under attack:** Memo §3 table total row: "**+$1.5–3.0M/yr against an MSA-offshore mix; roughly +$0.5–1.5M against a boutique mix**"; the CFO sentence; the constants ("Cost | +$1.5–3.0M/yr base case … +$0.5–1.5M with the offset"); index 1.1; Applying It 4.5.
**The attack:** Do the memo's own subtraction. Year-3 run-rate is $4.1–5.9M (the line items sum correctly to that — checked). Today against the MSA mix is $2.4M. The delta is **+$1.7M to +$3.5M**, not +$1.5–3.0M; there is no combination of the table's own line items that yields $1.5M or caps at $3.0M. The with-offset band fails the same way: (+1.7–3.5) − (1.1–1.8) spans −0.1 to +2.4, and "+$0.5–1.5M" appears nowhere in that arithmetic — it is a judgment band typeset as a derivation, in the row labeled as the table's product. v2's cost failure was direction; v3's is that the one sentence the memo was rebuilt to support — "the honest CFO sentence" — is off by $0.2–0.5M at both ends against the table above it, and the first thing a CFO does is the subtraction. The cycle-2 sign-off condition was a cost table the headline follows from; the table is right and the headline does not follow.
**What would satisfy me:** Either restate the headline as +$1.7–3.5M (and recompute the offset band as a stated scenario: e.g. "+$0.6–2.4M, typically +$1–1.5M"), or show which line items move together to justify the narrower band, in the basis column. Propagate to the constants, the CFO sentence, index 1.1 and Applying It. Thirty minutes of work.

### A3-3 — "First quarter boundary after G0 + 6" gives month 12 on the happy path, read strictly

**Severity:** major
**Claim under attack:** Memo §2 and constants: "G1 = the first quarter boundary after G0 + 6 months (two full quarters of data)"; happy path G0 = 3, G1 = 9.
**The attack:** If G0 = 3 lands on a quarter boundary, G0 + 6 = 9 is also a boundary, and the first boundary *after* 9 is 12. The happy-path calendar on every page (3/9/18/30) requires the inclusive reading ("at or after"), which the definition does not say. Whoever judges Gate 1 in month 9 of a real transition will meet someone who reads "after" strictly and gains a free quarter. Second gap: whose quarters? Calendar and fiscal quarters differ at most media companies; the definition never says, and "the annual plan" (Gate 2) is a fiscal artifact. Third, the Learning Plan's gloss — "every later date is an offset from Gate 0 … if Gate 0 slips to month 6, everything after it slips three months" — is true for the named case only: under the boundary-snap, a *one-month* G0 slip (3→4) slips G1 by three (9→12). Dates after G1 are offsets from G1, not G0. The gloss will be quoted as the rule.
**What would satisfy me:** "G1 = the first fiscal-quarter boundary at or after G0 + 6" in the memo and constants; the Learning Plan gloss corrected to "later dates are offsets from Gate 0 and Gate 1; a Gate 0 slip moves Gate 1 to the next quarter boundary — a one-month slip can cost three."

### A3-4 — Gate 0's target month 3 is unreachable by the plan's own lead times, and the stated critical path is not the critical path

**Severity:** major
**Claim under attack:** "G0 … target month 3, no later than month 6"; Phase 0 plan: site head "start expected month 3–5"; wanted list "freeze at head + 30 days or month 4, whichever is first"; Gate 0 criterion "≥ 60% of the frozen wanted list accepted"; "Critical path: site head → engineering managers → Gate 1"; vendor release "not on the critical path if started at month 0."
**The attack:** Sequence Gate 0 from the plan's own rows. The head starts month 3–5 (the plan's words). The freeze is at head + 30 or month 4 — so month 4 at the earliest under the head-review branch. Offers go out after the freeze and after bands are set (HR, 2 months) and after there is a vendor release to convert under (3–6 months from month 0). Ten acceptances follow offers by weeks. Best case on the plan's own numbers: G0 ≈ month 4–5. The "target month 3" printed beside every happy-path calendar cannot be produced by the plan below it; the real range is 4–6, i.e., the T1 path is the modal path, and every "happy path" row on the site is the plan's best week, not its expectation. Second: the stated critical path (head → EMs → Gate 1) is the critical path to *Gate 1*. The critical path to *Gate 0* runs head → freeze → offers → acceptances, with the vendor release as a gating input to offers — and the plan calls the vendor release "not on the critical path if started at month 0," which is true only if a 3–6-month negotiation finishes in 3. If it takes 5, Gate 0 waits on it, and nothing in the plan says so. Because the schedule is phase-relative, none of this breaks downstream dates — that is v3's genuine achievement — but the memo should not print a target its own table refutes.
**What would satisfy me:** Either "target month 4–5, no later than 6" with the happy path re-labeled, or a head-start expectation of month 2–3 with the search-open date moved accordingly; and a second critical-path line: "to Gate 0: site head → list freeze → vendor release terms → offers → acceptances."

### A3-5 — The dissolution is announced three months before the gate that justifies it is judged

**Severity:** major
**Claim under attack:** "The US QoE team's dissolution is announced at **G1 − 3**"; Gate 1 is judged at G1 on "two consecutive quarters"; T9: "Because announcements are phase-relative, a freeze at Gate 0 or 1 leaves no US team in notice."
**The attack:** At G1 − 3 one quarter of Phase 1 gate data exists. If quarter two goes bad — or, the modal case, if the EM searches slip and Gate 1 fails on "both engineering managers started," a criterion with no performance content — the Phase 2 transfer does not happen at G1, and the US QoE team has been in notice since G1 − 3 for a transfer with no new date. T11 handles exactly this shape *for a hiring freeze* (announcement withdrawn, team re-confirmed, retention extended and costed); T9 handles it for sponsor loss; plain Gate 1 failure — the most ordinary of the three events — has no handler. The memo also never says what a failed Gate 1 does to the clock (re-judged at the next quarter boundary? Phase 2 preconditions re-dated?). T9's sentence is true of freezes and silently overclaims for failures. This is A2-13's scenario reborn one branch over, and the fix is the same sentence.
**What would satisfy me:** One rule at Gate 1: "If Gate 1 fails, the failing criterion is named, the gate is re-judged at the next quarter boundary, and the T11 mechanism applies to the announcement — withdrawn, the US QoE team re-confirmed until a re-judged pass, retention extended at the stated cost." And T9's clause reworded to cover "a freeze or a failed gate."

### A3-6 — Two walk-throughs put the same decision on opposite sides of the experimentation line

**Severity:** major
**Claim under attack:** Applying It 4.2, walk-through (b): India "as provider, decides whether running experiments recompute in flight or from the next start, with the review gate consulted on what is salvageable." Walk-through (c): "the salvage decision is the review gate's."
**The attack:** Recompute-in-flight versus from-next-start *is* a salvageability decision: which running experiments' readouts remain valid under the old definition is the question the review gate exists to answer. Walk-through (b) gives it to India (gate consulted) — partly, one suspects, because backfill hours were charged to India's gate in v2 and v3 wants the provider in control of its own gate exposure; walk-through (c) gives the same class of decision to the gate. In practice: India schedules a from-next-start recomputation, the review gate later refuses the affected readouts, and the "one hand-off" becomes a dispute with no written owner — the diffuse-ownership defect inside the memo's own showcase. There is also a governance smell: the infrastructure provider deciding what results mean, to manage its own SLA, is the inversion of the reason analysis stays central (synthesis finding 8; every case-study company).
**What would satisfy me:** Draw the sub-line once: India decides *scheduling and mechanics* of recomputation under the SLA; the review gate decides *validity* — which experiments' readouts are accepted under which definition — and that decision is an input India's schedule must honor, counted as the one hand-off. Apply the same sentence to both walk-throughs.

### A3-7 — T4's measure has no definition, and schema extensions are both "roadmap items" and "SLA'd"

**Severity:** minor (real, not blocking)
**Claim under attack:** T4: "Hand-offs per experimentation change exceed two at the G0 + 6 reading, or the schema-change SLA is missed two months running (decision log; SLA tracker)." Memo §1: "a schema extension is India's roadmap item, prioritised with the US as customer."
**The attack:** The decision log's written field is "needed a US decision" (A2-24's fix); nothing defines a *hand-off* or names who counts one. The walk-throughs count generously — acceptance of a served request, and iteration when the served metric does not match intent, are counted as zero — so the G0+6 reading can be gamed in either direction by choosing what a "change" and a "hand-off" are. Separately, §1 makes schema extensions roadmap items (no service level) while T4 fires on "the schema-change SLA" — either extensions carry an SLA (then §1's "roadmap item, prioritised" is wrong) or they do not (then T4's second clause is unmeasurable and the highest-value changes — the ratio-metrics/CUPED class from cycle 2 — sit in an unbounded queue, which is where "customer" quietly becomes "supplicant"). This is the answer to whether the US is a customer or a queue-holder: it is a customer exactly as far as the SLA reaches, and the memo is ambiguous about how far that is.
**What would satisfy me:** A written definition of "hand-off per change" beside the decision-log definition, with the same owner; and one sentence resolving extensions: "definition requests within the schema carry SLA X; schema extensions carry a committed-quarter answer, and T4's second clause measures both."

### A3-8 — Gate 2's decommissioning can be satisfied while the shadow lives outside the audit's reach; "adopted" is undefined

**Severity:** major
**Claim under attack:** Gate 2: "playback engineering has **decommissioned** its own QoE computation … (playback engineering director attests …)"; "quarterly duplicate-pipeline audit finds no shadow QoE pipelines" (run by the metrics-catalog function); "the India-authored QoE roadmap … names at least three metric or dimension changes the US adopted."
**The attack:** The audit that backs the attestation is run by the *metrics-catalog function* over catalog-visible assets — pipelines, dashboards, checking queries in the data platform. Playback engineering's QoE computation does not have to live there: it can live client-side in the player SDK, in the engineering observability stack (Grafana over ops telemetry), or in a third-party QoE vendor subscription (Conviva/Mux-class), none of which the catalog function can see and the last of which is arguably not "its own computation" at all. The gameable move is precise: buy the vendor dashboard, decommission the in-house pipeline, attest truthfully, point the SLO dashboard at India's tables — and keep making every real playback call off the vendor screen. The gate then certifies a domain nobody consults. Second: "adopted" is undefined. Three India-authored *dimension* additions (device model, CDN POP) that the US passively consumes are "three changes adopted" by any plain reading, and the gate passes without India ever having decided anything contested. The v2 defect was a gate free to pass; the v3 gate costs something to pass, but the cost can be paid in a currency the gate does not inspect.
**What would satisfy me:** The attestation names systems: "no QoE computation in the player SDK, the observability stack, or a third-party QoE service used for playback decisions, other than as an India-owned contract" — or the memo says plainly that the gate tests warehouse-side ownership only and accepts the residual. And a definition of "adopted": at least one *metric* (not dimension) change, and each change must have altered a playback SLO threshold, a release-gate criterion, or an exec-reported number.

### A3-9 — The 60-in-commerce else-branch moves the data that legal just refused

**Severity:** major
**Claim under attack:** §6 row 3: "If counsel does **not** clear fraud: commerce-source ingestion still moves as a platform component (it carries no fraud models), scored partial/pass/pass."
**The attack:** The else-branch exists *because* counsel found fraud non-transferable as scoped — and the memo's own legal analysis says the problem is the data, not the models: "payment tokens, household graphs and, for EU subscribers, GDPR-scoped personal data" (Applying It 4.2; Charter Evidence 5.4). Raw commerce events are subscription, payment and account events; a commerce-source ingestion component in India lands exactly the data classes counsel just refused, minus the models that were never the issue. "It carries no fraud models" answers an objection nobody raised. The row's three-test score also quietly drops the legal column — the one column that created the branch. It may well be that counsel's refusal is narrower (processing and decisioning in India, not pipeline transit under pseudonymization) — but then that distinction is the entire load-bearing wall of the else-branch and it appears nowhere.
**What would satisfy me:** A fourth score in the row (legal: unknown, scoped in the same Phase 0 review — raw-event transit vs decisioning distinguished), and one sentence: "commerce-source ingestion moves only if counsel's refusal was about decisioning, not data transit; if it is about the data, the remaining contractors are released and the row's cost stands alone."

### A3-10 — The fraud-first branch silently deletes v3's own on-site-customer argument

**Severity:** minor (real, not blocking)
**Claim under attack:** §1: "The engine has one customer on its own site: the QoE team supplies QoE guardrail metrics"; Gate 0 re-decision: "Phase 2 becomes fraud and QoE becomes a capability"; Gate 0 criterion "at least 10 of the 16 platform and experimentation contractors."
**The attack:** Three loose ends in the branch the memo added at cycle 2's insistence. (1) In the fraud-first world there is no India QoE team, so the experimentation engine's on-site customer — the fact v3 introduced to answer the drift condition — does not exist; the fraud team is a plausible replacement (enforcement-threshold experiments are how paid-sharing was tuned) but nobody says so, and DQ tooling's "first customers are the India ingestion and QoE teams" also loses one of two. (2) "QoE becomes a capability" is not defined — owned by whom, is the US QoE team then never dissolved? One sentence. (3) Gate 0's "10 of 16" is hard-coded to the assumed contractor distribution; on the 60-in-commerce baseline there are not 16 platform-and-experimentation contractors, so the gate hosting the re-decision cannot be read on the baseline that triggers it. Also: if no data maps exist, counsel's fraud answer arrives at G0 + 3 (Phase 0 plan) — after the Gate 0 re-decision it feeds; the plan should say the re-decision waits or is provisional.
**What would satisfy me:** Four sentences in §6 row 3 / Gate 0: the engine's customer in the fraud-first world is the fraud data team; DQ's first customers likewise; "QoE remains a capability: telemetry and pipelines in India, definitions with the US QoE team, which is not dissolved"; the acceptance gate restated as "≥ 60% of the frozen list, in heads per the confirmed baseline"; and "if counsel's fraud answer arrives at G0 + 3, the re-decision is taken then, before any Phase 2 commitment."

### A3-11 — The fifth criterion is waived for the first domain without argument

**Severity:** minor (real, not blocking)
**Claim under attack:** §1: the fifth criterion is "named honestly because it decides the Phase 3 choice"; the scoring table: QoE "Worst of the four"; the same memo cites re-homing "every two to three years" and T7 has "no structural fallback."
**The attack:** The memo's own base rate puts a P&L-driven re-homing more likely than not inside the 30–33 months the plan needs, and the domain chosen scores worst on surviving one. The trade — legal risk now over political risk later — is visible on the page, which is to the memo's credit, but the *reason* the fifth criterion binds the Phase 3 choice and not the first is never stated. The available defense exists in the memo's own furniture (a re-homed QoE bet that dies lands on the Gate-2-fails branch: a platform site, survivable and costed) and should be said, because the alternative reading is that the criterion was scoped to wherever it would not change the answer.
**What would satisfy me:** One sentence after the scoring verdict: "The fifth criterion does not bind the first-domain choice because its downside is the costed Gate-2-failure landing — a platform site — whereas legal exposure has no such landing; it binds Phase 3 because by then the site can afford to optimize for survival."

### A3-12 — T9's "unwind cost" is defined as the money saved by unwinding

**Severity:** minor
**Claim under attack:** T9: "unwind — with the unwind cost stated (the one-time table, less what is spent)."
**The attack:** The one-time table less what is spent is the *remaining budget*, i.e., what unwinding avoids spending — not what unwinding costs. Unwinding transferred components means re-forming US ownership (the six-month re-hire T3/T4 price, per component), re-engaging or extending the vendor, and severance/retention on the India side; none is stated, and the incoming executive who asks for the unwind number will be handed a savings line.
**What would satisfy me:** "Unwind cost: re-forming US teams for the transferred components (T3/T4's six-month hiring clocks, ~$0.4–0.6M recruiting), vendor re-engagement or extension at the prevailing rate, and India severance — order $1.5–3M — against the one-time spend already sunk."

### A3-13 — T12's $6.8M is a line-swap, not the scenario's arithmetic

**Severity:** minor
**Claim under attack:** One-time total "**$1.6–4.4M** (T12 path: up to $6.8M)."
**The attack:** $6.8M = $4.4M − $1.2M (base double-running) + $3.6M (T12 double-running) — every other line held constant. But T12 is "convert nobody": the $0.4–0.6M conversion retention grants for 30–35 converted people cannot be in a total for a scenario with zero converted people, and the recruiting line is priced for 12–15 net-new hires in a scenario T12 itself prices at ~40 hires ($0.4–0.6M). Consistent T12 arithmetic: 1.0 + 0.6 (40-hire recruiting) + 0 (grants) + 0.5 + 3.6 + 0.6 ≈ up to $6.3M, plus the two engineer-quarters for runbooks that carry no dollar figure. Small, but this table was rebuilt to be derivable and its worst-case total is not.
**What would satisfy me:** A one-line T12 sub-total built from the scenario's own lines (≈ $5.0–6.3M plus runbook engineer-quarters), or drop the parenthetical.

### A3-14 — After a withdrawn domain claim, Gate 3 can never pass

**Severity:** minor
**Claim under attack:** Gate 3: "Gate 2 holding" as a criterion; "If Gate 2 fails … the site is a platform site."
**The attack:** On the Gate-2-fails branch — the branch the memo works hardest to make respectable — Gate 2 is failed forever, so Gate 3 as written can never be judged passed: the site's 45–50 FTE certification, the promotion criterion and the successor confirmation all hang off a gate that is unreachable. The platform-site landing needs its own Gate 3 (the same criteria minus "Gate 2 holding," plus "the platform-product roadmap in the annual plan"), or the annual review that withdraws the claim should be stated to re-base the remaining gates.
**What would satisfy me:** One sentence in "If Gate 2 fails": "Gate 3 is then judged without the Gate 2 criterion, against the platform charter."

### A3-15 — The site head's list veto is dead on the T1 path

**Severity:** minor
**Claim under attack:** Phase 0 plan: wanted list "reviewed by the site head within 30 days of starting; freeze at head + 30 days or month 4, whichever is first"; "The head gets a veto, not a blank page."
**The attack:** On the T1 path the head starts month 5–6; the list froze at month 4 under the "whichever is first" rule, offers are out, and some are accepted (Gate 0 needs 10 of 16). The head's "review within 30 days of starting" is a review of a frozen, partially accepted list — a briefing, not a veto. The veto exists only if the head starts by roughly month 3, which A3-4 shows is the best case, not the expectation. The memo cites Zinnov's "first three hiring decisions" and then, on its own modal path, has the US directors make them. This is a trade the memo half-owns ("the vendor negotiation needs a list") — own it fully.
**What would satisfy me:** Either "offers before the head's start are limited to the two tech-lead seats and the clearly-safe half of the list; the balance waits for the head's review," or a plain sentence: "if the head starts after month 4, the US directors chose the cohort, and the memo accepts Zinnov's warning applies."

### A3-16 — The boutique-mix "per-head saving" needs its margin assumption stated

**Severity:** minor
**Claim under attack:** Memo §3 / Applying It 4.5: "Against a boutique-heavy contractor mix billing $80–100k a seat, conversion is a per-head saving"; synthesis finding 7: "conversion at market bands is a cost step-up, not a saving."
**The attack:** The $58–77k loaded conversion cost is derived from the *$60k* bill rate. Applied to a boutique rate the same way ($80–100k × 60–70% pay-through + premium × 1.3 load), the converted cost is $78–127k and there is no saving. The saving claim holds only if boutique premiums are margin and onshore overhead rather than engineer pay — plausible, common, and unstated. It matters for more than the table: if a boutique-billed engineer is in fact paid near the bill rate, the offer at centre bands is a pay cut and the "10 of 16 accept" gate is exposed. This is also the one place v3 brushes against synthesis finding 7 without saying why the finding does not apply.
**What would satisfy me:** One clause: "assuming boutique premiums sit in vendor margin rather than engineer pay — if the released roster shows otherwise, the conversion cost and the acceptance gate both move."

---

## Summary of what would move me to sign

Fix A3-1 (two stale paragraphs) and A3-2 (make the headline deltas the table's own arithmetic) and I sign v3, with A3-3 through A3-9 attached as reservations for the next annual review of the plan rather than conditions of the signature — because the memo is now what it says it is: a well-governed platform site with local management, one honestly-priced domain bet with a test that costs something on both sides, and a calendar that can no longer strand anyone by construction. The majors are the difference between a plan that is right and a plan that cannot be quoted against itself; they are worth an afternoon before the memo goes to the CFO, whose first act will be the subtraction in A3-2.
