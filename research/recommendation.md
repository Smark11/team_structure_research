# Recommendation — the India site charter, and what it does to the rest of the org

**Date:** 2026-08-30. **Status:** decision memo, v2 (after review cycle 1; v1 is in git history). Citation keys refer to the C1–C5 source lists; judgment calls are marked **[judgment]**; evidence tags as in the research reports. Values that must be identical everywhere on the site are in the constants table at the end.

## Assumed baseline (correct these; §6 shows what changes if they are wrong)

The prompt gives domains, not headcounts. Every number below is illustrative until replaced. **[assumption]**

| Area | Assumed heads | Of which India contractors |
|---|---|---|
| Core data platform (ingest, orchestration, warehouse, quality, catalog) | 30 | 12 |
| Commerce (subscriptions, subscribers, paid sharing, fraud) | 25 | 8 |
| Experimentation (platform + analysis) | 15 | 4 |
| Browse | 10 | 2 |
| Search | 10 | 2 |
| Sessions & quality of experience (QoE) | 15 | 8 |
| Conversion funnels | 10 | 2 |
| Leadership, PM/TPM, analytics enablement, governance | 25 | 2 |
| **Total** | **140** | **~40** |

Also assumed: contractors sit under a single vendor master services agreement (the vendor controls who is released); there is no India site head, product owner or second-line manager today; US hours are Pacific and Eastern, giving a working-hours gap of 9.5–13.5 hours depending on coast and season (the site uses "the twelve-hour gap" as shorthand) and an overlap of zero at nominal hours, at most 2.5 hours if Eastern and India both stretch; the org has an advertising tier whose measurement data is not yet owned by this org (if it has none, §6 says what changes). The baseline was not chosen to fit the answer: §6 re-runs the decision with the contractors concentrated in commerce.

---

## 1. The recommendation in one sentence

**Charter the India site as the accountable owner of whole platform components — telemetry ingestion and the experimentation platform engine first, data-quality and contracts tooling next — and of one whole domain, quality of experience, while sessionization and the metrics catalog stay central; graduate a second domain (fraud and paid sharing, or ads measurement) on a dated, criteria-gated decision; and keep commerce, experimentation analysis, browse, search and conversion funnels anchored in the US.**

It is a hybrid that transfers ownership by whole units on written gates. It is not an extension: there is no phase in which India contributes to work the US owns. It *does* graduate, and this memo says so plainly, because the honest distinction from the "graduating extension" it rejects is the starting state — whole ownership from the first transfer — not the presence of gates. **[judgment]**

### Why this and not the alternatives — the defense

**The evidence rules out the two pure options and the pure extension.**

- *Full domain ownership of commerce or funnels* has no documented success case for a new centre. The India organizations that owned a consumer domain end-to-end — Hotstar, Google Pay — were India-first products with a local P&L [C5-33][C5-35] `[documented]`. Commerce has the most US decision-makers per change (pricing, bundling, finance, legal, trust & safety) and each of those decisions is a cross-site work item; Herbsleb and Mockus measured such items at about 2.5x the calendar time of single-site items, driven by more people per item [C3-43][C5-18] `[documented]`. Hotstar is *not* evidence that domain charters fail: its dispersal followed the rights economics — the team went where the cricket went — and shows that a self-contained site follows its market's P&L, which is true of any charter [C2-16] `[inferred, single trade source]`.
- *Pure platform ownership* is the modal centre charter and it scales — JPMorgan at ~55,000, WBD's India hub, Lowe's platform VPs [C5-27][C5-31][C5-25] `[documented]`. The claim that it *drifts* is weaker than v1 said: the documented divestitures are 2008–09 BPO/IT-support captives [C5-13], the "captives become stagnant" line is one practitioner in a trade article [C5-15], and Sky's 2025 technology cuts are a consolidation, not a failed charter [C2-38]. **[judgment]** The memo prefers to add one domain as a *hedge* against a plausible drift, not because drift is documented for technology-platform sites. That is a smaller claim than v1 made and it is the honest one.
- *A graduating extension* — India contributes to US-owned work until criteria are met — is the configuration in which ownership is diffuse by design, and diffuse ownership is the best-replicated defect predictor in the software-engineering literature: Microsoft's organizational metrics predicted failure-prone components at ~86% precision, beating churn and complexity [C3-8] `[documented]`. The market picture is a snapshot, not a rate: Zinnov's ladder puts 56% of India centres in its two execution tiers and 44% in its two ownership tiers, from a firm that sells centre set-ups [C5-1] `[documented, consultant]`. The two celebrated graduations, Target and Lowe's, took roughly two decades and ten years and had product management, data science and managers in India by the time ownership was described as theirs — the sequence is not documented [C5-22][C5-24][C5-25] `[documented, single interview and company pages]`. Nothing in a US owner's incentives pushes a hand-off later [C3-1] **[judgment]**. This memo's own gate criteria are invented too; the difference is that they are written down before the first transfer, with the measurement system named.

