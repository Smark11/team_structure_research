# C1 — Streaming-native / tech case studies: Netflix, Spotify, YouTube/Google, Amazon (Prime Video + Amazon data model)

**Research agent:** C1 | **Date:** 2026-08-29 | **Status:** evidence memo, not a recommendation

**Reader's decision:** charter for an India site inside a ~140-person data org (commerce, experimentation, browse/search, sessions, QoE, funnels, core platform) — full domain ownership vs. platform/capability ownership vs. graduating extension vs. hybrid.

**Tags:** `[documented]` = source fetched and read; `[inferred]` = reasonable read of public signals; `[folklore]` = widely repeated, weakly sourced. Where I could not reach a source I say so rather than cite it.

---

## 0. The short version

1. All four converge on the same shape: a **central platform (data, experimentation, ML) plus domain-aligned scientists/analysts**, differing mainly in where the domain people's reporting line sits (Netflix: central org, vertically aligned; Spotify: product areas; Amazon: business orgs; Google: product areas). `[documented]`
2. **Experimentation is a central platform everywhere, governed by tooling plus human review** — Google's "experiment council" [C1-24], Spotify's fail-rate checks and reviewers [C1-17], Netflix's XP/embedded-scientist "collaboration" [C1-2]. `[documented]`
3. **Remote sites hold capability or product-vertical charters, not data-domain ownership.** Warsaw: production tech/infra/gaming [C1-6]; Boston: acquired music intelligence [C1-22]; Zurich: YouTube's second development HQ [C1-27]; Bengaluru: playback, X-Ray, live, client testing [C1-36]. `[documented]`
4. **Spotify's own people have said since 2015 that the "Spotify model" was aspiration, not practice, and Spotify re-centralized at the top in 2023** [C1-11][C1-12][C1-13][C1-19][C1-20]. `[documented]`
5. Outcome attribution is weak everywhere; what *is* attributable are the coordination failures structure created and companies then wrote about fixing [C1-14][C1-31][C1-34]. `[documented]`

---

## 1. Netflix

### 1.1 Structure
Netflix's data org has, since at least 2020, been a single **"Data Science and Engineering" (DSE)** group that spans data engineering, analytics engineering, visualization engineering, experimentation/causal-inference data science, and algorithms research [C1-1][C1-2]. `[documented]` The 2020 analytics post is explicit about the design principle: "we align our analytics professionals with the listed business area verticals rather than organizing them within a single functional horizontal," with the stated intent that analytics people "possess deep business context and are thought leaders alongside their business counterparts" [C1-1]. `[documented]` The verticals shown in the post's figure include content, studio, membership/growth, marketing, product, streaming/platform and finance [C1-1]. `[documented]`

That is a textbook **hub-and-spoke**: one reporting line, craft standard and hiring bar, with people deployed into verticals. `[inferred — the post never uses the phrase.]` The same post calls analytics engineers "a specialized resource and a rare commodity" who "are given freedom to choose their projects" and must prioritize by business impact — the central org, not the business partner, owns prioritization of scarce talent [C1-1]. `[documented]`

### 1.2 Platforms: central
- **Experimentation (XP).** The Jan 2022 post by Martin Tingley et al. lays out the structure directly: "there are a number of data science teams at Netflix that partner directly with Product Managers, engineering teams, and other business units to design, execute, and learn from experiments. To enable scale, we've built, and continue to invest in, an internal experimentation platform (XP for short). And we intentionally encourage collaboration between the centralized experimentation platform and the data science teams that partner directly with Netflix business units." [C1-2] `[documented]` Embedded scientists own the full lifecycle while XP provides allocation, measurement and tooling [C1-2]. Scientists "own all aspects of the analysis of a study (with help from our stellar data engineering and experimentation platform teams)" and "bring our analytics point of view to lively cross-functional debates on roll-out decisions" — launch decisions are cross-functional, owned by neither the scientist nor the platform [C1-4]. `[documented]`
- **ML platform.** The Machine Learning Platform (MLP) team "provides an entire ecosystem of tools around Metaflow" and describes itself as a foundation layer "with integrations to our company-wide data, compute, and orchestration platform"; "hundreds of Metaflow projects" are deployed internally and "all the use cases were engineered by practitioners themselves" — the platform team builds paved roads, domain teams build the models [C1-3]. `[documented]` Data lake is S3/Iceberg with Spark for ETL — a single company-wide warehouse, not per-domain lakes [C1-3]. `[documented]`

