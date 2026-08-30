# Cycle 1 — Reviewer A, red team on the recommendation

**Reviewer persona:** VP who ran a ~150-person data org and stood up an India site; has watched this memo fail before.
**Inputs read:** `research/recommendation.md`, `research/synthesis.md`, `docs/index.html`, `docs/applying-it.html` (rendered text, including the decoded scoring-matrix figure), `research/c1-*.md`, `c2-*.md`, `c3-*.md`, `c5-*.md`.
**Date:** 2026-08-30.

## Verdict

1. I would not sign this memo as written. I would sign a version that (a) admits it is a graduating extension with a three-month first graduation, (b) scores QoE honestly against playback engineering and the session fact table, and (c) has a cost line.
2. The single weakest link is the claim that sessions/QoE "passes all three tests" — it is asserted, never scored against what QoE actually is in a streaming company, and it is contradicted by the memo's own scoring of the experimentation backend.
3. The second weakest link is the headline base rate: "~27% graduate in five years" is a cross-sectional snapshot repurposed as a cohort completion rate, is internally inconsistent inside C5 itself (27% vs 44%), and appears in the two-minute version, Fig. 1.1, and two steelmen.
4. Two of the eight tripwires have fallbacks the org cannot execute, because the plan dissolves the US team that the fallback returns the work to.
5. The memo has no cost, no legal answer, no ads answer, and no plan for the site head or the sponsor leaving. In a company where (per C2) every data reorg is P&L-triggered, a memo with no dollar line does not survive contact with finance.

**Blocking items:** A1, A3, A6, A12, A16, A19. Everything else is major or minor.

---

## A1 — "Three of five tracks independently named QoE" is a misreading of the reports

**Severity:** blocking
**Claim under attack:** recommendation.md §1 "Why one domain, and why this one" — "it is the domain three of five tracks independently named [C1 §Implications][C2 §Implications][C5 §5]"; index.html "In two minutes" ("three of the five research tracks independently named") and §1.2e; applying-it.html Judgment box ("Three of the five tracks named it independently").
**The attack:** Read what the three reports actually say. C1 §Implications names QoE/sessions as "one narrowly scoped, whole domain … with its own leader **as a graduation test**" — and lists "metrics-catalog/QoE pipelines" under *platform/capability* ownership, not domain ownership. C2 §Implications says "**graduating** domain ownership in domains that are stable and measurable (fraud, paid-sharing, QoE)" — fraud listed first, QoE third, all three as graduating, none day-one. C5 §5 item 4 names "experimentation platform, QoE/sessions **telemetry** — high-volume, low-regulatory" — telemetry is a capability, and C5's own item 5 recommends "extension for the rest with a written 24-month graduation test." C3 does not mention QoE at all and argues for fraud/subscriber-state. So: zero of five tracks named QoE as a day-one, end-to-end domain; two named it as a *graduating* domain (the model the memo rejects), one as telemetry capability. The memo converts "mentioned" into "converged on," and drops the framing every report attached.
**What would satisfy me:** Replace the sentence with: "Two tracks (C1, C2) name QoE or sessions as a candidate for *graduating* domain ownership; C5 names QoE telemetry as a capability; C3 argues for fraud. The choice to move it at month 9 rather than graduate it later is this memo's judgment." Move the `[judgment]` tag to cover the whole claim, and remove "independently."

## A2 — The memo is a graduating extension and should say so

**Severity:** major
**Claim under attack:** the one-sentence recommendation ("a platform-plus-one-domain hybrid, **not a graduating extension**") and §5C "The recommendation keeps the *mechanism* (criteria, dated gates) and drops the *starting state* (no ownership)."
**The attack:** What transfers on day one? Nothing (Phase 0). What transfers at month 3? Three platform components the memo itself says the contractors already work on — "a change of ownership, not of hands." QoE moves at month 9 *if* Phase 1 gates pass; fraud at month 18 *if* Phase 2 gates pass. Each gate is a graduation criterion. The memo's stated distinction from option C is "starting state," but the starting state of option C with a three-month first gate is identical to this plan. The memo then argues against option C using C5's finding that "explicit graduation criteria are not documented anywhere I could verify" — which applies with exactly equal force to the memo's own criteria, which are also undocumented inventions. §5D compounds this: it cites C5 ("hybrid is what mature sites became, not what they were chartered as") as a reason to reject *undifferentiated* hybrid, while recommending a chartered hybrid for which C5 says there is "no base rate."
**What would satisfy me:** Rewrite the one-sentence recommendation to own it: "a graduating model with the first graduation at month 3, the criteria written now, and no phase in which India contributes without owning." Delete "not a graduating extension." In §5C, drop the "undocumented criteria" argument or apply it to yourself.