**The evidence supports one shape.** Of the remote sites in the case studies, those chartered as new hubs by a US parent — Netflix Warsaw, Prime Video Bengaluru, WBD India — hold capability charters [C1-6][C1-36][C2-22] `[documented; WBD's is careers-page copy]`. Google Zurich grew into product-surface ownership over about eighteen years; Sky/Osterley is the *origin* site of the Peacock platform, not a remote one; Spotify Boston kept the charter it was acquired with [C1-27][C2-28][C1-22] `[documented]`. None is a data organization; the data-org literature does not treat geography at all [C3 §8]. The distributed-work research says distance is survivable for separable work with clear ownership and shared tooling — Microsoft found no measurable quality penalty for distributed components once ownership was site-level [C3-9] — and costly for coupled work with diffuse ownership [C3-43][C3-45][C5-19] `[documented]`. Target's operating rule twenty-one years in — "ownership of outcomes resting with where the center of gravity for the capability sits" — is one executive's sentence in one interview, and it is the best description of a working hybrid the research found [C5-22] `[documented, single source]`.

**Why one domain, and which one — scored, not asserted.** A platform-only site has no customer on its own site and nothing the US cannot ship without. The research tracks did not converge on a first domain: C3 argued for defence-heavy fraud and commerce data quality; C5 named QoE and sessions *telemetry* as a capability; C1 and C2 named QoE or sessions as candidates for *graduating* domain ownership, with C2 listing fraud first. **[judgment]** The choice below is this memo's, made against three tests derived from that research (few US decision-makers per change; standardizable outputs; separability from the warehouse's reciprocal dependencies) plus a legal gate (cross-border personal data). The full scoring is on the Applying It page; the result:

| Candidate first domain | US decision-makers per change | Outputs standardize | Separable from warehouse | Cross-border data | Outcome the parent notices |
|---|---|---|---|---|---|
| **Quality of experience** (playback telemetry → QoE metrics → analytics partner to playback/client/CDN engineering) | Partial — engineering consumers (playback, client, CDN/live ops, device certification) sign off metric-definition changes, which are rare and industry-standardized; pipeline and dimension changes need nobody | Pass | Pass, *if* sessionization is excluded: QoE metrics derive from playback events, and consumers read them (sequential dependence, contractable) | Device and network identifiers; no payment instruments or household graphs — reviewable in Phase 0 | Modest: playback SLOs, release gates, partner reporting. Playback engineering *could* compute its own — the Phase 2 gate tests whether it stops |
| **Sessions / engagement** (sessionization, hours viewed, engagement metrics) | Many — finance, content, marketing, product all consume | Pass | **Fail** — the session fact is the most reciprocally-read table in a streaming warehouse | Account identifiers | Large |
| **Fraud & paid sharing** | Partial — trust & safety, finance, legal on threshold changes; fewer people than QoE's engineering consumers but decisions denominated in dollars and latency-sensitive | Pass | Partial — reads account, payment, device and session facts | Payment tokens, household graphs, EU-scoped personal data under India's DPDP Act — may be non-transferable as scoped | Largest: paid-sharing enforcement drove the 2023–25 streaming P&L turns [C2 §1.5] |
| **Ads measurement** (if the org has an ads tier) | Partial — ad sales/ops; standards are external (IAB/MRC) | Pass — outputs are contracts by construction | Partial — identity-graph coupling | Identity data | Large, and it is the data every P&L-driven reorg chases [C2-11][C2-43] |