### 1.3 How it changed over time and why
- **2020:** Elizabeth Stone joins as VP, Product Data Science & Engineering, later VP, Data & Insights [C1-7]. `[documented]`
- **Oct 2023:** Stone named Netflix's first-ever CTO [C1-7][C1-8]. `[documented]`
- **Feb 2026:** Stone promoted to Chief Product and Technology Officer, leading "product, engineering, and data teams," after CPO Eunice Kim's Sept 2025 departure; co-CEO Greg Peters cited her ability to "simplify complexity, connect the dots across our business, and help teams move quickly" [C1-8]. `[documented]`

The read: the data leader absorbed product and engineering, not the reverse — the strongest public signal of a centralized data org that reports high. `[inferred]` A Netflix jobs page describing "Data & Insights" as "centralized and globally distributed" surfaced only in search results; unverified.

Triggers: the 2022 reorganization (ads tier, paid sharing, layoffs) reshaped the leadership tier, but no public statement ties a data-org reorg to it; the hub-and-spoke shape looks stable across 2020–2024 posts. `[inferred]`

### 1.4 Global site strategy
Netflix's engineering is overwhelmingly US-based (Los Gatos, Los Angeles). In Jan 2023 it announced its first engineering hub outside the US, in Warsaw, to "help build the products that our internal and external creative partners use to deliver Netflix shows and films," citing Poland's "amazing engineering talent" [C1-5]. `[documented]` By March 2026 the new Warsaw office housed ~300 staff across functions and was described as "Netflix's only technology hub outside of the United States," with engineering focused on **infrastructure, gaming and production technology** [C1-6]. `[documented]` India offices (Mumbai; Hyderabad opened March 2026) are content/production and AVGC-focused, not engineering [C1-9]. `[documented]`

Note the charter shape: the one non-US hub got **capability/platform charters** (production tooling, infra, games), not "own the membership data domain." `[documented]` No data-science or analytics charter for Warsaw appears in any public statement I read. `[inferred]`

### 1.5 Outcomes and attribution
Netflix claims decisions across "every corner of the business" run through tests and DSE [C1-1][C1-2], but nothing public separates the structure's contribution from the "context not control" culture the same posts lean on. `[documented claim; attribution unproven]` What is attributable: the central-platform + embedded-scientist arrangement scaled to "hundreds" of ML projects and company-wide experimentation without fragmenting into per-domain platforms [C1-2][C1-3]. `[inferred]`

---

## 2. Spotify

### 2.1 The 2012 snapshot and what it actually said
The Kniberg & Ivarsson whitepaper (Oct 2012) described ~30 squads across 3 cities, squads as "mini-startups" with long-term missions, tribes capped "smaller than 100 people or so" on the Dunbar rationale, chapters and guilds for craft alignment — and opened with a disclaimer that is usually skipped: "This article is only a snapshot of our current way of working — a journey in progress, not a journey completed. By the time you read this, things have already changed." [C1-10] `[documented]` Squads were explicitly told to use "metrics and A/B testing to find out what really works" ("Think it, build it, ship it, tweak it") [C1-10]. `[documented]`

### 2.2 Spotify's own retrospectives
- **Kniberg, June 2015:** the material "wasn't actually intended to be a generic framework or 'model' at all. It's just an example of how one company works"; he states he did not invent it and advises adapting, not copying [C1-11]. `[documented]`
- **Ivarsson, July 2016 (podcast):** "Spotify is not a model"; the authors "never imagined the spread"; he names alignment across teams as a growing problem and squad autonomy as in tension with "a consistent design language and customer journey" [C1-12]. `[documented]`
- **Jeremiah Lee, April 2020 ("Spotify's Failed #SquadGoals"):** a former Spotify PM (2017–) argues the model "was only ever aspirational," quotes agile coach Joakim Sundén (2011–2017): "Even at the time we wrote it, we weren't doing it. It was part ambition, part approximation," and lists four failure modes — matrix management with unclear accountability, autonomy without alignment, collaboration assumed rather than taught, and terminology that made the model hard to evaluate. He says leadership "incrementally transitioned to more traditional management structures" [C1-13]. `[documented]` (The Sundén and Ivarsson quotes I have only via Lee's post and the podcast page respectively; I did not find Sundén's original.) `[documented, second-hand]`

A 2023 Journal of Systems and Software study on decentralized decision-making at Spotify (Šmite et al.) describes the later "missions → tribes → squads" layering; the publisher blocked my fetch, so I do not cite it and cannot vouch for its detail. The existence of "Missions" as an organizational layer above tribes is widely repeated but, for this memo, `[folklore]`.