## A3 — The 27% base rate is a snapshot, not a rate, and C5 contradicts itself on it

**Severity:** blocking
**Claim under attack:** recommendation.md §1 ("~27% of India GCCs reach portfolio ownership within five years"), §5A ("a five-year graduation that 73% of sites never complete"), §5C; index.html two-minute version, Fig. 1.1 panel C ("~27% graduate in five years"), §1.2c, §1.6a, §1.6c.
**The attack:** C5 §1 derives the number from Zinnov's maturity ladder — a *population distribution* of 13% / 43% / 39% / 5% at one point in time. A distribution tells you nothing about how many sites reach a tier "within five years"; that needs a cohort followed over time, which Zinnov does not publish (and C5 does not claim to have). Worse, C5 §5's own table says "44% are Portfolio/Transformation" — so the same report gives 27% and 44% for the same thing two sections apart. The synthesis and memo picked the lower number, wrote "within five years" onto it, and then inverted it into "73% never complete." That is three unsupported transformations of one consultant number, and it is the memo's most-repeated statistic.
**What would satisfy me:** Remove every "27%," "73%," and "within five years." If you want a base-rate sentence, the defensible one is: "About 56% of India GCCs are in Zinnov's two execution tiers today; the ladder is a snapshot, not a graduation rate, and comes from a firm that sells GCC set-ups." Fix Fig. 1.1 panel C accordingly.

## A4 — Hotstar is an economics story, and the memo tags it wrong

**Severity:** major
**Claim under attack:** recommendation.md §1 ("Hotstar's tech team drained to a competitor the moment the rights economics turned [C2-16][C5-33][C5-35] `[documented]`"); index.html two-minute version (untagged, presented as fact); §1.2a ("the Hotstar coda is the risk").
**The attack:** C2-16 is tagged by C2 as "`[inferred — single trade newsletter quoting an unnamed executive]`" and C5 says the 2023 tech-layoff story is "`[folklore]` … I could not verify." The memo upgrades it to `[documented]`. Substantively, the memo uses Hotstar as evidence that *domain ownership* is fragile. It is not evidence of that. Hotstar lost its cricket rights and a chunk of its team followed the rights to the new holder; a *platform*-chartered India site inside a Disney that then exited India via the JioStar JV would have been JV'd away just the same. The memo's own tripwire 7 concedes that platform components "move with whoever owns data next." Hotstar shows that a site tied to a P&L follows the P&L — which is true of every charter. It discriminates nothing between options A and B.
**What would satisfy me:** Tag Hotstar `[inferred, single source]` everywhere it appears. Replace "the Hotstar coda is the risk, not the reward" with an honest sentence: "Hotstar's dispersal was driven by rights economics; it shows a self-contained site follows its market's P&L, not that domain charters fail." Stop using it as the lead example in the two-minute version.

## A5 — "Every remote engineering site holds a capability charter" is false on the research's own terms

**Severity:** major
**Claim under attack:** recommendation.md §1 "The evidence supports one shape. Every remote engineering site in the eight case studies holds a capability charter"; index.html two-minute version.
**The attack:** Synthesis §A.2 admits Google Zurich "grew into product-surface ownership" as YouTube's second development HQ [C1-27]. Hotstar held a domain. Sky/Osterley is not a remote site for the Peacock platform — it is the *origin* site; the platform was built there first [C2-28]. Spotify Boston is an acquisition that kept its charter. Strip those and the genuine support is Netflix Warsaw, Prime Video Bengaluru, and WBD India — and WBD's charter is careers-page copy per C2-22. Three sites, none of them a data organization, and C3 §8 says the data literature "does not treat geography" at all. "Every" should be "three of the eight, none of which is a data org."
**What would satisfy me:** Change to: "Of the remote sites in the case studies, those chartered as new hubs by a US parent (Warsaw, Prime Video Bengaluru, WBD India) hold capability charters; Zurich grew into product ownership over ~18 years; Sky and Boston were origin or acquired sites. None is a data org." Drop "every."

## A6 — QoE does not obviously pass Test 1 or Test 3, and the memo never actually scores it