QoE wins on separability and on legal exposure, and it is the *smallest* outcome. Fraud wins on outcome relevance and loses on legal exposure and decision latency. The memo chooses lower risk first and says so: QoE is the first domain; fraud and ads measurement are the two candidates for the month-18 decision, and which one is chosen depends on the Phase 0 legal review and on whether the org has an ads tier. If QoE is not adopted as the source of truth by month 18, the domain claim was wrong for this org and the site continues as a platform-plus-capability site (tripwire T5). **Sessionization stays central**: v1 called the domain "sessions and QoE"; that was the reviewer's strongest catch, and the session fact table is the warehouse's spine.

**Why "whole components" rather than "the platform," and where the experimentation line is drawn.** Moving the whole platform on day one would strip the US of platform architecture while the site has no senior leadership — the vacuum Zinnov documents [C5-9]. Team Topologies allows a platform to be several teams with clean interfaces [C3-13]; Amazon's correction to the two-pizza rule was that dependencies, not size, predict failure [C1-31] `[documented]`. So components move one at a time, each with one owner on one site. The experimentation platform is the hard case, because its customers (analysis, the review gate) stay in the US. The line: **India owns assignment, exposure logging and the metrics-computation engine, including the implementation of metric definitions as versioned configuration; the US owns the semantic definitions, the catalog and the review gate.** A definition change is a US-authored config change against a schema India maintains; a computation change is India's. That is X-as-a-service with a versioned contract [C3-14], which is the interaction mode designed for remote customers — not "India builds, US approves." If that contract cannot be held (T4), the fallback is to move metrics computation back and keep only assignment and exposure logging in India. **[judgment]**

**Why not fraud first (the strongest alternative).** Fraud is defence-heavy, output-standardized (chargeback rate, recovery revenue, false-positive rate), stable in definition, and coordinated by standardized outputs — Mintzberg's only configuration built to run at arm's length [C3-4][C3-42]. Its US stakeholders per change are fewer than QoE's engineering consumers. And it is the outcome a CFO notices. It loses the *first* slot on two grounds: personal data (payment instruments, household graphs, EU-scoped data processed in India) may make it non-transferable as scoped, and that is unknowable until the Phase 0 legal review; and its decisions are denominated in dollars with a 12-hour gap on every threshold change. Choosing QoE first is choosing lower risk over higher relevance; the memo does not pretend otherwise. **[judgment]**

---

## 2. The phased path

Each phase names the ownership that transfers, what must be in place first, and the observable criteria that gate the next phase — with the system that produces each number, its owner, and when it starts. A missed criterion holds the phase; it does not fail the plan. Phase 1 begins when Gate 0 passes: target month 3, no later than month 6 (T1).