### 2.3 Data science: embedded ("Product Insights")
Spotify's data scientists and user researchers sit together in **Product Insights** teams embedded with product areas, with reporting lines deliberately not split by discipline; the post states Product Insights "is not a centralized function." [C1-23] `[inferred — I could only read this post via a search-index excerpt; both the Medium original and the EPIC mirror returned 403. Treat the quote as probable, not verified.]` Analytics engineering at Spotify is also organized within Insights rather than in a central data team (same caveat).

### 2.4 Platforms: central, and increasingly so
- **Data platform.** As of April 2024 Spotify describes a dedicated data-platform organization with three areas — Data Collection, Data Processing, Data Management — evolved from "a single group managing Europe's largest Hadoop cluster," processing 1.4 trillion data points/day and "aligned to deliver on its proposition to fuel crucial use cases for different parts of the business, from payments to experimentation" [C1-16]. `[documented]`
- **Experimentation.** Timeline from Spotify's own posts: an early Analytics team ran ad-hoc tests; **2013** a team was spun up to build ABBA; a **2017** hack-week diagnosis found four structural problems — one-to-one coupling of experiments to feature flags, A/B events being ~25% of total event volume, data scientists doing inconsistent notebook analyses, and *teams manually coordinating bucket ranges between experiments*, which was "error prone" — leading to the **2018** Experimentation Platform with a central Metrics Catalog [C1-14]. `[documented]` By 2023 the platform served "hundreds of squads and thousands of developers," scaled from "fewer than 20 priority experiments per year" to "thousands," and was externalized as **Confidence** [C1-15]. `[documented]` In 2025 the platform team reports a 64% "learning rate" vs. 12% win rate, governs quality with automated fail-rate checks (sample-ratio mismatch, pre-exposure imbalance, misconfigured serving), and runs an "engagement team" as a "center of excellence for internal customer success" — training, best practices, and "adding experiment reviewers" which "can drastically impact learning rates" [C1-17]. `[documented]` In Jan 2026 Spotify explained why the ML/personalization stack and the experimentation stack are owned by different teams with deliberately separate infrastructure, integrated by API; 58 teams ran 520 experiments on the mobile home page alone in a year [C1-18]. `[documented]`

The manual-coordination failure in [C1-14] is the clearest public example of what "autonomous squads, no central platform" costs in a data org: the squads were literally negotiating bucket ranges with each other. `[documented]`

### 2.5 How the structure changed and why (2023 onward)
- **Jan 23, 2023:** ~6% cut; Gustav Söderström named Chief Product Officer and co-president overseeing "the majority of our engineering and product work"; Alex Norström Chief Business Officer and co-president. Reasons stated: "drive more efficiency, control costs, and speed up decision-making"; 2022 opex growth "outpaced our revenue growth by 2X" [C1-19]. `[documented]`
- **Jun 2023:** ~200 cut in a podcast-division "strategic realignment." `[documented in trade press; not fetched here — treat as context]`
- **Dec 4, 2023:** ~17% cut. Ek: "By most metrics, we were more productive but less efficient. We need to be both"; there were "too many people dedicated to supporting work and even doing work around the work rather than contributing to opportunities with real impact"; "being lean is not just an option but a necessity" [C1-20]. `[documented]`

That is an explicit management verdict on the autonomy-heavy structure: the cost was coordination work, not output. `[inferred — Ek does not name the squad model.]`

### 2.6 Global site strategy
R&D hubs as of 2019: Stockholm, Gothenburg, New York, San Francisco, Boston, plus London (opened April 2019) as "Spotify's first major technology center outside the US and Sweden" [C1-21]. `[documented]` Boston exists because of the March 2014 acquisition of The Echo Nest (music-intelligence/recommendation), whose Somerville HQ Spotify committed to keep running [C1-22]. `[documented]` Spotify's current locations page lists 27 offices including Bangalore, Gurgaon and Mumbai but does not distinguish engineering from commercial sites; I found no public evidence of an India R&D charter. `[documented absence]` Pattern: Spotify's non-Stockholm hubs grew from either an **acquired capability** (Boston) or **talent-market access** (NYC, London), and at least in public framing they hold product-area and capability charters, not data-domain charters. `[inferred]`

### 2.7 Outcomes and attribution
The one clean structure-to-outcome link is negative and self-reported: squad autonomy produced coordination waste in experimentation (2017) [C1-14] and "work around the work" company-wide (2023) [C1-20]. `[documented]` Experiment volume growing to thousands per year is attributable to the platform and its center-of-excellence practices, not to the squad model [C1-15][C1-17]. `[inferred]`

---

## 3. YouTube / Google

Caveat: Google publishes almost nothing about YouTube's data-science org; what follows is Google-wide with YouTube specifics where they exist.