**Severity:** blocking
**Claim under attack:** recommendation.md §1 ("QoE/sessions … passes all three tests … consumers are engineers and one analytics group, not the pricing committee"); applying-it.html Judgment box ("QoE/sessions is the only domain that clears all three tests: telemetry in, metrics out … its pipelines sit upstream of the warehouse"); scoring matrix row Sessions & QoE = pass/pass/pass.
**The attack:** Nothing in C1–C5 describes what QoE/sessions is inside a streaming company, so the score is pure assertion. Here is what it is. (Test 1) QoE metrics — rebuffer ratio, startup time, EBVS, bitrate — are the SLOs of playback engineering, client/device engineering, CDN and delivery ops, live-event ops, and partner/device certification. A change to the session definition or a QoE metric is a cross-site work item with *more* US engineering stakeholders per change than a fraud threshold change, which touches trust-and-safety and finance. The memo counts "US decision-makers" only in the business, not in engineering, which is where QoE's deciders are. (Test 3) The session fact is the most reciprocally-read table in a streaming warehouse: hours viewed, engagement, retention, content performance and finance's "viewing" numbers are all derived from it. "Sits upstream of the warehouse" is true of raw telemetry, not of sessionization and metrics. The memo's own matrix scores the experimentation backend T3 = *partial* while scoring sessions T3 = *pass*; sessionization is more warehouse-coupled than exposure logging, not less. The scoring was fitted to the answer. Finally, the anti-drift argument (T5) requires "an outcome the US cannot ship without." Playback engineering can and usually does compute its own QoE from client telemetry; if India's QoE metrics are late, the US ships anyway. That is exactly why Phase 2's gate is "US adopts India's metrics as source of truth" — the US has a choice, which means the US owns the outcome.
**What would satisfy me:** Score QoE on the page with the actual US stakeholders listed (playback, client, CDN/ops, live, device certification, finance viewing metrics) and the actual warehouse dependents of the session fact. If it still passes, show it. If it does not, either (a) split "telemetry and QoE pipelines" (capability, Phase 1) from "session definitions and engagement metrics" (stays central with the metrics catalog), or (b) argue fraud/paid-sharing as the first domain per A8. Change the matrix so sessions and experimentation backend are scored consistently on Test 3.

## A7 — The scoring figure disagrees with its own alt text and with the prose

**Severity:** minor
**Claim under attack:** applying-it.html Fig. 4.1 `<desc>` ("Telemetry ingestion, data quality and contracts, and the experimentation platform backend pass all three"); index.html §1.2e ("Fraud passes the first two but not cleanly the third").
**The attack:** Decoded from the SVG: experimentation backend is pass/pass/**partial**, not "all three." Fraud is **partial**/pass/partial, so the prose claim that fraud "passes the first two" contradicts the figure on Test 1. Two of eleven rows disagree with the text describing them. A reader who trusts the figure and a reader who trusts the prose reach different conclusions about whether the experimentation backend is a clean Phase 1 move.
**What would satisfy me:** Make the desc, the prose, and the circles agree. If experimentation backend is partial on T3, say why it still moves in Phase 1 (the answer is probably "metric definitions arrive as inputs" — but see A19).

## A8 — The strongest case for fraud/paid-sharing as *first* domain is never made, and it is stronger than the memo's

**Severity:** major
**Claim under attack:** recommendation.md §1 ("Fraud/paid-sharing is the second candidate … with real US stakeholders and dollar-denominated decisions — hence a dated graduation"); synthesis T1 resolution.
**The attack:** The memo's own T5 argument says the site needs an outcome the company cares about; then it disqualifies fraud *because* its outcomes are denominated in dollars. That is backwards. C3's case: fraud and paid-sharing are defense-heavy, output-standardized (chargeback rate, sharing-recovery revenue, false-positive rate), stable in definition, and coordinated by standardized outputs — Mintzberg's only configuration built to run at arm's length. C2 §1.5/T8 says paid-sharing enforcement was the largest single driver of the 2023–25 streaming P&L turns; owning its data and models is the outcome a CFO notices in a reorg. Its US stakeholders — T&S and finance — are *fewer per change* than playback engineering, and decision rights over thresholds can be written into a table. QoE, by contrast, has no P&L, no CFO constituency, and a US engineering org that can compute it themselves. The memo's real reason for QoE-first is "that is where the contractors are assumed to sit" — which is an artifact of the invented baseline (see A17). The PII objection is not unique to fraud: QoE telemetry carries IPs, device IDs and account IDs (see A21).
**What would satisfy me:** A paragraph in §1 that gives fraud its full case and defeats it on evidence rather than on "dollars." If the honest answer is "fraud is better on outcome and worse on legal/latency, and we are choosing lower risk over higher relevance," say that, and then A6's fix decides whether QoE actually clears the bar.