| Phase | Window | India owns (whole, with on-call) | Must be in place first | Gate to the next phase (measure · system · owner · starts) |
|---|---|---|---|---|
| **0 — Foundation** | Months 0–3 (to 6 at most) | Nothing new. Ownership decisions are announced with dates; the dissolution of the US QoE team is *not* announced until month 6 (see §3). | Site head hired and started, with a global functional title (e.g., Head of Data Platform Engineering & Telemetry), reporting to the data executive; search opened before the memo is signed, via a search firm plus internal candidates, budgeted at a director-plus band [C5-3][C5-9]. Wanted-conversion list frozen in writing at month 1, before offers. Vendor release terms negotiated [C5-15]. Legal/PII review of telemetry, QoE and fraud data processed in India, owned by privacy counsel, delivered by month 3. Baseline captured: freshness/completeness contract breaches, P1 incidents and backfill hours per platform component, from existing observability and incident tooling, owned by the US platform director. Cross-site decision log switched on: a required "needed a US decision" field on every ticket, owned by the site head. Team APIs written for every team on both sites [C3-16]. Compensation at centre-market bands, 25–40% above IT-services bands at mid-senior levels [C5-11]; conversion retention grant vesting at months 18 and 30. | Site head started · ≥ 1 engineering manager *started* per Phase 1 component (2) · ≥ 60% of the *frozen* wanted list accepted · legal review delivered · baseline captured. (HRIS; offer tracker; counsel memo; observability.) |
| **1 — Two platform components** | Months 3–9 | (a) Telemetry and event ingestion with its streaming pipelines; (b) the experimentation platform engine — assignment, exposure logging, metrics computation and the versioned implementation of catalog definitions. US stops owning these, including on-call. | Each at ≥ 6 FTE in India with a named single-threaded owner [C3-23][C1-31]; runbooks and paved-road docs; identical CI/CD and tooling across sites [C3-9]. Management: until the second-line managers are in seat, the site head runs the Phase 1 teams directly with two tech leads and the ≤ 8-direct rule is suspended — stated, not hidden. | Two consecutive quarters with contract-breach incidents and P1 incidents on transferred components no worse than the baseline plus its own quarter-to-quarter variance (observability; site head reports, US platform director attests) · India on-call at 100% (pager schedule) · < 30% of India work items needing a US decision *and* no rise in contract-breach incidents (decision log) · regretted attrition of the converted cohort ≤ 25% annualized and not rising quarter over quarter (HRIS). |
| **2 — First domain + third component** | Months 9–18 | Quality of experience end to end: playback telemetry pipelines, QoE metric definitions and computation, the QoE analytics partner seat, the roadmap. Plus (c) data-quality, observability and contracts tooling — net-new by construction, staffed during Phase 1. The US QoE team is dissolved at the month-9 transfer; its people move to browse, search, funnels or commerce, or take the one US-side QoE liaison seat. Sessionization and engagement metrics stay with the US warehouse/semantic-layer team. | A staff-level QoE analytics lead in India who owns the QoE roadmap and is the named decision-maker for metric-definition changes under a decision-rights table signed by playback and client engineering, using NBCUniversal's "embedded with and equally accountable to" phrasing for the US stakeholders [C2-33]; Team API published; DQ tooling team at ≥ 6. | QoE metrics authored in India are the tables referenced by playback SLO dashboards and release gates (playback engineering director attests) · India-authored QoE roadmap accepted in the annual plan · decision-log median for India-owned changes needing US input ≤ 3 business days · quarterly duplicate-pipeline audit (metrics-catalog function) finds no shadow QoE pipelines · Phase 1 gate still holding. |
| **3 — Second-domain decision** | Months 18–30 | *Either* fraud & paid sharing (pipelines, models, fraud metrics), *or* ads measurement, *or* — if neither clears its legal and decision-rights preconditions — expansion of the platform charter into ML-platform components and the catalog. Decided at month 18 against the criteria, not sentiment; either outcome is a working site, only the undecided one is a failure. | Fraud: legal review cleared; India analytics lead; decision-rights table with trust & safety and finance; US domain liaison. Ads: same with ad sales/ops; standards contract. | India site at 45–50 FTE with ≤ 8 directs per manager [C3-20][C3-23] · Phase 2 gates holding · ≥ 2 India-based engineers promoted into staff or lead roles · named successor for the site head in seat. |
| **Steady state** | Month 30+ | Three platform components + one or two domains, reviewed annually against the tripwires. | — | Ownership moves only with a written Team-API change and a dated transfer. |

**Staffing arithmetic (assumed baseline).** Platform contractors 12 + experimentation 4 = 16; at 60% acceptance ≈ 10 converted. Phase 1 needs 12 (two components × 6) → 2–4 net-new plus two tech leads by month 9. Phase 2: QoE contractors 8 → ≈ 5 converted; the QoE team needs 6–8 and the DQ tooling team 6, both net-new-heavy → ≈ 10–12 net-new by month 18, hired during Phase 1. Total India by month 30: ~30–35 converted + 12–15 net-new = 45–50. v1's "change of ownership, not of hands" was true of Phase 1(a) and (b) only; Phase 2 is a change of hands for roughly half the people involved. **[assumption]**