### 3.1 Structure
Google's data-science roles are titled by product area ("Data Scientist, Product," "Data Scientist, Core Compute," "Business Data Scientist, gTech") and split into product vs. research tracks, which signals an **embedded-by-product** model with a shared job ladder rather than a single central analytics org. `[inferred — from job-title conventions only; no Google org statement found.]` ML engineering sits under SWE. `[inferred]`

### 3.2 Experimentation: central infrastructure, engineer-run governance
The canonical source is Tang, Agarwal, O'Brien & Meyer, KDD 2010. Google's overlapping experiment infrastructure — domains/layers/experiments, deployed **March 2007** — is company infrastructure, and the paper is explicit that "an experiment infrastructure alone is insufficient": it adds tools (automated data-file checks, real-time monitoring, standardized metrics so "two experimenters should use the same filters") and two human processes: an **experiment council**, "a group of engineers who review a light-weight checklist that experimenters fill out prior to running their experiment," and a discussion forum where results are interpreted and archived [C1-24]. `[documented]` Governance is thus a central review gate staffed by engineers, not a data-science sign-off; product teams design and run experiments themselves. `[documented]` Whether YouTube runs on this exact stack today is not public. `[inferred]`

### 3.3 How it changed and why
- **Apr 20, 2023:** Google merged Google Research's Brain team with DeepMind into Google DeepMind under Demis Hassabis; Jeff Dean became Chief Scientist reporting to Pichai. Stated reason: "the pace of progress is now faster than ever" and combining "into one focused team, backed by the computational resources of Google, will significantly accelerate our progress in AI" [C1-25]. `[documented]` This is a **centralization** move for frontier ML research, triggered by competitive pressure — the opposite direction from product-embedded DS.
- **Feb 2023:** Neal Mohan (ex-CPO) became YouTube CEO. `[documented in reporting; not fetched — context only]` I found no public YouTube data-org reorg.

### 3.4 Global site strategy
- **Zurich:** Google's largest development center outside the US; ~2,000 in 2017 growing toward 5,000, hosting Search, Maps, Calendar, YouTube, Gmail, Assistant, Photos and Translate engineering and described as the European home base for ML [C1-26]. By 2022 ~5,000 staff and "Zurich is currently the largest headquarters of the YouTube development team alongside the headquarters in San Bruno" [C1-27]. `[documented]` That is a **product-engineering** charter for a remote site at full-peer scale — the best example in this set of a non-HQ site owning product surface areas, though not the analytics function.
- **India:** Google's India engineering centres (Hyderabad IDC, dated 2004 by a secondary source; Bengaluru) are ~10,000 people with charters cited as Search quality, Pay infrastructure, Cloud, and AI [C1-28]. `[folklore — the only source I could reach is a GCC-directory profile compiled from LinkedIn/Wikipedia; treat specifics with suspicion.]`
- **London:** DeepMind HQ [C1-25]. `[documented]`

### 3.5 Outcomes and attribution
Only the 2010 paper's own result is attributable: experiment count, launches and distinct experimenters rose after the 2007 infrastructure plus council/forum processes [C1-24]. `[documented]` YouTube's data org is undocumented, so nothing there is attributable.

---

## 4. Amazon — Prime Video and the broader Amazon data model

### 4.1 The org model: two-pizza teams → single-threaded leaders
AWS's own explainer: two-pizza teams (<10 people) with "single-threaded ownership" of one product/service and its full lifecycle, adopted to "minimize lines of communication and decrease overhead of bureaucracy," with single-threaded leaders (STLs) using narratives for oversight rather than approvals [C1-29]. `[documented]` Bryar & Carr (*Working Backwards*, 2021) [C1-30] report the correction Amazon made: "the biggest predictor of a team's success was not whether it was small" — it was dependencies; Amazon treated inter-team coordination as a defect to eliminate and shifted the emphasis from team size to a single-threaded leader with a separable team; "the best way to fail at inventing something is by making it somebody's part-time job" [C1-31]. `[documented via secondary summary of the book; I did not read the book pages directly.]` The "Bezos API mandate" has only a memoir post as its source; `[folklore]`, not cited. Practitioners distinguish single-threaded *ownership* (leader controls all resources) from single-threaded *leadership* (leader drives priorities across lines that report elsewhere) [C1-38]. `[inferred]`

