# Synthesis — what five research tracks agree on, and where they don't

**Date:** 2026-08-29. **Inputs:** C1 (streaming-native cases), C2 (legacy media cases), C3 (canon), C4 (learning plan), C5 (India charter evidence). Citation keys refer to each report's source list. Judgment calls are marked **[judgment]**.

---

## A. The strongest cross-cutting findings

### 1. Every company that runs data at scale keeps the platform central and puts the *people* near the domain.
Netflix (one DSE org, analysts aligned to verticals, central XP and MLP) [C1-1][C1-2][C1-3]; Spotify (central data platform and experimentation platform, embedded Product Insights) [C1-14][C1-16][C1-23]; Google (central experiment infrastructure since 2007) [C1-24]; Disney (central Experiment-X + 19 federated stakeholder teams) [C2-12]; NBCU (centralized CDO org with teams "embedded with and equally accountable to" the businesses) [C2-33]. The two public counter-examples are both *retrofits after failure*: Spotify squads negotiating experiment bucket ranges by hand until a 2018 platform [C1-14]; Amazon finance's 25+ siloed databases until the 2019 Galaxy lake [C1-34]; Paramount's three services on two clouds with separate data pipelines for seven years [C2-43]. `[documented]` Nobody publicly runs per-domain metric definitions or per-domain A/B stacks. `[inferred]`

### 2. Remote engineering sites are chartered on capabilities, not data domains — and the exceptions took decades or were home-market products.
Netflix Warsaw: infrastructure, gaming, production tech [C1-6]. Prime Video Bengaluru: playback, X-Ray, live, client testing [C1-36]. WBD India: data engineering/ML, applied DS, ad platforms, enterprise data [C2-22]. Sky/Peacock UK: the whole streaming platform, reused for SkyShowtime and Showmax [C2-28][C2-29]. Spotify Boston: an acquired, self-contained capability [C1-22]. The only remote site that grew into product-surface ownership is Google Zurich, after ~18 years and at ~5,000 people [C1-27]. The only India engineering orgs that owned a consumer domain end-to-end — Hotstar, Google Pay — were India-first products with local P&L, and Hotstar's tech team drained to a competitor when the rights economics turned [C2-16][C5-33][C5-35]. `[documented]`

### 3. Distance does not degrade quality; diffuse ownership and coupled work do.
Microsoft Vista: distributed development had a negligible effect on post-release failures once ownership was clear and process/tooling were shared [C3-9]; the same dataset shows diffuse ownership predicts defects at ~86% precision [C3-8]. Cross-site work items take ~2.5x as long, driven by more people per item, not slower people [C3-43][C5-18]. Time-zone separation hurts more than spatial separation [C5-19]. The tactic with evidence behind it is to *reduce intensive collaboration across sites* by giving each site separable modules [C3-45][C5-20]. `[documented]`

### 4. The graduating-extension model has a real but low base rate, and the graduations that happened were preceded by hiring product, data science and managers in India.
~27% of India GCCs reach "Portfolio Hub" ownership within five years, per the firm that sells GCC set-ups (so treat as an upper bound) [C5-1]. Target (2005 IT support → integrated HQ) and Lowe's (2015 "one team, multiple locations" → India VPs owning Applied AI/Data and platforms) took 15 and 10 years respectively, and both hired PM/DS/managers before ownership moved [C5-22][C5-24][C5-25]. Forrester's 2007 cohort had >60% of captives "struggling," and the 2008–09 divestitures were support charters that never got anything to own [C5-12][C5-13]. `[documented, partly consultant-sourced]`

### 5. A single accountable owner per separable unit of work is what survived in every case; autonomy without ownership is what failed.
Amazon's single-threaded leader correction ("the biggest predictor of a team's success was not whether it was small" — it was dependencies) [C1-31]; Spotify's own people on the squad model ("even at the time we wrote it, we weren't doing it") and its 2023 re-centralization ("too many people... doing work around the work") [C1-13][C1-20]; Target's "ownership of outcomes rests with where the center of gravity for the capability sits" [C5-22]. `[documented]`

### 6. Structure is the least powerful lever and the most frequently re-decided one.
Galbraith: processes, rewards and people compensate for a mediocre structure but not the reverse [C3-1]. Every data reorg at Disney, WBD, NBCU and Paramount was triggered by a P&L question, never a data question; the two most recent (2026) pulled product data platforms toward ad monetization [C2-11][C2-43]. `[documented]` Whatever the India site owns must be robust to the US org being re-cut every 2–3 years by someone else. **[judgment]**

### 7. The talent facts constrain year one more than the org theory does.
AI/data roles in India GCCs run 18–25% attrition with 18–24-month tenures; the binding scarcity is second-line managers, not engineers; the vendor controls which contractors are offered for conversion; GCCs now pay 15–40% above IT services at mid-senior levels, so conversion at market bands is a cost step-up, not a saving [C5-7][C5-9][C5-11][C5-15]. `[documented, consultant/secondary]`

### 8. Experimentation is a platform discipline with a human review gate, everywhere.
Google's experiment council [C1-24], Spotify's fail-rate checks, reviewers and "engagement team" [C1-17], Netflix's XP + embedded scientists in "intentional collaboration" [C1-2], Disney's Core Experimentation sub-team owning standardized analysis [C2-12]. The *platform engineering* is separable; the *analysis and launch decision* sit with the stakeholders. `[documented]`