**What does not move, at any phase:** experimentation *analysis*, the metrics catalog and the experiment review gate stay one central function, as at Google, Spotify, Netflix and Disney [C1-24][C1-17][C1-2][C2-12] `[documented]`; sessionization and engagement metrics stay with the warehouse team; commerce packaging, conversion funnels, browse and search stay US-anchored while pricing, bundling and content strategy are set in the US **[judgment]**.

**Measurement caveat.** The delivery measures are freshness/completeness contract breaches, P1 incidents and backfill hours — things a data org can produce today — not DORA's four metrics. The research the memo leans on says DORA's *structural* finding transfers to data work and its four metrics do not [C3 §7]. The threshold "baseline plus its own variance" replaces v1's arbitrary 30%.

---

## 3. Implications for the whole 140-person org

**What India owns first, and why.** Telemetry ingestion and the experimentation engine go first because they have the cleanest interfaces (a schema, an SLA, a versioned contract), few US decision-makers per change, and — on the assumed baseline — are where contractors already work. QoE goes second because it is the whole domain whose consumers are engineers with a decision-rights table, not the pricing committee. DQ/contracts tooling goes alongside QoE because it is net-new and needs the Phase 1 hires first.

**What the US org stops doing.** This is the part that fails in practice, so it is explicit:
- US platform engineers stop owning, gatekeeping and carrying on-call for the transferred components. They keep: sessionization and the semantic layer, warehouse modeling, governance and access, the ML platform (until Phase 3), the metrics catalog and its semantic definitions, and platform architecture as a shared standard, not a veto.
- The US QoE team is dissolved at the month-9 transfer. Its dissolution is announced at month 6, not month 0, and its members carry retention terms through month 12, because announcing a team's end nine months early is how the knowledge walks out before the transfer. **[judgment]**
- No US manager has India directs. Every India engineer reports to an India manager; every India manager reports to the site head. During Phase 1 the site head runs the teams directly with tech leads until the managers land (stated above).
- Half-ownership is banned as a category after Phase 1: no "India builds, US approves" arrangement. The one deliberate exception is the versioned metric-definition contract in the experimentation engine, which is an X-as-a-service interface, not shared ownership; T4 tests whether it holds.

**Reporting lines.** The site head is a peer of the US directors on the data executive's staff, with a global functional title and accountability for the transferred components and domains — not a country manager [C5-3][C5-9]. The whole org stays one hub-and-spoke: central reporting line and hiring bar, people aligned to verticals, the org (not the business partner) prioritizing scarce talent — the Netflix shape, at an order of magnitude smaller [C1-1]. Experimentation analysis and the metrics catalog report centrally in the US.

**Headcount and cost (assumption-dependent; finance replaces every number).** ~40 contractor seats convert to 30–35 FTE at centre-market bands, plus 12–15 net-new hires in India (site head, 3–4 managers, one QoE analytics lead, 3–4 staff engineers, engineers for the DQ team), landing at 45–50 India FTE and ~90–95 US. The US does not shrink by fiat; it stops backfilling the transferred seats.

| Line (annual unless noted) | Today (vendor) | Year 3 (site) | Basis |
|---|---|---|---|
| 40 contractor seats at a blended vendor rate | $2.4M ($60k/seat) | — | assumed blended offshore rate |
| 30–35 converted engineers, fully loaded | — | $1.7–2.0M ($55k) | centre-market bands, 25–40% over IT-services [C5-11] |
| 3–4 engineering managers, 1 analytics lead, 3–4 staff engineers | — | $1.0–1.3M | senior India bands (assumed $110–140k loaded) |
| Site head | — | $0.3–0.4M | director-plus, global title |
| Overlap-hours stipends, travel, retention grants | — | $0.4–0.5M | assumed |
| **Run-rate** | **$2.4M** | **$3.4–4.2M** | **+$1.0–1.8M/yr** |
| One-time: vendor release fees, recruiting, transition | — | $0.7–1.5M | release 0–25% of annual contract; recruiting ~20% of first-year comp |
| Offset: US seats not backfilled (5–8 at ~$220k loaded) | — | −$1.1–1.8M/yr | from the transferred components and the QoE team |