## A9 — "India PM for QoE" is a title without a job, and the citation does not support it

**Severity:** major
**Claim under attack:** Phase 2 precondition "India PM or product-analytics lead for QoE hired [C5-22][C5-25]"; index.html Phase 2 ("An India product or product-analytics lead is hired before the transfer, because product management in India is what every documented domain owner had").
**The attack:** C5-22 (Target) and C5-25 (Lowe's) describe product managers for *retail products* — store design, fulfillment, omnichannel — in sites of 5,000+. The memo transfers that to "a PM for an 8–10 person data team with no product surface." What does that person own? Not a roadmap the US accepts (Phase 2 gate says the US decides whether to accept it). Not metric definitions (playback engineering signs the decision-rights table). The memo's own hedge — "PM *or* product-analytics lead" — signals it does not know. The site's cure for platform-only drift is a domain with a PM; if the PM role is vestigial, the cure is vestigial.
**What would satisfy me:** Either define the role concretely (owns the QoE metrics roadmap, is the single decision-maker for metric-definition changes under the decision-rights table, owns the analytics partner relationship with playback) and size the domain to justify it, or replace it with "staff-level analytics engineer who owns the QoE roadmap" and drop the PM citation.

## A10 — Phase 1 arithmetic requires 8–10 net-new India hires in six months with no managers in seat

**Severity:** major
**Claim under attack:** Phase 1 precondition "Each component staffed at ≥ 6 FTE in India"; §3 "the transfer is a change of ownership, not of hands"; applying-it.html steady-state table (three Phase 1 teams at 6–8, 6–7, 6–7).
**The attack:** Three components at ≥ 6 = 18–22 FTE by month 9. The baseline puts 12 contractors in platform and 4 in experimentation = 16; at the Gate 0 acceptance threshold of 60%, that is ~10 converted. The gap is 8–12 net-new hires in months 3–9, in a market C5 describes at 7:1–8:1 candidate ratios with second-line managers as the binding scarcity — and Gate 0 only requires those managers to be "hired **or identified**." So Phase 1 is a change of hands for a third to half of each team, managed by managers who may not exist. "Data quality, observability and contracts tooling" is also unlikely to be where pipeline-maintenance contractors sit; that one is net-new by construction.
**What would satisfy me:** Show the Phase 1 staffing math per component (converted vs. net-new), name the hiring lead time assumed, and change Gate 0 from "hired or identified" to "hired and started" for at least one EM per Phase 1 component. Or reduce Phase 1 to two components.

## A11 — The DORA gate uses metrics the org does not have and C3 says do not fit data work

**Severity:** major
**Claim under attack:** Phase 1 gate "Two consecutive quarters with change-failure rate and incident MTTR on transferred components within 30% of pre-transfer baseline [C3-28]"; tripwire 3.
**The attack:** C3 §7, the section the memo cites, says the four DORA metrics "assume the unit of change is a service deploy," that "nobody has validated the metrics on work whose output is a decision," and that the transferable part is "the *structural* finding, not the four metrics." The memo cites the section and adopts the four metrics. Practically: does this org have a per-component change-failure rate for ingestion pipelines *today*? If not, there is no "pre-transfer baseline," and the first two quarters after transfer are the baseline — measured by the team being measured. The 30% band is arbitrary. And the gate can be held forever by a noisy baseline.
**What would satisfy me:** Name the actual measures the org can produce now (SLA breaches on freshness/completeness contracts, P1 incident count, backfill hours) and require a baseline to be captured in Phase 0 as a precondition. Cite C3 §7 honestly: "DORA's structural finding, not its four metrics." Justify 30% or replace it with "no worse than the baseline's own quarter-to-quarter variance."

## A12 — Two gates are unmeasurable or gameable as written

**Severity:** blocking
**Claim under attack:** Phase 1 gate "< 30% of India work items requiring a US decision to close"; Gate 0 "conversion offers accepted by ≥ 60% of the contractors the org actually wants"; tripwire 8 "median decision latency … ≤ 3 business days."
**The attack:** No data org tags tickets with "required a US decision." The measure exists only if someone builds it in Phase 0, and the memo does not assign that. Once it exists it is gamed in the obvious direction: India stops asking, the number drops, and the ownership problem becomes a quality problem two quarters later. The 60% acceptance gate is passed by shrinking the "wanted" list until 60% of it says yes. Decision latency with a 0–2.5 hour overlap means one round-trip is already one business day; "≤ 3 days" is two round-trips, which is fine — but it is only observable if every cross-site decision is logged, and nobody is assigned to log it.
**What would satisfy me:** For each numeric gate, add one line: *what system produces this number, who owns it, and when it starts*. Freeze the "wanted" conversion list in writing at month 1, before offers, so the denominator cannot move. Add an anti-gaming check to the 30% gate: "and no increase in contract-breach incidents on the same components."

## A13 — The attrition gate is set below the market base rate for the roles you need

**Severity:** major
**Claim under attack:** Phase 1 gate "converted-cohort attrition < 20% annualized"; tripwire 2 "> 25% in the first 12 months."
**The attack:** C5 §4 says the data/AI roles this site needs run 18–25% with 18–24-month tenures, and the synthesis repeats it as finding 7. A gate of < 20% is at or below the market; the plan will be "held" by default in a normal year, or the gate will be waived, which teaches everyone the gates are decorative. Meanwhile at 18–25% on ~30–35 converted people, expect 12–18 departures by month 30 — the entire "converted core" of the QoE team may have turned over before Phase 2's gate is judged. The plan has no backfill mechanism, no retention instrument (bands "at GCC market" is a floor, not a retention plan), and its pyramid proxy (≥ 2 promotions) can be met while half the site walks.
**What would satisfy me:** Set the gate at the market rate with a direction ("≤ 25% and not rising quarter over quarter"), add regretted-attrition as the tracked measure, and add a Phase 0 retention instrument (conversion retention grant vesting at month 18/30). State the expected turnover arithmetic in §3.

## A14 — Missing tripwires: sponsor leaves, site head leaves, hiring freeze, vendor blocks release

**Severity:** major
**Claim under attack:** §4 tripwires table (eight items).
**The attack:** The way I have actually watched this memo die: (1) the US data executive who sponsored it leaves or is re-orged (C2: every data reorg is P&L-triggered; C5-15: momentum "can quickly sag as a result of executive turnover") — no tripwire. (2) The site head leaves in year two — the plan names the leadership vacuum only as a *hiring* risk. (3) A hiring freeze mid-Phase 1 — every C2 company had one during the period covered; WBD stood up its hub *during* cuts. With a freeze at month 6, the ≥ 6 floor is unmeetable and the memo bans half-teams, so the plan halts with the US having already stopped on-call. (4) The vendor invokes non-solicit or prices the release above budget — C5 says non-solicit terms are `[unverified]` but standard; the memo mentions "vendor release terms negotiated" in Phase 0 and has no fallback if negotiation fails. (5) The US QoE team attrits *before* month 9 once its dissolution is announced at month 0 — knowledge walks out before the transfer. Ownership decisions are "announced, not executed" in Phase 0; announcing a team's dissolution nine months early is how you lose it.
**What would satisfy me:** Add tripwires 9–12 for sponsor change, site-head departure, hiring freeze, and vendor release failure, each with a fallback. For (5), either delay the announcement of the US QoE team's dissolution or add retention terms for that team through month 12.

## A15 — Tripwire 7's fallback is not a fallback

**Severity:** minor
**Claim under attack:** Tripwire 7 fallback "Charter lives in Team APIs and ownership tables, not in a reporting line; re-attach the site head to the new executive as a peer."
**The attack:** A Team API is a document. When Disney moved its data platform under ad-tech in April 2026 [C2-11], nobody consulted the ownership tables. The new executive decides whether the India site head is a peer, and a site head with a "global functional title" for telemetry and data quality is the easiest peer to demote. The fallback amounts to "hope the new owner reads the document."
**What would satisfy me:** State the real mitigation: the site must own something the *new* likely owner depends on. That is the ads/measurement argument in A22. Otherwise label this tripwire "no fallback; the charter is at the new executive's discretion."

## A16 — Tripwires 3 and 5 return work to a US team the plan has already dissolved

**Severity:** blocking
**Claim under attack:** Tripwire 5 fallback "Return QoE to a US owner"; Tripwire 3 fallback "transfer the component back and expand another"; §3 "The US QoE/sessions team ceases to exist as an owning team at month 9–12. Its engineers and analysts move to browse, search, funnels, or commerce."
**The attack:** Tripwire 5 fires at month 18. The US QoE team was dissolved at month 9–12 and its people redeployed to other domains, which by then have re-planned around them. There is no US owner to return QoE to; re-forming one is a 6–12 month hire during which the domain is orphaned — with the India team that just failed its gate still holding the pipelines. Tripwire 3 has the same defect for platform components: the US "stops owning … including on-call" at month 3; "transfer back" at quarter 3 means re-staffing on-call for a component the US has not touched in nine months. The memo's phrasing — "a platform site that works is better than a domain site that does not" — is true and irrelevant if the fallback cannot be executed. This is the failure I have seen: the fallback is invoked, the US has nobody, and the outcome is a half-owned domain nobody planned for.
**What would satisfy me:** Either keep the one US QoE liaison seat as a *team* of 2–3 through month 18 (an explicit, budgeted hedge — and be honest that this is a shadow team by another name) or change the fallback to what is actually available: "keep QoE in India, narrow it to telemetry and pipelines, and move session/metric definitions to the central metrics catalog." Same for tripwire 3: the realistic fallback is "re-pair and narrow," not "transfer back."

## A17 — The baseline was chosen to fit the conclusion, and the sensitivity claim is untested

**Severity:** major
**Claim under attack:** "the argument survives ±30% on any line"; applying-it.html Sensitivity box ("Move 8 contractors from QoE to commerce and Phase 1 gets slower, not different"); §6 first bullet.
**The attack:** The invented baseline puts 8 of 15 QoE heads (53%) as contractors — the most contractor-heavy domain in the org — and then the memo says QoE goes first partly because "it is where India contractors already sit." Set the baseline the way a subscription business more plausibly looks (commerce pipelines are the highest-maintenance in the org; contractors concentrate there) and the "already sits" argument flips to commerce while the three tests are unchanged — which means the three tests were never the deciding factor. Now run the actual sensitivity: with 20 contractors instead of 40, Phase 1's 18–22 FTE floor consumes every convertible head and Phase 2 has no cohort; the "change of ownership not of hands" premise is gone and the plan is a net-new site build on a 30-month clock. With 60 contractors concentrated in commerce, the plan re-skills 15–25 commerce-pipeline people into telemetry and data-quality tooling while commerce loses its maintenance capacity — a change of hands on *both* sites. Neither of those is "slower, not different." The ±30% claim is asserted without arithmetic.
**What would satisfy me:** A three-row sensitivity table (20 / 40 / 60 contractors; concentrated in platform+QoE vs. commerce) showing Phase 1 converted vs. net-new headcount and whether Phase 2 has a cohort. Delete "survives ±30% on any line" unless the table shows it. State plainly: "if the contractors sit in commerce, the first-domain decision should be re-run."

## A18 — The pure-platform steelman is beaten with a 2009 back-office article and one practitioner quote

**Severity:** major
**Claim under attack:** §1 and §5B "it is also the modal drift: captives … stagnate and get cut or sold [C5-13][C5-15][C2-38]"; index.html §1.2b.
**The attack:** The evidence for "platform-only drifts" is: Citi selling a BPO/IT-support captive to TCS in 2008 [C5-13] — not a data platform, not 2026; one West Monroe consultant's sentence in a CIO article [C5-15]; and Sky cutting 600 technology roles in 2025 [C2-38] — a cost consolidation that is *not* evidence the platform charter failed (the platform is being rationalized as one org, per C2 §3.1). Against that, the memo's own evidence says the platform charter works at Netflix Warsaw, Prime Video Bengaluru, WBD India, JPMorgan and Sky/Peacock. The memo's counter is "the difference is small on paper and large in year three" — a forecast with no case behind it. And the memo then makes "the site stays a platform site" the *acceptable* fallback in tripwire 5. It cannot be both the failure mode and the acceptable landing.
**What would satisfy me:** Either find a documented case of a *technology-platform* captive (not BPO) drifting to divestiture, or downgrade the drift claim to `[judgment]` and rewrite §5B's "why it still loses" as "why we prefer to add one domain: it is a hedge against drift, not a documented necessity." Reconcile with tripwire 5.

## A19 — "India computes metrics, the US defines them" is the half-ownership the memo bans

**Severity:** blocking
**Claim under attack:** Phase 1 component (c) "experimentation *platform* backend (assignment, exposure logging, metrics computation — not analysis or the review gate)"; ownership table row "metric definitions arrive as inputs from the US catalog, never authored in the backend"; §3 "Half-ownership is banned as a category: no 'India builds, US approves' arrangement survives Phase 1."
**The attack:** Every metric-definition change in the US catalog is a computation change in the India backend. That is one work item with two owners on two sites — Herbsleb's 2.5x on every metric change, and precisely the "India builds, US approves" arrangement §3 bans. The memo's own matrix scores this component *partial* on Test 3 and moves it anyway. The same split recurs for QoE: India "authors" QoE metric definitions (Phase 2) but the metrics catalog — "the source of metric definitions" — stays in the US, so QoE metrics used in experiments have two authors. And note the drift argument: the experimentation backend's *only* customers (analysis, review gate) are on the other site — the exact "platform with no customer on its own site" condition the memo says causes stagnation. The QoE-as-internal-customer cure does not reach it.
**What would satisfy me:** Draw the line inside experimentation somewhere a single owner can hold: either India owns the backend *and* the metric-definition *implementation* (the catalog's compute layer), with the US owning only the semantic definition and review — and say the interface is a schema with a versioned contract — or leave metrics computation in the US and move only assignment and exposure logging. Say which QoE metrics the catalog owns after Phase 2.

## A20 — No cost, no ROI, no CFO sentence

**Severity:** blocking
**Claim under attack:** §3 "Headcount shape at steady state" and "Budget and rewards"; absence of any cost line anywhere in the memo or site.
**The attack:** The memo concedes, in pieces: conversion at 15–40% above IT-services rates [C5-11]; 10–15 net-new senior hires including a site head; a per-head "cost step-up"; the residual 2.5x on whatever stays shared; US redeployments; vendor release fees (unquantified, possibly material); travel and overlap-hours stipends. It never adds them up and never states what the company gets for the delta — capacity? speed? risk reduction? tenure? C2's central finding is that every data reorg in this industry was triggered by a P&L question. A memo that asks for a 45–50 FTE site with no dollar figure will be answered by finance with one, and it will not be the memo's.
**What would satisfy me:** A one-table three-year cost view: vendor run-rate today vs. FTE + senior hires + release fees + one-time transition, with the year-three delta stated as a range. One paragraph on what the delta buys, in the CFO's terms. If the honest answer is "this costs more and buys resilience and ownership," write that sentence.

## A21 — PII and cross-border transfer are a one-line placeholder for what may kill Phase 3 (and touch Phase 2)

**Severity:** major
**Claim under attack:** Phase 3 precondition "regulatory/PII controls reviewed"; ownership table "PII and regulatory controls reviewed before transfer."
**The attack:** Fraud and paid-sharing data means account identifiers, payment instrument tokens, IP/geo, device fingerprints, household graphs, and for EU subscribers, GDPR-scoped personal data — processed in India under the DPDP Act 2023 and whatever the company's existing data-transfer mechanisms are. If legal's answer is "pseudonymized only" or "no model training on EU data in India," the fraud domain is not transferable as scoped and the memo should say the ML-platform alternative is the *expected* Phase 3 outcome, not the fallback. And QoE telemetry — IP, device ID, account ID, location — raises the same question at Phase 2, where the memo says nothing. A review that can end the phase is a Phase 0 item, not a Phase 3 precondition.
**What would satisfy me:** Move the legal/PII assessment to Phase 0 with a named owner; state in §2 that the Phase 3 fraud option is conditional on it; add a sentence on QoE telemetry PII at Phase 2.

## A22 — Ads and measurement data are the domain the reorgs chase, and the memo does not score it

**Severity:** major
**Claim under attack:** §3 "Ad-data plumbing, if it exists in this org, is a candidate for a later India platform component"; scoring matrix (no ads/measurement row).
**The attack:** C2's most consistent pattern is that product data platforms get pulled toward ad monetization (Disney 2026, Paramount 2026, NBCU's two data orgs, WBD's Olli). The memo's answer is a tripwire and a parenthetical. But if this org has an ads tier — most streamers do by 2026 — ad-measurement data is arguably the unit that best fits the memo's own three tests: its standards are external (IAB, MRC), its outputs are contracts by construction, its product decision-makers sit outside the data org entirely, and it is the one thing a future ad-tech owner of the data org will depend on daily. Owning it makes the site sticky to the P&L that reorgs follow; not owning it makes the site the first thing a new owner does not understand. The memo scores browse, search and funnels — which it never intended to move — and omits the one domain that changes tripwire 7's fallback from "hope" to "leverage."
**What would satisfy me:** Add an ads/measurement row to the matrix, scored honestly (it may fail Test 3 on identity-graph coupling — say so). If it passes, name it as the Phase 3 alternative alongside ML platform. If the org has no ads tier, say that in the baseline.

## A23 — The site-head timeline contains a sequence bug and no sourcing plan

**Severity:** minor
**Claim under attack:** Gate 0→1 "Site head in seat" (month 3); tripwire 1 "No site head … in seat by month 6."
**The attack:** Phase 1 transfers begin at month 3 and are gated on the site head being in seat; the tripwire allows until month 6. If the head lands at month 5, has Phase 1 started or not? Either the gate is month 6 and Phase 1 starts at 6, or the tripwire is month 3. Separately: a director-plus data-platform leader with a global title in India, at C5's 7–8:1 candidate ratios and with second-line managers as the scarcest tier, is a 4–6 month search *after* the role is approved and banded. Month 3 is the day the search closes if it opened before the memo was signed. There is no sourcing plan (search firm, internal candidate, relocation, comp) anywhere.
**What would satisfy me:** Pick one date. Add two sentences on how the head is found and what happens to the Phase 1 clock if the search runs to month 6.

## A24 — Half-ownership is "banned," but the plan runs on it from month 3 until the EMs arrive

**Severity:** major
**Claim under attack:** §3 "US managers stop having India directs. Every India engineer reports to an India manager"; Gate 0 "≥ 2 second-line managers hired **or identified**."
**The attack:** At month 3, ~10–18 converted engineers need a manager. If the EMs are "identified" but not hired, either a US manager has India directs (banned by §3) or the site head has 10–18 directs (violates the ≤ 8 ceiling the memo cites from C3-20/C3-23). The memo bans the configuration it will be in for the first six to nine months and does not say which rule bends. The applying-it page concedes "the span line does not close cleanly" at *steady state*; it is worse in Phase 1.
**What would satisfy me:** State the Phase 1 management arrangement explicitly ("the site head runs the Phase 1 teams directly with two tech leads until EMs land at month N; the ≤ 8 rule is suspended until then") or make EM hires a hard gate.

## A25 — Herbsleb's 2.5x is stretched past what the study measured

**Severity:** minor
**Claim under attack:** §3 "Remote directs across a 12-hour gap is the Herbsleb 2.5x applied to 1:1s"; §1 "applies to every one of them" (pricing decisions); index.html 1.4 "the Herbsleb penalty applied to one-to-ones."
**The attack:** Herbsleb & Mockus measured modification-request resolution time at Lucent in the late 1990s, and the mechanism was more people per item [C5-18][C3-43]. It says nothing about manager–report relationships, and nothing about executive pricing decisions. Using it as a multiplier for 1:1s is rhetoric wearing a citation. Also "12-hour gap" — the memo's own Fig. 4.3 gives 9.5 (Eastern) to 12.5 (Pacific), with the winter picture an hour worse.
**What would satisfy me:** Delete the 1:1s line or tag it `[judgment]` without the citation. Use the org's actual overlap figure consistently.

## A26 — Citation-tag drift between the memo and the reports

**Severity:** minor
**Claim under attack:** recommendation.md tagging throughout; index.html two-minute version (untagged claims).
**The attack:** Beyond Hotstar (A4): "both hired PM/DS/managers *before* ownership moved [C5-22][C5-25]" — C5-25 is Lowe's current "About" page and establishes no sequence; C5-22 is a single trade interview. "Target … 'ownership of outcomes rests with where the center of gravity sits'" is one executive's sentence in one interview, presented three times as an operating rule. The two-minute version in index.html carries no evidence tags at all on its factual claims, while the drill-downs do; the reader who stops at two minutes gets a memo with no uncertainty in it. The memo's own §6 says "attribution is weak everywhere" and then the two-minute version reads as if it were not.
**What would satisfy me:** Tag the two-minute version at the same granularity as the drill-downs. Change "hired before ownership moved" to "had product management in India by the time ownership was described as theirs; sequence not documented."

## A27 — "Shadow team" tripwire has no detection mechanism

**Severity:** minor
**Claim under attack:** Tripwire 6 "A US team re-creates capacity for a transferred component … Executive intervention within 30 days."
**The attack:** Shadow teams are not announced. The observable is duplicated pipelines, a second QoE dashboard, a US analyst "just checking" India's numbers with their own query. Thirty-day intervention assumes the executive finds out in month one; in practice it surfaces at planning when two teams request headcount for the same thing.
**What would satisfy me:** Add the detection: a quarterly catalog audit for duplicate metric definitions and pipelines over transferred components, owned by the metrics-catalog function, with the duplicate count reported alongside the gate metrics.