---

## B. The honest tensions

### T1. Which domain should India own first? The reports disagree — productively.
- C3 (canon) argues for **defense-heavy** work — fraud, commerce data quality, subscriber-state modeling — because it is coordinated by standardized outputs, which distance tolerates; and *against* experimentation/browse/funnel work, which is adhocratic and stakeholder-adjacent.
- C5 (India evidence) argues for **experimentation platform or QoE/sessions telemetry** — high-volume, low-regulatory, few US business stakeholders — and *against* commerce/fraud, which has the most US stakeholders and the most latency-sensitive decisions.
- C1 and C2 (cases) both name **QoE or sessions** as the least politically contested, best-instrumented candidates; C2 adds fraud and paid-sharing as "stable and measurable" versus commerce packaging and funnels, which are "most exposed to strategy swings."

**Resolution [judgment]:** the criterion everyone actually shares is *few US decision-makers in the loop per change, standardizable outputs, and separability from the warehouse's reciprocal dependencies*. QoE/sessions passes all three (telemetry in, metrics out, consumers are engineers and a small analytics group). Fraud/paid-sharing passes the first two but has US trust-and-safety, legal and finance stakeholders and decisions with real dollar latency — it is the *second* candidate, not the first, and only once an India PM exists. Commerce packaging, conversion funnels, browse and search fail the first test outright while pricing, bundling and content strategy are set in the US. Experimentation splits: the platform engineering is a capability (India-ownable); the analysis/review function stays with the stakeholders.

### T2. Team Topologies and data mesh prescribe domain-owned data teams; the staffing arithmetic says a 140-person org cannot afford eight of them.
Larson's six-person team floor × eight domains = 48 heads of domain data engineering before a platform exists [C3-23]; the 2026 Thoughtworks data-mesh retrospective says most orgs cannot staff data-competent domain teams and end up with a thick central platform doing the domain work anyway [C3-33]. **[judgment]** At 140, Netflix-style hub-and-spoke (central reporting line and hiring bar, people aligned to verticals) is the closest documented analogue, not mesh.

### T3. Conway's Law cuts both ways on data.
The mirroring hypothesis is well-supported for software [C3-7], but warehouse data is reciprocally interdependent — every domain reads every other domain's facts — so mirroring the org onto the data produces silos before it produces modularity [C3-52]. Architecture reduces coordination need by ~30%, not to zero [C3-12]. **[judgment]** "Give India a clean module and the coordination problem goes away" is one-third true.

### T4. Span-of-control ceilings vs. team-size floors at a small site.
A 12-person site with two domains cannot honor both Larson's floor (6–8) and the span ceiling (≤8) without a layer nobody wants to fund [C3-23][C3-24]. The frameworks are silent; budget decides. **[judgment]** This is the arithmetic that says the India site should start with *fewer, whole* teams rather than many partial ones.

### T5. Platform ownership is both the modal success and the modal drift.
JPMorgan (55k) and WBD India show platform charters scale; Citi's captive sold to TCS and Borowski's "captives become stagnant with marginal improvements" show they drift into cost centers when no product outcome depends on them [C5-13][C5-15][C5-26][C5-31]. **[judgment]** A platform-only India charter is the safe choice that quietly becomes the stagnant choice unless the site also owns one outcome the US cannot ship without.

### T6. Mintzberg's adhocracy vs. Galbraith's formal lateral processes.
Innovative data work is coordinated by mutual adjustment, which is exactly what distance destroys; the only fix is formalized interfaces, which Mintzberg predicts will slow the work [C3-4][C3-44]. No clean resolution — route adhocratic work to where the stakeholders sit; formalize only the interfaces. **[judgment]**

### T7. The evidence on GCC decision rights, budget and on-call is consultant material.
Nothing rigorous exists on "send a US leader vs. hire local," RAPID/DACI adoption, or budget ownership at GCCs; C5 flags all of it as `[unverified]`. Nothing in the data-org literature is replicated or treats geography [C3 §8]. The recommendation will have to make judgment calls here and label them.

### T8. Attribution is weak everywhere.
No company has published outcome data tying structure to results; every streaming P&L turn in 2023–2025 is better explained by pricing, paid-sharing enforcement and content cuts than by any org chart [C2 §1.5, §2.4]. What *is* attributable are the coordination failures companies wrote about fixing [C1-14][C1-34][C2-43]. The recommendation rests on avoiding documented failure modes more than on copying documented successes.

---

## C. What this means for the recommendation (bridge to `recommendation.md`)

1. Charter the India site on **platform/capability ownership plus one whole, separable domain (QoE/sessions)**, with a written graduation path for a second domain (fraud/paid-sharing). Pure extension is the documented stagnation path; pure domain ownership of commerce/funnels has no documented success case for a new GCC.
2. Whatever India owns, the **US org must stop owning it** — half-ownership is the one configuration every source says fails.
3. Hire the **site head (global functional title), one PM and second-line managers before graduating anything**; the graduations that happened all did this first.
4. Keep **experimentation analysis, metric definitions and the review gate central**; India can own the experimentation *platform engineering* as a capability.
5. Design the interface as **Team APIs and data contracts**, not stand-ups; budget for the residual ~2.5x on anything still shared.
6. Write **graduation criteria and tripwires now**, because nothing in the incentive structure pushes a US owner to hand off later.