The honest CFO sentence: **this costs roughly the same as today by year three — more in India, less in the US — and buys ownership, tenure and in-region on-call in exchange for a two-year transition and $0.7–1.5M one-time.** If the US backfill offset is not taken, it costs $1–2M a year more. **[assumption; judgment]**

**Budget and rewards.** Galbraith's point is that rewards and processes decide whether a structure works [C3-1]. The India site gets its own hiring budget and a promotion cycle on the same calendar and ladder as the US; India-authored roadmaps enter the same planning process; on-call compensation is identical. Without these, the charter is a slide. **[judgment]**

---

## 4. Tripwires — what would prove this wrong, and the fallback for each

Numbered T1–T12; dated so that "not yet" has an expiry. Fallbacks are written to be executable by the org as it exists at that date — v1's "return it to the US team" fallbacks fired after that team had been dissolved.

| # | Tripwire (observable · source) | What it means | Fallback |
|---|---|---|---|
| T1 | No site head *started* by **month 6** (HRIS). | Leadership-vacuum failure mode [C5-9]. | Transfer nothing. Run as a managed extension with explicit Team APIs; revisit at month 9. An interim US leader only on a written 12-month posting with a named local successor. |
| T2 | Regretted attrition of the converted cohort > **25%** in the first 12 months, or acceptance < **50%** of the frozen wanted list (HRIS; offer tracker). | Vendor control of the transfer, or bands below centre market [C5-11][C5-15]. | Pause Phase 2. Re-band; renegotiate the release; hire net-new rather than convert. |
| T3 | Contract-breach or P1 incidents on a transferred component above baseline-plus-variance for **two consecutive quarters** (observability). | Team composition or tooling parity, not distance [C3-9]. | Quarter 3: re-pair with a US engineer in facilitating mode; check the six-person floor. Quarter 4 still failing: *narrow* — India keeps the pipelines, the US takes the contract-change decisions for two quarters (a time-boxed shared state, named as such). Transfer-back only after a US team is re-formed (a six-month hire), never as an overnight fallback. |
| T4 | > **30%** of India work items need a US decision after **month 9**, or the metric-definition contract in the experimentation engine generates cross-site work on every change (decision log). | The boundary was drawn through a coupled system [C3-43]. | Re-cut the boundary: move the decision right to India or move the work back. For experimentation: move metrics computation back to the US, keep assignment and exposure logging in India. |
| T5 | QoE metrics authored in India are not the tables referenced by playback SLOs and release gates by **month 18** (attestation). | The domain is not separable from its US engineering stakeholders, or trust was never built [C3-44]. | Narrow QoE to a capability: India keeps telemetry and QoE pipelines; metric definitions move to the central catalog; the US liaison seat becomes the QoE metrics owner. The site continues as platform-plus-capability, and this memo's "one domain" claim was wrong for this org. |
| T6 | Quarterly duplicate audit finds a second pipeline, dashboard or "checking" query over a transferred component (metrics-catalog function). | A decision-rights failure, not a capability failure [C1-31]. | Executive decision within 30 days of the audit: dissolve the duplicate or formally re-transfer the component. Either; not both. |
| T7 | A P&L-driven reorg re-homes the data org under a different executive (the Disney 2026 pattern) [C2-11]. | The environment changed. | **No structural fallback exists**; the charter is at the new executive's discretion. The mitigation is leverage: the site owns components the likely new owner depends on daily (telemetry; ads measurement if chosen in Phase 3). Team APIs and ownership tables make the hand-over legible; they do not protect it. |
| T8 | Decision-log median for India-owned changes needing US input > **3 business days** at **month 12**. | The interface is a stand-up, not a contract [C5-19][C5-20]. | Move the decision right to India for that class of change, or reclassify the work as shared and stop counting it as India-owned. |
| T9 | The sponsoring data executive leaves or is re-orged before month 18. | Momentum sags on executive turnover [C5-15]. | The charter, gates and dashboard are written into the site head's and the US directors' objectives at month 0; the incoming executive receives the memo and the gate dashboard in week one. Phases hold at the last passed gate; nothing is left half-transferred. |
| T10 | The site head leaves. | Leadership vacuum, second edition. | The named successor (a senior India manager, in seat from month 9 as a gate criterion for Phase 3) acts; no new transfers until a permanent head is in seat. |
| T11 | Hiring freeze during a phase. | The six-person floor becomes unmeetable. | Nothing below six transfers. Components already in India stay in India with a named US escalation engineer (not on-call); the phase clock pauses and the gate dates move with it. |
| T12 | The vendor invokes non-solicit terms or prices the release above budget (unverifiable in advance [C5 §2]). | The conversion premise fails. | Hire net-new for the component with the fewest contractors first (the experimentation engine); convert nobody; timeline +6 months. |

