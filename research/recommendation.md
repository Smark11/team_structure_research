# Recommendation — the India site charter, and what it does to the rest of the org

**Date:** 2026-08-29. **Status:** decision memo, v1 (pre-review). Citation keys refer to the C1–C5 source lists; judgment calls are marked **[judgment]**. Evidence tags as in the research reports.

## Assumed baseline (correct these; the argument survives ±30% on any line)

The prompt gives domains, not headcounts. The memo assumes the following, and every number below should be treated as illustrative until replaced. **[assumption]**

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

Assumed: India contractors are concentrated in pipeline maintenance for platform, QoE/sessions and commerce; they sit under a vendor MSA; there is no India site head, PM, or second-line manager today; US hours are Pacific/Eastern, giving a 0–2.5 hour overlap with IST.

---

## 1. The recommendation in one sentence

**Charter the India site as the accountable owner of specific whole components of the core data platform and of one whole domain — sessions and quality of experience — from the start; write a dated, criteria-based graduation for a second domain (fraud and paid sharing); and keep commerce, experimentation analysis, browse, search and conversion funnels anchored in the US — a platform-plus-one-domain hybrid, not a graduating extension.**

### Why this and not the alternatives — the defense

**The evidence rules out the two pure options and the pure extension.**

- *Full domain ownership of commerce or funnels* has no documented success case for a new GCC. The India orgs that owned a consumer domain end-to-end were India-first products with local P&L (Hotstar, Google Pay), and Hotstar's tech team drained to a competitor the moment the rights economics turned [C2-16][C5-33][C5-35] `[documented]`. Commerce is the domain with the most US decision-makers per change (pricing, finance, legal, trust & safety) and the highest cost of decision latency; Herbsleb–Mockus's 2.5x on cross-site work items applies to every one of them [C3-43][C5-18] `[documented]`.
- *Pure platform ownership* is the modal GCC charter and it scales — JPMorgan at 55k, WBD's India hub [C5-26][C2-22] — but it is also the modal drift: captives "become stagnant with marginal improvements" when no product outcome depends on them, and support-only charters were what got divested in 2008–09 and cut at Sky in 2025 [C5-13][C5-15][C2-38] `[documented]`.
- *A graduating extension* is the documented stagnation path: ~27% of India GCCs reach portfolio ownership within five years, per the firm that sells GCC set-ups [C5-1]; the two celebrated graduations (Target, Lowe's) took 10–15 years and hired PM, data science and managers *before* ownership moved [C5-22][C5-25] `[documented]`. During the extension phase ownership is diffuse by definition, and diffuse ownership is the best-replicated predictor of defects in the literature [C3-8] `[documented]`. Nothing in a US owner's incentives pushes a hand-off later [C3-1] **[judgment]**.

**The evidence supports one shape.** Every remote engineering site in the eight case studies holds a capability charter (Netflix Warsaw, Prime Video Bengaluru, WBD India, Sky/Peacock UK, Spotify Boston) [C1-6][C1-36][C2-22][C2-29][C1-22] `[documented]`; the distributed-work research says distance is survivable for *separable* work with *clear ownership* and shared tooling, and fatal for coupled work with diffuse ownership [C3-9][C3-45][C5-19] `[documented]`; and Target's operating rule — "ownership of outcomes rests with where the center of gravity for the capability sits" — is what a hybrid looks like when it works [C5-22] `[documented]`.

**Why one domain, and why this one.** A platform-only site has no customer of its own and no outcome the US cannot ship without; that is tension T5 in the synthesis. QoE/sessions is the domain that passes all three tests the research tracks converge on — few US decision-makers per change, standardizable outputs (telemetry in, metrics out), and separability from the warehouse's reciprocal dependencies — and it is the domain three of five tracks independently named [C1 §Implications][C2 §Implications][C5 §5] **[judgment]**. It is also, by assumption, where India contractors already sit. Fraud/paid-sharing is the second candidate: defense-heavy, output-standardizable [C3-42], but with real US stakeholders and dollar-denominated decisions — hence a dated graduation with criteria, not a day-one transfer.

**Why "whole components" of the platform rather than "the platform."** Moving the entire core platform to India on day one would strip the US of platform architecture while the site has no senior leadership — the leadership-vacuum failure mode [C5-9]. Team Topologies allows a platform to be several teams with clean interfaces [C3-13]; each component gets one owner, on one site. **[judgment]**

---

## 2. The phased path

Each phase names the ownership transfer, the hires that must precede it, and the graduation criteria that gate the next phase. Criteria are observable and dated; a missed criterion holds the phase, it does not fail the plan.

<!-- phase table -->
| Phase | Window | India owns (whole, with on-call) | Must be in place before the transfer | Graduation criteria to next phase |
|---|---|---|---|---|
| **0 — Foundation** | Months 0–3 | Nothing new. Ownership decisions are *announced*, not executed. | Site head hired with a **global functional title** (e.g., Head of Data Platform Engineering & Telemetry), reporting to the data executive directly. Vendor release terms negotiated. Team APIs written for every team on both sites [C3-16]. Compensation bands set at GCC market, not vendor-plus [C5-11]. | Site head in seat; ≥ 2 second-line managers hired or identified; conversion offers accepted by ≥ 60% of the contractors the org actually wants (not the ones the vendor offers) [C5-15]. |
| **1 — Platform components** | Months 3–9 | Three whole platform components: (a) telemetry/event ingestion and streaming pipelines, (b) data quality, observability and contracts tooling, (c) experimentation *platform* backend (assignment, exposure logging, metrics computation — not analysis or the review gate). US stops owning these, including on-call. | Each component staffed at ≥ 6 FTE in India [C3-23]; a named India single-threaded owner per component [C1-31]; runbooks and paved-road docs; shared CI/CD and tooling identical across sites [C3-9]. | Two consecutive quarters with change-failure rate and incident MTTR on transferred components within 30% of pre-transfer baseline [C3-28]; India on-call at 100% for those components; < 30% of India work items requiring a US decision to close; converted-cohort attrition < 20% annualized. |
| **2 — First domain** | Months 9–18 | Sessions & QoE end-to-end: pipelines, metric definitions, models, the analytics partner seat, and the roadmap. The US QoE/sessions team is dissolved into this; its people redeploy to browse/search/funnels or become the US-side liaison. | India PM or product-analytics lead for QoE hired [C5-22][C5-25]; decision-rights table (who decides metric changes, who is consulted) signed by US playback/client engineering; Team API published. | QoE metrics authored in India adopted as source-of-truth by US client/playback engineering; India-authored roadmap accepted in the annual planning cycle; median decision latency for India-owned changes needing US input ≤ 3 business days; no US shadow team for QoE work. |
| **3 — Second-domain decision** | Months 18–30 | *Either* fraud & paid-sharing data domain (pipelines, models, fraud metrics) *or*, if criteria unmet, expansion of platform charter (ML platform components, catalog). Decided at month 18 against criteria, not sentiment. | Fraud: India PM + US trust-and-safety/finance stakeholders agree a decision-rights table; a US-based domain liaison; regulatory/PII controls reviewed. | India site at 45–55 FTE with ≤ 8 directs per manager [C3-20][C3-23]; Phase 2 criteria still holding; ≥ 2 India-based engineers promoted into staff/lead roles (a proxy for a working pyramid). |
| **Steady state** | Month 30+ | Platform components + 1–2 domains, reviewed annually against the tripwires. | — | Charter reviewed annually; ownership moves only with a written Team-API change and a dated transfer. |

**What does not move, at any phase:** experimentation *analysis*, the metrics catalog and the experiment review gate stay one central function in the US, as at Google, Spotify, Netflix and Disney [C1-24][C1-17][C1-2][C2-12] `[documented]`; commerce packaging, conversion funnels, browse and search stay US-anchored while pricing, bundling and content strategy are set in the US **[judgment]**.

---

## 3. Implications for the whole 140-person org

**What India owns first, and why.** Telemetry ingestion, data quality/contracts tooling and the experimentation platform backend go first because they are the platform components with the cleanest interfaces (a schema, an SLA, an API) and the fewest US decision-makers per change; they are also where contractors already work, so the transfer is a change of ownership, not of hands **[judgment, assumption]**. QoE/sessions goes second because it is the whole domain whose consumers are engineers and one analytics group, not the pricing committee.

**What the US org stops doing.** This is the part that fails in practice, so it is explicit:
- US platform engineers stop owning, reviewing-as-gatekeepers, and being on-call for the three transferred components. They keep: warehouse modeling and the semantic layer, governance and access, the ML platform (until Phase 3), and platform architecture *as a shared standard*, not as a veto.
- The US QoE/sessions team ceases to exist as an owning team at month 9–12. Its engineers and analysts move to browse, search, funnels, or commerce, or take the one US-side QoE liaison seat.
- US managers stop having India directs. Every India engineer reports to an India manager; every India manager reports to the site head [C3-20][C3-24] **[judgment]**. Remote directs across a 12-hour gap is the Herbsleb 2.5x applied to 1:1s.
- Half-ownership is banned as a category: no "India builds, US approves" arrangement survives Phase 1. If a component cannot be owned whole on one site, it is not transferred [C3-8][C1-31].

**Reporting lines.** The site head is a peer of the US directors on the data executive's staff, with a global functional title and P&L-style accountability for the transferred components and domains — not a country manager [C5-3][C5-9]. Domain teams remain in one hub-and-spoke org: central reporting line and hiring bar, people aligned to verticals, the org (not the business partner) prioritizing scarce talent — the Netflix shape [C1-1]. Experimentation analysis and the metrics catalog report centrally in the US. Ad-data plumbing, if it exists in this org, is a candidate for a later India platform component precisely because the case studies show it is the layer that gets pulled toward monetization in every P&L-driven reorg [C2-11][C2-43] **[judgment]**.

**Headcount shape at steady state (assumption-dependent).** ~40 contractor seats convert to ~30–35 FTE at market bands (expect the vendor to withhold some of the best people and expect a per-head cost step-up [C5-11][C5-15]), plus 10–15 net-new senior hires in India (site head, 3–4 EMs, 1–2 PMs, 3–4 staff engineers), landing at 45–50 India FTE and ~90–95 US. The US does not shrink by fiat; it stops backfilling the transferred seats.

**Budget and rewards.** Galbraith's point is that rewards and processes decide whether a structure works [C3-1]. The India site gets its own hiring budget and promotion cycle on the same calendar and ladder as the US; India-authored roadmaps enter the same planning process; on-call compensation is identical. Without these, the charter is a slide **[judgment]**.

---

## 4. Tripwires — what would prove this wrong, and the fallback for each

| # | Tripwire (observable) | What it means | Fallback |
|---|---|---|---|
| 1 | No site head with a global functional title in seat by **month 6**. | The leadership-vacuum failure mode [C5-9]; the plan cannot proceed to Phase 1 safely. | Transfer nothing. Run as a managed extension with explicit Team APIs; revisit at month 9; consider an interim US leader on a 12-month posting only if they will hand over to a local hire on a written date. |
| 2 | Converted-cohort attrition > **25%** in the first 12 months, or offer acceptance < 50% of the people the org wanted. | Vendor control of the transfer, or bands set below GCC market [C5-11][C5-15]. | Pause Phase 2. Re-band; renegotiate vendor release; hire net-new rather than convert. |
| 3 | Change-failure rate or MTTR on a transferred component worse than baseline by > 30% for **two consecutive quarters**. | Team composition or tooling parity failed, not distance per se [C3-9]. | Re-pair with a US engineer in *facilitating* mode for one quarter; check the Larson floor (≥ 6); if still failing at quarter 3, transfer the component back and expand another. |
| 4 | > 30% of India work items require a US decision to close after **month 9** (the extension trap). | The boundary was drawn through a coupled system; ownership is diffuse in practice [C3-43]. | Re-cut the component boundary; move the decision right to India or move the work back. Do not keep the label "owner" on a team that cannot close its own tickets. |
| 5 | QoE metrics authored in India are not adopted as source-of-truth by US engineering by **month 18**. | The domain is not separable from US stakeholders, or trust was not built [C3-44]. | Return QoE to a US owner; expand India's platform charter (ML platform, catalog) instead; the site stays a platform site and the memo's "one domain" claim was wrong for this org. |
| 6 | A US team re-creates capacity for a transferred component ("we can't wait for India"). | A decision-rights failure, not a capability failure [C1-31]. | Executive intervention within 30 days: dissolve the shadow team or formally re-transfer the component. Either is acceptable; both at once is the failure. |
| 7 | A P&L-driven reorg re-homes the data org under a different executive (the Disney 2026 pattern) [C2-11]. | The environment changed; the charter must be portable. | Charter lives in Team APIs and ownership tables, not in a reporting line; re-attach the site head to the new executive as a peer. If the new owner wants platform under ad-tech, the India components move with it — they are the most portable part of the org. |
| 8 | Median decision latency on India-owned changes needing US input > **3 business days** at month 12. | The time-zone interface is a stand-up, not a contract [C5-19][C5-20]. | Move the decision right to India for that class of change, or reclassify the work as shared and stop counting it as India-owned. |

---

## 5. Steelmanned alternatives

### A. Full domain ownership — give India commerce end-to-end
**Strongest case.** Hotstar proves an India engineering org can own a streaming product at record concurrency and export its platform to other markets [C5-33]. Amazon's lesson is to move the *decision-maker* with the team, not the analysts, and to treat dependencies as defects [C1-31]; a whole domain with an STL on site is exactly that. Contractors already touch commerce pipelines; commerce is the domain with the clearest P&L, so India would have an outcome the company cares about. Decisive ownership beats a five-year graduation that 73% of sites never complete [C5-1].
**Why it still loses.** Hotstar and Google Pay were India-first products with local P&L; there is no verified case of a *global* consumer domain handed to a new GCC on day one succeeding [C5 §5]. Commerce has the densest US stakeholder set and the most latency-sensitive decisions; every pricing, bundling and paid-sharing decision is a cross-site work item at 2.5x [C3-43]. The site has no PM, no second-line managers and no site head today — the three things the successful domain owners hired first [C5-22][C5-25]. And the Hotstar coda is the risk, not the reward: a self-contained India org is easy to lose whole [C2-16].

### B. Pure platform/capability ownership — India is the data platform, nothing else
**Strongest case.** It is the modal successful GCC charter (JPMorgan, WBD India, Lowe's platform VPs) [C5-26][C2-22][C5-25]; platform work is coordinated by standardization, which distance tolerates [C3-4][C3-9]; interfaces are APIs and schemas, not product debates; it is what the contractors already do; it is fastest to charter and easiest to defend to a CFO.
**Why it still loses as the whole charter.** It is also the modal drift: captives with no product outcome depending on them stagnate and get cut or sold [C5-13][C5-15][C2-38]. A platform with no internal customer on its own site loses the "platform as product" feedback loop [C3-15]. It builds a junior-heavy pyramid with no path to the second-line managers the site will need [C5-6]. The recommendation *is* mostly this option — with one domain added so the site has an outcome the US cannot ship without. The difference is small on paper and large in year three.

### C. Graduating extension — start as an extension of US teams, graduate on criteria
**Strongest case.** Lowest immediate risk; it lets the org learn who the converted people actually are before committing ownership; Target and Lowe's are real graduations [C5-22][C5-24]; Olson & Olson say common ground must precede remote collaboration, and an extension phase is how common ground is built [C3-44]; Galbraith's lateral-relations-first sequencing is respectable theory [C3-2].
**Why it still loses.** The base rate is ~27% in five years and the celebrated cases took 10–15 years [C5-1][C5-22]; during the extension phase ownership is diffuse, which is the Nagappan defect predictor and the Lee/Spotify "responsibility without accountability" pattern [C3-8][C1-13]; nothing in the incentive structure pushes a US owner to hand off; and "graduation criteria" for GCCs are not documented anywhere the research could verify [C5 §5] — the org would be inventing them under pressure later. The recommendation keeps the *mechanism* (criteria, dated gates) and drops the *starting state* (no ownership).

### D. Undifferentiated hybrid — decide per team, case by case
**Strongest case.** Target's "center of gravity" rule is a hybrid and it worked [C5-22]; Walmart runs global platforms next to a separately owned local product company [C5-28][C5-30]; flexibility respects the fact that domains differ (DalleMule's offense/defense) [C3-42].
**Why it still loses.** "Hybrid" is what mature sites *became*, not what they were chartered as [C5 §5]; without naming which domain and which components on day one, per-team choice produces the half-ownership configuration every source says fails, because each US owner chooses "extension" for their own team [C3-8][C1-31]. The recommendation is a hybrid with the choices made.

---

## 6. What remains uncertain (carried into the review loop)

- The headcount baseline is assumed. If contractors are concentrated in commerce rather than QoE/platform, Phase 1's "change of ownership, not of hands" claim weakens and Phase 1 takes longer.
- Everything about decision-rights frameworks, budget ownership and on-call at GCCs is consultant material [C5 §3]; the decision-rights tables above are judgment.
- No source treats domain-vs-capability at a *remote* site for *data* teams specifically [C3 §8]; the recommendation extrapolates from software-engineering distance research and GCC base rates.
- The 27% base rate and the attrition figures come from firms with a commercial interest in GCCs [C5-1][C5-7].
- Attribution is weak everywhere; this memo rests on avoiding documented failure modes more than on copying documented successes.