### 4.2 Where data sits
Amazon does not have a company-wide "data organization." Data engineers, BIEs, data scientists, applied scientists and economists are hired by, and report into, business orgs (a "Data, eNgineering and Analytics (DNA)" team inside North American Stores surfaced in search, spanning DA/DE/BI/DS for that one org). `[inferred — the job page 404'd when I fetched it; the pattern is consistent with amazon.jobs title conventions but I could not verify a specific posting.]` The consequence is documented by Werner Vogels (Jan 2020): before the **Galaxy** data lake, Amazon's operations-finance data lived in "more than 25 databases with regional teams creating their own local version of datasets," each with separate credentials; a finance-operations team (not a central data org) built Galaxy in 2019 on S3 plus the proprietary Andes and Elastic Data eXchange layers, and "the various teams are working on moving their data into it" [C1-34]. `[documented]` This is the cost side of full decentralization: duplicated datasets, per-team access, and a retrofitted central catalog.

### 4.3 Experimentation
Weblab is Amazon's internal A/B platform; Ron Kohavi "was the director of data mining and personalization at Amazon, where he was responsible for Weblab" [C1-32] — which places Weblab in the early 2000s. `[documented]` The widely circulated numbers ("created 2011, 546 experiments year one, 12,000+ per year now") appear in vendor blogs without citations [C1-33] and conflict with Kohavi's tenure; treat as `[folklore]`. What is safely inferable: a central platform, used by business teams under their own STLs, with launch decisions inside the owning team. `[inferred]` An "Experimentation & Optimization" team page exists on amazon.jobs but did not render for me; not cited.

### 4.4 Prime Video
Prime Video's engineering is organized as **Prime Video Experience & Technology (PVXT)**, "the technical backbone of Amazon Prime Video's global streaming service," covering discovery/search, playback, download, live, encoding, delivery, client experiences, content protection and anti-fraud [C1-36]. `[documented]` The 2023 "microservices to monolith" post was one PVXT service team's architectural call — STL autonomy in action, not an org story. `[documented; widely misread]` On the business side, Prime Video India's functional heads (SVOD, marketplace, marketing, originals, licensing, productions) report to a VP for APAC & MENA, with the India country-director seat vacant since July 2024 [C1-37]. `[documented]` Business leadership is regional; technology is global (PVXT). `[inferred]`

### 4.5 Global site strategy (India)
Amazon's Hyderabad campus (opened Aug 2019) is its largest building worldwide with 15,000 seats, hosting AWS, Kindle, Alexa, Amazon.in and Home Services teams; India country manager Amit Agarwal: "This facility will build services globally" [C1-35]. `[documented]` Prime Video's Bengaluru site is expanding "spanning across X-Ray, playback services, live technologies, player and client testing and other foundational technologies," with a Principal Engineer role to "guide global Prime Video teams on architecture decisions" [C1-36]. `[documented]` Pattern: Amazon India sites hold **capability and service charters inside global orgs** (playback, X-Ray, Kindle, Alexa services), with STLs on site; they are not carved out as "India owns the commerce data domain." `[inferred]` I could not verify the frequently repeated "Amazon IDC began in Hyderabad in 2004" from a primary source; Gulf News dates Amazon's *retail* entry to 2013 [C1-35]. `[folklore]`

### 4.6 Outcomes and attribution
Attributable: the STL model's self-diagnosed failure mode (dependencies, not size) [C1-31] and the silo cost that forced Galaxy [C1-34]. `[documented]` Prime Video's product outcomes cannot be tied to PVXT's structure from public material.

---

## 5. Cross-case synthesis

| | Reporting line of domain analysts/scientists | Data platform | Experimentation platform | Exp. governance | Remote-site charters (public) |
|---|---|---|---|---|---|
| Netflix | Central DSE org, vertically aligned [C1-1] | Central (S3/Iceberg, Spark, Metaflow MLP) [C1-3] | Central XP + embedded scientists, "intentional collaboration" [C1-2] | Cross-functional roll-out debates; scientists own analysis [C1-4] | Warsaw: infra, production tech, gaming [C1-6] |
| Spotify | Embedded Product Insights in product areas [C1-23, weakly verified] | Central data platform org (collection/processing/management) [C1-16] | Central EP/Confidence, built after squad-level coordination failed [C1-14][C1-15] | Automated fail-rate checks, reviewers, center-of-excellence [C1-17] | Boston (acquired capability), London (talent access) [C1-21][C1-22] |
| Google/YouTube | Embedded by product (title conventions) [inferred] | Central infra (undocumented for YouTube) | Central since 2007 [C1-24] | Experiment council of engineers + forum [C1-24] | Zurich: full product-engineering peer incl. YouTube [C1-27] |
| Amazon/PV | Inside each business org under STLs [inferred] | Historically per-org; Galaxy retrofitted 2019 [C1-34] | Central Weblab, decisions in owning team [C1-32] | Team-level; no central council public | Hyderabad/Bengaluru: services & capabilities inside global orgs [C1-35][C1-36] |