---

## 5. Steelmanned alternatives

### A. Full domain ownership — give India commerce end-to-end
**Strongest case.** Hotstar proves an India engineering org can own a streaming product at record concurrency and export its platform [C5-33]. Amazon's lesson is to move the decision-maker with the team [C1-31]. Contractors already touch commerce pipelines; commerce has the clearest P&L, so India would own an outcome the company cares about. Decisive ownership beats a decade-long graduation.
**Why it still loses.** Hotstar and Google Pay were India-first products with local P&L; there is no verified case of a *global* consumer domain handed to a new centre on day one succeeding [C5 §5]. Commerce has the densest US stakeholder set; every pricing, bundling and paid-sharing decision is a cross-site work item at ~2.5x [C3-43]. On the assumed baseline the site has no site head, no product owner and no second-line managers — the three things the documented domain owners had by the time they owned anything [C5-22][C5-25]. And fraud — the commerce sub-domain with the best case — is scored and gated in §1.

### B. Pure platform/capability ownership — India is the data platform, nothing else
**Strongest case.** The modal successful centre charter [C5-26][C2-22][C5-25]; platform work is coordinated by standardization, which distance tolerates [C3-4][C3-9]; interfaces are APIs and schemas; it is what the contractors already do; fastest to charter and easiest to defend to a CFO. The recommendation is 80% this option.
**Why the memo adds one domain anyway.** Not because drift is documented for technology-platform sites — it is not; the divestiture record is BPO-era [C5-13] and the stagnation line is one practitioner [C5-15]. Because a platform with no customer on its own site loses the platform-as-product feedback loop [C3-15], builds a junior-heavy pyramid with no path to the second-line managers the site will need [C5-6], and gives a future P&L-driven owner nothing to notice (T7). One domain is a hedge with a written test (T5); if the test fails, the site *is* option B, and that is an acceptable landing, not a failure. **[judgment]**

### C. Graduating extension — start as an extension of US teams, graduate on criteria
**Strongest case.** Lowest immediate risk; it lets the org learn who the converted people are before committing ownership; Target and Lowe's are real graduations [C5-22][C5-24]; Olson & Olson say common ground must precede remote collaboration, and an extension phase builds it [C3-44]; Galbraith's lateral-relations-first sequencing is respectable theory [C3-2].
**Why it still loses.** During the extension phase ownership is diffuse — the Nagappan defect predictor and Spotify's "responsibility without accountability" [C3-8][C1-13]; nothing in the incentive structure pushes a US owner to hand off; and the celebrated graduations took ten to twenty years. The recommendation keeps the mechanism (dated gates, written criteria — invented here, as they would be there) and changes the starting state: whole ownership from the first transfer, never contribution to US-owned work.

### D. Undifferentiated hybrid — decide per team, case by case
**Strongest case.** Target's centre-of-gravity rule is a hybrid and it worked [C5-22]; Walmart runs global platforms next to a separately owned local product company [C5-28][C5-30]; domains differ [C3-42].
**Why it still loses.** "Hybrid" is what mature sites became [C5 §5]; without naming which units on day one, per-team choice produces half-ownership because each US owner chooses "extension" for their own team [C3-8][C1-31]. The recommendation is a hybrid with the choices made and scored.

---

## 6. Sensitivity — what changes if the baseline is wrong

| Scenario | Phase 1 (two components × 6) | Phase 2 cohort | What changes |
|---|---|---|---|
| **40 contractors, concentrated in platform + QoE** (assumed) | ~10 converted, 2–4 net-new | ~5 converted + ~10 net-new | The plan as written. |
| **20 contractors, same concentration** | ~5 converted, 7 net-new | ~0 converted, all net-new | Phase 1 is a net-new site build; +6 months on every gate; the "change of ownership, not of hands" premise is gone for both phases. Start with one component, not two. |
| **60 contractors, concentrated in commerce** | ~6 converted from platform, 6 net-new; 20+ commerce contractors have no home in the plan | QoE all net-new | **Re-run the first-domain decision.** The three tests are unchanged, but the "already sits there" argument now favours fraud/paid-sharing pipelines, and the plan would re-skill or release 20+ commerce-pipeline people. Fraud-first becomes the likely answer if the legal review clears it. |
| **No ads tier** | — | — | Phase 3 is fraud or ML platform; T7's leverage argument weakens to telemetry alone. |

v1 claimed "the argument survives ±30% on any line"; it does on headcount *totals* and it does not on *concentration*. The first-domain choice is sensitive to where the contractors sit. **[judgment]**

---

## 7. What remains uncertain

- The headcount baseline is assumed; §6 shows where the plan is sensitive.
- Everything about decision-rights frameworks, budget ownership and on-call at India centres is consultant material [C5 §3]; the decision-rights tables here are judgment.
- No source treats domain-vs-capability ownership at a remote site for data teams specifically [C3 §8]; the memo extrapolates from software-engineering distance research and centre snapshots.
- The Zinnov distribution and the attrition figures come from firms with a commercial interest in centres looking good [C5-1][C5-7].
- The cost table is illustrative; finance replaces it.
- Attribution is weak everywhere; this memo rests on avoiding documented failure modes more than on copying documented successes.

---

## Constants (hold identical on every page)

| Fact | Value |
|---|---|
| India steady-state FTE | 45–50 |
| US steady state | ~90–95 |
| Netflix vs this org | "an order of magnitude larger" |
| Time-zone gap | "the twelve-hour gap"; range 9.5–13.5 h stated once (Fig 4.3) |
| Overlap window | zero at nominal hours; ≤ 2.5 h if Eastern and India both stretch; Pacific none |
| Centre pay premium over IT services | 25–40% (HRKatha/EY; the 15–40% figure in C5 is unsupported) |
| Span | ≤ 8 directs; platform teams 7–8, domain teams 5–7 |
| Zinnov ladder | 56% execution tiers (13 + 43), 44% ownership tiers (39 + 5); a snapshot, not a rate. Zinnov's own "27% reach Portfolio Hub in 5 years" may be cited once, attributed to Zinnov with the method-unpublished caveat, never as a base rate |
| Remote sites with capability charters | Warsaw, Prime Video Bengaluru, WBD India (new hubs); Zurich, Sky, Boston, Hotstar are different cases |
| Hotstar tech drain | inferred, single trade source |
| Phase 1 components | telemetry ingestion; experimentation engine (2) |
| Phase 2 | QoE domain + DQ/contracts tooling; US QoE team dissolved at month 9, announced month 6 |
| First domain | quality of experience (sessionization stays central) |
| Gates | months 3 (≤ 6), 9, 18, 30 |
| Tripwires | T1–T12 |
| Cost | run-rate +$1.0–1.8M/yr before US offset; ≈ neutral after; one-time $0.7–1.5M |