Three things stand out. **The platform is always central, and the two companies that let it be otherwise paid for it in public**: Spotify's squads negotiating experiment buckets by hand [C1-14] and Amazon finance's 25 databases [C1-34] were both fixed by building a central platform after the fact. `[documented]` **"Embedded" means embedded scientists, never embedded platforms**: Netflix keeps the reporting line central; Spotify moved it into product but keeps metric definitions in a central catalog [C1-14]; Google keeps a central review gate [C1-24]. Nobody publicly runs per-domain metrics or per-domain A/B stacks. `[inferred]` **Remote-site charters are capability-shaped**; the one site that grew into product-surface ownership (Zurich) took ~18 years and ~5,000 people, and still does not own the analytics function [C1-27]. `[documented + inferred]`

---

## 6. What I could not verify
Netflix "Data & Insights" scope (search snippet only); Spotify Product Insights "not a centralized function" (403 on both hosts; search excerpt only); Spotify "Missions" layer and the 2023 JSS study (publisher blocked; not cited); Sundén's original statement (only via Lee); Amazon Weblab date and experiment counts (vendor folklore, contradicted by Kohavi's tenure); "Amazon IDC Hyderabad 2004" (no primary source); Google India charters (directory site only); YouTube's internal data-org structure (no public documentation found); Amazon "DNA" BIE team page (404).

---

## Implications for the decision

**Domain vs. capability ownership at a remote site.** The evidence leans hard one way: every remote engineering site in these four cases holds a capability or service charter first (production tooling, playback, X-Ray, music intelligence, infra), and the only site that grew into product-surface ownership (Google Zurich) did so over roughly two decades and at a scale that dwarfs a 140-person org [C1-27]. No case shows a remote site being handed end-to-end ownership of a *data domain* (commerce, experimentation analysis for the business) as its founding charter. **[judgment]** For an India site converting contractors to FTEs, the cases support starting with **platform/capability ownership** — core data platform components, experimentation-platform engineering, metrics-catalog/QoE pipelines — where the work is well-specified, the interface to US stakeholders is an API or a dataset rather than a daily product debate, and a single-threaded leader can sit on site. **[judgment]** Full domain ownership (e.g., "India owns commerce analytics") is what the Netflix and Spotify models both say requires "deep business context" alongside business counterparts [C1-1][C1-13]; that context is hardest to acquire across 10+ time zones from stakeholders who sit in the US. If a domain is moved, the Amazon pattern says move the *decision-maker* with it (an STL on site with the whole separable team), not just the analysts [C1-29][C1-31]. **[judgment]**

**Graduating extension vs. hybrid.** Spotify's Boston hub is the best precedent for graduation: it started as an acquired, self-contained capability and became a personalization center because it owned something whole from day one [C1-22]. Sites that start as overflow labor for US teams have no such anchor; Ek's "work around the work" [C1-20] is what an extension model produces at scale. **[judgment]** A hybrid — platform ownership on site now, plus one narrowly scoped, whole domain (QoE or sessions, which are instrumented, metric-defined and less politically contested than commerce) with its own leader as a graduation test — is the shape most consistent with the evidence. **[judgment]**

**Central vs. embedded at ~140 people.** All four companies are 10–100× larger and still keep platform, metric definitions and experiment review central [C1-2][C1-14][C1-24]. At 140 people the case for a *fully* embedded model is weaker than at Spotify's scale, and Netflix's hub-and-spoke — central reporting line and hiring bar, people aligned to verticals with the org (not the partner) prioritizing scarce talent [C1-1] — is the closest documented analogue to a mid-sized data org with a central leader. **[judgment]** The one thing the cases say not to do is let domain teams stand up their own platforms; the Spotify 2017 and Amazon 2019 retrofits are the bill for that [C1-14][C1-34]. Experimentation specifically should stay a single central platform with an explicit review gate; whether the review is engineers (Google) or a center-of-excellence with reviewers (Spotify) matters less than that it exists and is staffed [C1-17][C1-24]. **[judgment]**

Attribution caveat: none of this proves structure *causes* outcomes; the cases document which structures generated coordination costs large enough to be written about.

---

## Sources

All URLs fetched and read 2026-08-29 unless noted. Overall evidence tag in brackets.

- [C1-1] Molly Jackman & Meghana Reddy, "Analytics at Netflix: Who We Are and What We Do," Netflix TechBlog, Sep 18, 2020. https://netflixtechblog.com/analytics-at-netflix-who-we-are-and-what-we-do-7d9c08fe6965 [documented]
- [C1-2] Martin Tingley et al., "Experimentation is a major focus of Data Science across Netflix," Netflix TechBlog, Jan 11, 2022. https://netflixtechblog.com/experimentation-is-a-major-focus-of-data-science-across-netflix-f67923f8e985 [documented]
- [C1-3] David J. Berg et al., "Supporting Diverse ML Systems at Netflix," Netflix TechBlog, Mar 7, 2024. https://netflixtechblog.com/supporting-diverse-ml-systems-at-netflix-2d2e6b6d205d [documented]
- [C1-4] Stephanie Lane, Wenjing Zheng & Mihir Tendulkar, "A Day in the Life of an Experimentation and Causal Inference Scientist @ Netflix," Netflix TechBlog, n.d. (pre-Jan 2022; referenced by C1-2). https://netflixtechblog.com/a-day-in-the-life-of-an-experimentation-and-causal-inference-scientist-netflix-388edfb77d21 [documented]
- [C1-5] Netflix, "Netflix to Open New Engineering Hub in Poland," About Netflix, Jan 10, 2023. https://about.netflix.com/en/news/netflix-to-open-new-engineering-hub-in-poland [documented]
- [C1-6] Netflix, "Netflix Celebrates 10 Years in Poland and Supercharges Warsaw Presence With New Office," About Netflix, Mar 29, 2026. https://about.netflix.com/en/news/netflix-celebrates-10-years-in-poland-and-supercharges-warsaw-presence-with-new-office [documented]
- [C1-7] Netflix Investor Relations, "Leadership and Directors" (Elizabeth Stone biography). https://ir.netflix.net/governance/Leadership-and-directors/default.aspx [documented]
- [C1-8] Variety (Australia), "Netflix Promotes CTO Elizabeth Stone to Chief Product and Technology Officer," Feb 3, 2026. https://au.variety.com/2026/tv/news/netflix-elizabeth-stone-chief-product-and-technology-officer-32672 [documented]
- [C1-9] Siasat, "Revanth Reddy to launch Netflix Studios office in Hyderabad on Mar 12," Mar 2026. https://www.siasat.com/revanth-reddy-to-launch-netflix-studios-office-in-hyderabad-on-mar-12-3425752/ [documented]
- [C1-10] Henrik Kniberg & Anders Ivarsson, "Scaling Agile @ Spotify with Tribes, Squads, Chapters & Guilds," Crisp, Oct 2012 (PDF). https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf [documented]
- [C1-11] Henrik Kniberg, "No, I didn't invent the Spotify model," Crisp blog, Jun 7, 2015. https://blog.crisp.se/2015/06/07/henrikkniberg/no-i-didnt-invent-the-spotify-model [documented]
- [C1-12] The Agile Revolution, "Episode 112: Inside Spotify with Anders Ivarsson," Jul 6, 2016. https://theagilerevolution.com/2016/07/06/episode-112-inside-spotify-with-anders-ivarsson/ [documented]
- [C1-13] Jeremiah Lee, "Spotify's Failed #SquadGoals," jeremiahlee.com, Apr 19, 2020. https://www.jeremiahlee.com/posts/failed-squad-goals/ [documented; second-hand for the Sundén quote]
- [C1-14] Johan Rydberg, "Spotify's New Experimentation Platform (Part 1)," Spotify Engineering, Oct 29, 2020. https://engineering.atspotify.com/2020/10/spotifys-new-experimentation-platform-part-1 [documented]
- [C1-15] Spotify Engineering, "Coming Soon: Confidence — An Experimentation Platform from Spotify," Aug 3, 2023. https://engineering.atspotify.com/2023/8/coming-soon-confidence-an-experimentation-platform-from-spotify [documented]
- [C1-16] Anastasia Khlebnikova & Carol Cunha, "Data Platform Explained Part I," Spotify Engineering, Apr 2, 2024. https://engineering.atspotify.com/2024/4/data-platform-explained [documented]
- [C1-17] Michael Bellato, Mårten Schultzberg & Sebastian Ankargren, "Beyond Winning: Spotify's Experiments with Learning Framework," Spotify Engineering, Sep 23, 2025. https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework [documented]
- [C1-18] Yu Zhao & Mårten Schultzberg, "Why We Use Separate Tech Stacks for Personalization and Experimentation," Spotify Engineering, Jan 7, 2026. https://engineering.atspotify.com/2026/1/why-we-use-separate-tech-stacks-for-personalization-and-experimentation [documented]
- [C1-19] Spotify Newsroom, "An Update on January 2023 Organizational Changes," Jan 23, 2023. https://newsroom.spotify.com/2023-01-23/an-update-on-january-2023-organizational-changes/ [documented]
- [C1-20] Spotify Newsroom, "An Update on December 2023 Organizational Changes," Dec 4, 2023. https://newsroom.spotify.com/2023-12-04/an-update-on-december-2023-organizational-changes/ [documented]
- [C1-21] Music Business Worldwide, "Spotify opens Research and Development hub in London," Apr 16, 2019. https://www.musicbusinessworldwide.com/spotify-opens-research-and-development-hub-in-london/ [documented]
- [C1-22] TechCrunch, "Spotify Acquires The Echo Nest," Mar 6, 2014. https://techcrunch.com/2014/03/06/spotify-acquires-the-echo-nest/ [documented]
- [C1-23] Spotify Insights (Medium), "Cross-disciplinary Insights Teams: How We Integrate Data Scientists and User Researchers at Spotify," n.d. https://medium.com/spotify-insights/cross-disciplinary-insights-teams-how-we-integrate-data-scientists-and-user-researchers-at-spotify-cd8086285f0e — **direct fetch blocked (403) on 2026-08-29; content seen only via search-index excerpt** [inferred]
- [C1-24] Diane Tang, Ashish Agarwal, Deirdre O'Brien & Mike Meyer, "Overlapping Experiment Infrastructure: More, Better, Faster Experimentation," KDD 2010 (Google Research PDF). https://research.google.com/pubs/archive/36500.pdf [documented]
- [C1-25] Sundar Pichai, "Google DeepMind: Bringing together two world-class AI teams," Google (The Keyword), Apr 20, 2023. https://blog.google/technology/ai/april-ai-update/ [documented]
- [C1-26] Google (The Keyword), "Zurich calling – Expanding our European tech hub," Jan 17, 2017. https://blog.google/around-the-globe/google-europe/zurich-expanding-our-european-tech-hub/ [documented]
- [C1-27] Greater Zurich Area, "Google opens innovation center in Zurich," Jun 2022. https://www.greaterzuricharea.com/en/news/google-opens-innovation-center-zurich [documented]
- [C1-28] Business of GCC, "Google LLC (Alphabet Inc.) GCC in Bangalore — Global Capability Center Profile," updated Mar 18, 2026. https://www.businessofgcc.com/gcc-data/companies/google-llc-alphabet-inc-india [folklore — directory compiled from LinkedIn/Wikipedia]
- [C1-29] AWS Executive Insights, "Amazon's Two-Pizza Teams," n.d. https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/ [documented]
- [C1-30] Colin Bryar & Bill Carr, *Working Backwards: Insights, Stories, and Secrets from Inside Amazon*, St. Martin's Press, 2021 (book; publisher page verified only). https://www.amazon.com/Working-Backwards-Insights-Stories-Secrets/dp/1250267595 [documented]
- [C1-31] Sergio Schuler, "The myth of Amazon's 2-pizza teams," Product Leadership IO, Jan 10, 2023. https://www.productleadership.io/p/the-myth-of-amazons-2-pizza-teams-d14f2b4d834f [documented — secondary summary of C1-30]
- [C1-32] Ron Kohavi & Stefan Thomke, "The Surprising Power of Online Experiments," Harvard Business Review, Sep–Oct 2017. https://hbr.org/2017/09/the-surprising-power-of-online-experiments [documented]
- [C1-33] AWA Digital, "Experimentation Culture: The Truth About Amazon And Booking.com," updated Jan 23, 2023. https://www.awa-digital.com/blog/truth-about-amazon-booking-experimentation-culture/ [folklore — numbers uncited]
- [C1-34] Werner Vogels, "How Amazon is solving big-data challenges with data lakes," All Things Distributed, Jan 20, 2020. https://www.allthingsdistributed.com/2020/01/aws-datalake.html [documented]
- [C1-35] Gulf News, "Amazon opens largest campus," Aug 21, 2019. https://gulfnews.com/business/amazon-opens-largest-campus-1.65925605 [documented]
- [C1-36] Amazon.jobs, "Principal Software Engineer, Prime Video & Studios CoreTech — Bengaluru (Job ID 3146219)," 2026. https://amazon.jobs/en/jobs/3146219/principal-software-engineer-prime-video-studios-coretech [documented]
- [C1-37] Outlook Business, "Exclusive: Amazon Prime Video Rejigs India Leadership Structure as Top Job Remains Vacant Amid Battle with JioStar," Jun 12, 2025. https://www.outlookbusiness.com/corporate/exclusive-amazon-prime-video-rejigs-india-leadership-structure-as-top-job-remains-vacant-amid-battle-with-jiostar [documented]
- [C1-38] Pedro Del Gallego, "Single-Threaded Leaders at Amazon," personal blog, n.d. https://pedrodelgallego.github.io/blog/amazon/single-threaded-model/ [inferred — practitioner summary]
