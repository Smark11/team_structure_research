# C2 — Legacy Media Case Studies: Data/Engineering Org Design at Disney, WBD, NBCU/Peacock, Paramount

**Prepared for:** senior data executive, ~140-person data org, media/streaming
**Prepared by:** research agent C2
**Date:** 2026-08-29
**Scope:** org structure, reorg history, central-vs-embedded data, experimentation placement, global site charters, attributable outcomes — for Disney (Disney+/Hulu/ESPN+), Warner Bros. Discovery (HBO Max → Max → HBO Max), NBCUniversal/Peacock, Paramount (Paramount+/Pluto TV).

## How to read this

Legacy media is opaque about org design; the public record is reorg press releases, trade coverage of executive moves and layoffs, a thin layer of engineering-blog and vendor material, and job postings. Two gaps up front: **no company here has published how its experimentation function reports** (Disney's 2022 blog post is closest), and **India-site charters exist only as careers-page copy** (WBD is most explicit).

Tags: `[documented]` = press release, engineering blog, credible trade reporting; `[inferred]` = reasonable read of public signals; `[folklore]` = widely repeated, weakly sourced.

---

## 1. Disney (Disney+, Hulu, ESPN+; Disney Streaming / DTC technology)

### 1.1 Structure and how it changed

Disney's streaming tech org has been reorganized four times in eight years, each time for a CEO-level strategy reason, never a technology one.

- **Mar 2018: DTCI.** The **Direct-to-Consumer & International** segment under Kevin Mayer bundled "BAMTECH (technology and digital products center)" with the Hulu stake, ESPN+, international channels and global ad sales [C2-2] `[documented]`; Aaron LaBerge was its CTO [C2-3]. This is the origin of the BAMTech-lineage "Disney Streaming" engineering culture.
- **12 Oct 2020: DMED.** Chapek collapsed DTCI and Media Networks into **Disney Media & Entertainment Distribution** under Kareem Daniel, responsible for "P&L management and all distribution, operations, sales, advertising, **data and technology** functions worldwide" [C2-1] `[documented]` — streaming tech, ad sales and data under one non-creative chairman, the most centralized Disney's data/tech ever got. LaBerge became DMED CTO [C2-3].
- **Nov 2022 – 8 Feb 2023: DMED unwound.** Iger returned, Daniel exited, and Disney reorganized into Disney Entertainment, ESPN and Experiences, with 7,000 cuts and $5.5B savings announced alongside; Iger's rationale was to put "decision-making back in the hands of our creative teams" [C2-3] `[documented]`. Technology was **not** re-split by brand: it stayed one shared org, "Disney Entertainment & ESPN Technology," under LaBerge as President & CTO reporting jointly to the Disney Entertainment co-chairs and the ESPN chairman, "including the teams that build and run Disney+, Hulu and ESPN+" [C2-4] `[documented]`. That triple reporting line is the key design fact: one tech org, three P&Ls.
- **Aug 2024:** after LaBerge left [C2-4], Disney hired Adam Smith (YouTube VP Product; Subscriptions & Commerce) as **Chief Product & Technology Officer, Disney Entertainment & ESPN**, same triple reporting line, with "engineers, product managers, designers, **data scientists**, and technical operations teams" explicitly in his org [C2-5] `[documented]`. Product-side data science sits inside P&T, not a corporate data function. In Jun 2025 Smith cut "less than 2%" of P&T as "a rebalancing of resources" while still hiring [C2-10] `[documented]`.
- **Apr 2026: data moved toward ads.** After SVP Product Management & Engineering Ajay Arora left, Disney's **Data Product and Engineering** group was moved under Tony Donohoe, EVP of the ad platform (Data Engineering under Alek Zdziarski; Data Product under Romit Mehta, interim). The **"Commerce, Data and Identity" alliance** — which had overseen commerce, growth and account management across streaming — was dissolved, and the internal "Atlas" data initiative was cited as needing "tighter integration with ad technology systems" [C2-11] `[documented]`. This happened during a ~1,000-person cut under new CEO Josh D'Amaro [C2-11].

**Blunt read:** Disney went from "data and tech under a monetization chief" (2020) to "tech under the content businesses" (2023) and in 2026 swung the data platform back under ad-tech. `[judgment]` After five years of product-centric data investment, Disney decided the data platform's highest-value customer was **advertising monetization**. Whether wise or not, it is a warning that a media data org's reporting line follows whichever P&L is being asked to grow this year.

### 1.2 Hulu integration: the stack decision

Disney took operational control of Hulu in 2019; the widely reported plan to "bring Hulu onto BAMTech" is `[folklore]` — I found no primary source in those words. Documented sequence: Iger announced a "one app" experience in May 2023 [C2-7]; full Hulu-on-Disney+ integration shipped 27 Mar 2024, which LaBerge called "the most significant technical, operational, and product evolution for Disney+ since its launch," explicitly designed for reuse in the Star+ → Disney+ LatAm merge and the ESPN DTC launch [C2-6] `[documented]`; in Aug 2025 Iger said both services would be "on one tech platform" with cost synergies and a unified app in 2026 [C2-8] `[documented]`; a leaked May 2026 document said "the Hulu tech stack and app will be decommissioned," which Disney publicly walked back [C2-9] `[documented]`.

**Read:** the BAMTech-lineage stack won. Nothing public says what happened to Hulu's engineering and data teams — no mass layoff was reported and 2025 P&T cuts were <2% [C2-10] — so `[inferred]` this was a multi-year absorption, not a rip-and-replace with a headcount event. Contrast WBD.

### 1.3 Central vs. embedded; where experimentation sits

Disney Streaming's blog is the only first-party account of an experimentation org in this set. In 2019 it formed a central **Experiment-X** team because "different teams were using different tools"; shipped an MVP in six months and "X²" a year later; organized the team "around domains like product, backend engineering, data science and audience intelligence," with a **Core Experimentation** sub-team owning automated, standardized analysis (the ExpAn library) so stakeholders did not depend on analysts; and by Jan 2022 had onboarded **19 stakeholder teams** running experiments across "Landing Page, Sign Up Funnel, Commerce, and Quality of Service (QoS)," with experiment velocity in the OKRs [C2-12] `[documented]`. That is textbook **central platform + federated execution**, and the domains listed are this reader's domains. It was scoped across all "partner applications" (Disney+, Star+, Hulu, ESPN+) — the experimentation platform was multi-brand before the apps were.

Data platform: a Kinesis/Flink real-time pipeline feeding recommendations and operational analytics (2020) [C2-13] `[documented]`; **data governance as a dedicated function** (VP Data Governance, 2021) on Snowflake with "a single copy of data" [C2-14] `[documented]`. Ad-tech data has always sat in the ad org, and since Apr 2026 the streaming data platform reports there too [C2-11].

### 1.4 Global site strategy

**India is the important case, and it is cautionary.** Disney+ Hotstar (Apr 2020) was built on **Hotstar's own platform**, not BAMTech's, to "take advantage of Hotstar's existing infrastructure and customer base," with a UX distinct from global Disney+ [C2-15] `[documented]`. Hotstar was a full-stack, full-domain engineering org from 2015 — its own infrastructure and data platform, documented on its own engineering blog (EKS migration, "datacenter abstraction") [C2-17] `[documented, secondary]`. Its engineering base is usually described as Bangalore `[folklore]` — not primary-verified here.

The lesson is what happened next: after losing IPL digital rights to Viacom18/Jio in 2022, "Hotstar lost a considerable portion of its technology team" to the Jio side along with sports and sales leadership [C2-16] `[documented, single-source]`; subscribers fell >12M in a quarter; and in Nov 2024 Disney folded its whole Indian TV and streaming business into the **JioStar** JV (Reliance 63.16%, Disney 36.84%, Reliance operating), with the apps merged into JioHotstar on 14 Feb 2025 [C2-15] `[documented]`. Disney's only India engineering center of scale was a *product-owning* org with full ownership of a market — and it is no longer Disney's. **I found no evidence of a Disney streaming GCC in India post-JV**; Disney Streaming's tech centers remain US-based `[inferred]`.

### 1.5 Outcomes and attribution

Disney streaming went from ~$4B annual losses to profit across 2023–2025 `[folklore-level consensus]`, driven by pricing, password-sharing enforcement, content cuts and the bundle — not org design. Structure-attributable outcomes I'd defend: (1) one shared tech org across three P&Ls is what made the Hulu and Star+ consolidations reusable [C2-6]; (2) the central experimentation platform is the one data capability Disney chose to publicize, implying internal success [C2-12] `[inferred]`; (3) DMED lasted 28 months — a centralization that ignores where P&L accountability sits does not survive a CEO change.

---

## 2. Warner Bros. Discovery (HBO Max → Max → HBO Max; Discovery+)

### 2.1 Structure and how it changed

- **Pre-merger: two stacks.** HBO Max launched May 2020 on WarnerMedia's platform `[folklore]`. Discovery+ launched Jan 2021 on Discovery's global DTC platform, which had already subsumed Dplay and the Eurosport Player in Europe [C2-49] `[documented]` — multi-market and multi-brand by design before the merger.
- **Apr 2022 merger; Aug 2022 "one service" decision.** CTO Avi Saxena and CPO Tyler Whitworth both came from Discovery [C2-18] `[documented]`. The trade consensus is that **Max was built on the Discovery+ platform**. Be precise: in the only substantive technical interview, Saxena described 12 months of planning "to build a cohesive platform" with "engineer teams from both HBO Max and Discovery+ sides" contributing, a "20% faster" bar and four CDNs — he did *not* say "Discovery+ stack" [C2-18]. So "Max = Discovery+ backend" is `[folklore]`: widely repeated, consistent with who led, never primary-confirmed. `[inferred]` The organizationally important fact is that **the acquirer's smaller tech leadership took over the combined org**, which is unusual and is why the HBO Max engineering culture dispersed.
- **Layoffs.** Aug 2022 HBO Max cuts (70 people, 14% of Casey Bloys' org) were content, casting and international, not tech [C2-19] `[documented]`. Jul 2024 (~1,000 company-wide) was finance/business affairs, with "cuts to Max staffers in the single digits" [C2-20] `[documented]`. **No public source quantifies HBO Max tech/product attrition during the Max build** — "HBO Max engineers left en masse" is `[folklore]`.
- **Jun 2025 split; Dec 2025–Feb 2026 sale.** WBD announced separation into Streaming & Studios (HBO, HBO Max) and "Discovery Global" (CNN, Discovery, **Discovery+**) [C2-26] `[documented]` — the streaming portfolio *re-split by brand* while still sharing a platform. Netflix agreed to buy Streaming & Studios in Dec 2025; Paramount Skydance's hostile bid won with a $110.9B agreement on 27 Feb 2026; shareholders approved 23 Apr; DOJ cleared 12 Jun; 12 state AGs are litigating, trial is Mar 2027, outside date 1 Jun 2027 [C2-27] `[documented]`. WBD's tech org is in its third ownership limbo in five years.

### 2.2 Central vs. embedded; data

WBD's public data footprint is almost entirely **ad-sales**: the "Olli" first-party data platform (Apr 2024) sits in Digital Ad Sales under Ryan Gould on Snowflake clean rooms [C2-21] `[documented]`. Nothing public says where streaming product analytics, experimentation or DS report; job postings reference a "Marketing Intelligence & Data Products" team serving Subscriber Growth & Media `[inferred, snippets not fetched]`. `[inferred]` WBD runs data as embedded functions in ad sales, growth marketing and the DTC tech org, with no single owner.

### 2.3 Global site strategy — the most explicit India charter in this set

- Announced 17 May 2023 after Telangana's IT minister met WBD's SVP Finance; an "International Development Centre" with **1,200 professionals in year one** [C2-23] `[documented]`. Inaugurated 20 Sep 2023 with CFO Gunnar Wiedenfels present; the minister called it WBD's "first Greenfield office in Asia after the merger" [C2-24] `[documented]`. That the CFO, not the CTO, fronted it signals the mandate `[inferred]`.
- WBD's careers site describes an **"India Innovation Hub" across Bangalore, Hyderabad and Pune** with charters: streaming technology and content platforms; **data engineering and machine learning; applied data science**; identity, partnerships, trust & safety; **enterprise data services and automation**; product management; and **advertising platforms** — "building the future of Warner Bros. Discovery streaming from the ground up" [C2-22] `[documented, recruiting copy]`. Listings include Staff Data Engineer and Staff Software Engineer (Data Engineering, AdTech, Bangalore) `[inferred, from search titles]`.
- A GCC directory estimates ~1,500–1,600 heads with a 2,500 target by 2027 across "Max streaming platform, content recommendation AI, ad tech analytics, and enterprise IT" [C2-25] `[folklore — self-rated 75% confidence; conflicts with the primary sources on founding date]`.

**Read:** WBD's India charter is explicitly **capability/platform ownership across streaming, data/ML, ad-tech and enterprise data** — not a market or a product domain. It was stood up at peak cost-cutting (2023) and grew while US headcount shrank `[inferred]`. Europe: Warsaw carries an "HBO Max DTC Technology organization" (HBO Europe legacy) delivering to 60+ platforms `[inferred — seen in search results, page not fetched]`.

### 2.4 Outcomes and attribution

Max was more stable than HBO Max at launch — the explicit goal [C2-18] — and WBD's DTC segment turned profitable in 2024 `[folklore-level consensus]`, mostly from content amortization and pricing. What is attributable: a single-stack, single-leadership decision made within ~4 months of close produced a shippable combined product in 13 months — versus Disney's ~2019–2026 Hulu absorption — at the cost of the acquired side's engineering culture `[inferred]`. And the 2025 split shows the consolidation was product-level, not durable.

---

## 3. NBCUniversal / Peacock

### 3.1 Structure and how it changed

- **Jan 2019: NBCU–Sky partnership.** Peacock was built in ~12 months as a fully cloud-native AWS system by joint NBCU and Sky teams; the AWS case study quotes Sky's Director of Global OTT Platforms and Head of Group Reliability Engineering alongside Peacock's CTO Patrick Miceli [C2-28] `[documented]`. The UK team was the NOW TV team `[inferred — Variety's 2020 feature is paywalled; C2-28 independently confirms Sky-led engineering]`.
- **The "Global Streaming Platform."** Peacock rolled into six European markets on Sky's platforms in 2021 [C2-30] `[documented]`, and by 2024 Miceli was **CTO, Direct-to-Consumer and Global Streaming, at NBCUniversal *and* Sky**, running a platform across 70+ countries powering Peacock, SkyShowtime (Europe) and Showmax (Africa) [C2-29] `[documented]`. Sky's careers pages say Tech, Product & Data teams in Osterley and Leeds "collaborate with Comcast and NBCUniversal" on "Peacock to NOW," and sit "Across the EU. On both sides of the USA. And in India" [C2-31] `[documented]`. A real **shared platform org spanning two operating companies**, centered in the UK.
- **Data: centralization with explicit embedding (Jan 2023).** NBCU merged "research and decision sciences teams including applied analytics, **data engineering, and data science** into one portfolio-wide Television & Streaming organization" under Will Gonzalez, promoted from Peacock CDO to **EVP & Chief Data Officer**, reporting to chairman Mark Lazarus; Gonzalez had "created the decision sciences function within our Direct-to-Consumer business." Lazarus's memo says the research teams from Entertainment Networks, NBC Sports and Telemundo join the central org but "will remain **embedded with and equally accountable to** those businesses" [C2-33] `[documented]`. This is the only explicit public articulation of a **dual-accountability data model** in this set; the stated trigger was content windowing across networks and Peacock.
- **Ad-tech data is separate:** "One Platform" and the NBCUnified identity graph (200M person IDs) sit in Global Advertising & Partnerships under Krishan Bhatia [C2-36] `[documented]`. NBCU has *two* data orgs.
- **Jan 2026: Versant spin.** USA, CNBC, MSNBC, E!, Golf, Fandango and Rotten Tomatoes spun off; **Peacock, NBC, Bravo, studios and parks stayed** [C2-37] `[documented]`. `[inferred]` The 2023 cross-portfolio data org lost much of its network half three years later; nothing public on how it was divided.
- **Sky tech consolidation.** Sky cut ~1,000 jobs in 2024 and **600 technology roles** (London, Livingston, Leeds) in Sep 2025, "consolidating technology operations across its international presence" [C2-38] `[documented]` — `[inferred]` the platform is being rationalized as one org, not Sky-plus-Peacock parallel teams.

### 3.2 Central vs. embedded; where experimentation sits

Job postings only, so `[documented, thin]`: a "DTC Decision Sciences" team (NYC) owns ML for recommendations, content predictive modeling and MarTech [C2-35]; a **product analytics & experimentation team** (NYC) delivers "high quality analysis and well-designed experiments" for "product, design, engineering and editorial" across the full lifecycle — hypothesis, sample size, design, analysis [C2-34]; a separate "Ads Experimentation" role sits in ads `[inferred]`. Read: Peacock experimentation is an **analytics-side service function**, not a platform-engineering function as at Disney; the tooling presumably lives in the Sky/NBCU platform org, unconfirmed.

### 3.3 Global sites

- **UK (Osterley, Leeds):** the platform's engineering core — a **full platform-ownership** charter that predates the US product org [C2-28][C2-29][C2-31] `[documented]`.
- **India (Chennai):** the **Comcast India Engineering Center** "support[s] Comcast, NBCUniversal and Sky businesses," with recent work on frontline AI, syndication products, the Xfinity app and cybersecurity [C2-32] `[documented]`; its founding year and headcount are `[folklore]`. **No evidence of a Peacock- or NBCU-specific data/engineering site in Bangalore or Hyderabad**; CIEC is Comcast-wide and cable-centric.

### 3.4 Outcomes and attribution

Peacock reached scale (largest US live-streamed event, 2024 NFL wildcard; 300 live events/day at the 2024 Olympics [C2-29]) on a platform built in 12 months by a team that had already built NOW TV. That *is* plausibly structural — reusing an existing platform org rather than standing up a new one — and the platform's reuse for SkyShowtime and Showmax is the strongest "platform ownership at a non-HQ site works" datapoint in legacy media. Peacock's losses (~$2.8B peak in 2023 `[folklore-level consensus]`) are a rights story, not an org story.

---

## 4. Paramount (Paramount+, Pluto TV, BET+; CBS Interactive heritage)

### 4.1 Structure and how it changed

- **Heritage:** CBS Digital Media (2005) → CBS Interactive (2007) → CBS All Access [C2-41] `[documented]`. Viacom bought **Pluto TV** for $340M in 2019 mainly as a marketing funnel for linear brands; Pluto's engineering is in West Hollywood, Toronto and Berlin [C2-40] `[documented]`. CBS–Viacom merged Dec 2019; CBS All Access became Paramount+ on 4 Mar 2021 [C2-39] `[documented]`.
- **The non-decision (2019–2025):** Paramount "opted not to use Pluto TV's existing technology for Paramount Plus," leaving "two distinct technical systems" [C2-42] `[documented]`. By 2026 the three services "run on two different clouds with no connectivity between them" — separate recommendation engines, ad systems and data pipelines [C2-43] `[documented, trade reporting]`. CTO Phil Wiser (2018–2026) ran an enterprise "general compute" cloud migration (>95% cloud-native) and talked of making "technologies as disposable as we can" [C2-45][C2-44] `[documented]` — the streaming stacks stayed separate anyway.
- **Oct 2023: streaming reorg.** Deadline reported Paramount Streaming merged units and CPO Rob Gelick exited [C2-50] `[inferred — headline verified, article paywalled]`. `[inferred]` This is when Pluto and Paramount+ product/tech leadership combined under Tom Ryan (Pluto co-founder, CEO Paramount Streaming [C2-41]) — an org merger without a platform merger.
- **2024–2025: cuts and sale.** ~15% of US headcount (~2,000) cut in 2024 for $500M, including folding streaming distribution under the US networks distribution president [C2-46] `[documented]`; Skydance closed 7 Aug 2025 with a $2B synergy target; ~2,000 more layoffs began 29 Oct 2025 [C2-47] `[documented]`.
- **2026: consolidation, finally.** Pluto TV (and BET+) is migrating onto the **Paramount+** stack, targeted summer 2026, unifying infrastructure, **data, recommendations and ad tech**; "the company is reorganizing internal teams around key pillars like content, live streaming and monetization," with **no anticipated layoffs** [C2-42][C2-43] `[documented]`; Ellison called it a "soft merger" of back-ends with distinct front-ends [C2-39]. When Wiser left in May 2026 Paramount **did not replace the CTO**; his remit was split across the CIO and infrastructure, production-technology and security leads [C2-44] `[documented for the exit; the split is from a search summary — treat as inferred]`. The unified stack is explicitly the blueprint for absorbing HBO Max [C2-43] — now not before mid-2027 [C2-27].

### 4.2 Central vs. embedded; data

Ad-tech data: "EyeQ" (2020) is Paramount Advertising's unified digital video platform under John Halley [C2-48] `[documented]`. Streaming product data/experimentation: **no public record.** That data pipelines and recommenders were still separate per service in 2026 [C2-43] implies `[inferred]` data teams were embedded per-service through 2025 and are only now being centralized under the "monetization" and "content" pillars.

### 4.3 Global sites

**Essentially empty.** Paramount's India presence was Viacom18 (a JV, now Reliance's) and content/sales offices; **no evidence of a Paramount streaming or data engineering GCC in India** — searches across Bengaluru, Chennai, Hyderabad and Gurugram returned nothing company-specific. Pluto's Berlin and Toronto offices [C2-40] are the only documented non-US streaming engineering sites. SkyShowtime runs on the Sky/NBCU platform, not Paramount's [C2-29] `[documented]`.

### 4.4 Outcomes and attribution

The attributable outcome is negative: seven years of parallel stacks meant no cross-service personalization, unified ad targeting or shared data pipelines until 2026 [C2-43], and Paramount entered a $110B acquisition with its own house not yet unified. `[judgment]` Paramount is the strongest evidence here that **org consolidation without platform consolidation buys nothing** — the 2023 leadership merger produced no data or tech integration until a new owner forced it.

---

## 5. Cross-case patterns

| Dimension | Disney | WBD | NBCU/Peacock | Paramount |
|---|---|---|---|---|
| Streaming tech reports to | Content-business chairs (3-way), since 2023 | WBD CTO (ex-Discovery) → now in sale limbo | CTO DTC & Global Streaming, NBCU **and** Sky | Streaming CEO (Ryan); no group CTO since May 2026 |
| Stack consolidation after M&A | Slow absorption (Hulu → Disney+, 2019–2026) | Fast, acquirer-led, 13 months (2022–23) | N/A — built once on Sky, reused 3× | Deferred 7 years; forced 2026 |
| Product data/DS home | Inside P&T; data platform moved under **ad platform** Apr 2026 | Ad sales (Olli) + embedded; thin record | **Centralized CDO with explicit embedding** (2023) | Per-service until 2026; thin record |
| Experimentation | Central platform team + federated domains (2019–) | Unknown | Analytics-side service team (NYC) | Unknown |
| India charter | Full-market ownership (Hotstar) → divested to JV | **Capability/platform hub** (streaming, data/ML, ad-tech, enterprise data), 2023– | Comcast-wide CIEC (Chennai), cable-centric | None public |
| Europe charter | — | Warsaw HBO Max eng (legacy) | **Platform ownership** (UK) | Berlin/Toronto (Pluto) |

Three patterns hold across all four:

1. **Every data reorg was triggered by a P&L question, never a data question** — DMED (monetization), Disney 2023 (creative control), NBCU 2023 (windowing), Disney 2026 (ad measurement), Paramount 2026 (synergy target). `[documented]`
2. **Ad-tech data is always a separate org from product data**, and the two most recent moves (Disney 2026, Paramount 2026) pulled product data platforms *toward* monetization. `[documented]`
3. **Non-HQ sites hold durable charters when they own a platform or capability layer** (Sky/Peacock, WBD India), not a market whose economics can turn (Hotstar). `[inferred]`

---

## Implications for the decision

**On India-site charters in media companies specifically.** The public evidence is small but consistent. The one India site that had *full domain ownership* — Hotstar — owned a whole market's product, data and infrastructure, and that was exactly why it was separable: when the rights economics turned, the tech team drained to the competitor [C2-16] and the business was JV'd away [C2-15]. The one India site with a documented *capability charter* — WBD's Hyderabad/Bangalore/Pune hub covering data engineering, ML, applied DS, ad platforms and enterprise data [C2-22] — was stood up in four months during peak cost-cutting and has grown while US headcount fell. **[judgment]** For a US-led commerce/experimentation/data-platform org, the media precedent favors a **platform/capability charter first** (data platform, experimentation tooling, ad-data plumbing, QoE pipelines) with **graduating domain ownership** in domains that are stable and measurable (fraud, paid-sharing, QoE) rather than the ones most exposed to strategy swings (commerce packaging, funnels). NBCU's "part of the central org but embedded with and equally accountable to the business" wording [C2-33] is the best public template for how to phrase that dual accountability — it is the only one any of these companies bothered to write down.

**On integrating multiple stacks and orgs.** Three speeds are on display: WBD (fast, acquirer-led, culture loss), Disney (slow, six-year absorption, no headcount event), Paramount (deferred, then forced). **[judgment]** The Paramount case is the strongest evidence that merging leadership without merging data pipelines produces nothing measurable [C2-43]; the NBCU case is the strongest evidence that building on an existing platform org is faster than building a new one [C2-28]. For a reader converting India contractors to FTE, the analogous risk is the Hotstar one: contractor teams that own an isolated stack or an isolated domain are easy to lose and easy to cut. Converting to FTE **and** giving the site platform pieces that the US org depends on daily is what makes the site sticky in both directions.

**On central vs. embedded data teams.** Disney's Experiment-X is the only documented media example of central platform + federated execution, and its design goals — standardize metrics, remove reliance on analysts and engineers, support all partner apps — map directly onto this reader's experimentation and core-platform domains [C2-12]. NBCU centralized data engineering, DS and analytics under a CDO but kept embedding explicit [C2-33]. Disney then moved its data platform under ad-tech [C2-11]. **[judgment]** Expect the central-vs-embedded question to be re-decided by someone else every 2–3 years for P&L reasons; design the India charter to survive that — platform and tooling ownership survives reorgs, domain ownership follows the P&L. And the attribution limit is real: none of these companies has published outcome data tying structure to results, and every streaming P&L turn in 2023–2025 is better explained by pricing, password-sharing and content cuts than by any org chart.

---

## Sources

All URLs verified by fetch (WebFetch or browser) on 2026-08-29 unless marked otherwise. Tag = overall evidence quality of the source.

- **[C2-1]** The Walt Disney Company, "The Walt Disney Company Announces Strategic Reorganization of Its Media and Entertainment Businesses," press release, 12 Oct 2020. https://thewaltdisneycompany.com/press-releases/the-walt-disney-company-announces-strategic-reorganization-of-its-media-and-entertainment-businesses/ — accessed 2026-08-29. `[documented]`
- **[C2-2]** The Walt Disney Company, "The Walt Disney Company Announces Strategic Reorganization," press release, 14 Mar 2018. https://thewaltdisneycompany.com/press-releases/walt-disney-company-announces-strategic-reorganization/ — accessed 2026-08-29. `[documented]`
- **[C2-3]** Wikipedia, "Disney Media and Entertainment Distribution" (formation Oct 2020, Daniel exit Nov 2022, dissolution 8 Feb 2023, LaBerge role), 2026. https://en.wikipedia.org/wiki/Disney_Media_and_Entertainment_Distribution — accessed 2026-08-29. `[documented, tertiary — used for dates; underlying press coverage (Deadline/CNBC/THR Feb 2023) is paywalled to this agent]`
- **[C2-4]** Todd Spangler, "Disney and ESPN CTO Aaron LaBerge to Exit, Will Become Chief Technology Officer of Sports-Betting Company Penn Entertainment," Variety, 22 Apr 2024. https://variety.com/2024/tv/news/disney-espn-aaron-laberge-exit-penn-entertainment-1235978219/ — accessed 2026-08-29. `[documented]`
- **[C2-5]** The Walt Disney Company, "Disney Names Adam Smith Chief Product & Technology Officer, Disney Entertainment & ESPN," 15 Aug 2024. https://thewaltdisneycompany.com/news/adam-smith-disney-chief-product-technology-officer-entertainment-espn/ — accessed 2026-08-29. `[documented]`
- **[C2-6]** Todd Spangler, "Hulu on Disney+ Officially Launches, and Disney Will Go Harder With Bundle Upsell Pitches," Variety, 27 Mar 2024. https://variety.com/2024/digital/news/hulu-on-disney-plus-official-launch-bundle-1235952711/ — accessed 2026-08-29. `[documented]`
- **[C2-7]** Lauren Forristal, "Disney+ and Hulu content to combine into one streaming app later this year," TechCrunch, 10 May 2023. https://techcrunch.com/2023/05/10/disney-and-hulu-content-combine-into-one-app-later-this-year/ — accessed 2026-08-29. `[documented]`
- **[C2-8]** Todd Spangler, "Hulu App to Be Phased Out as Disney Is 'Fully Integrating' Service Into Disney+," Variety, 6 Aug 2025. https://variety.com/2025/digital/news/hulu-app-phased-out-disney-plus-fully-integrating-1236480450/ — accessed 2026-08-29. `[documented]`
- **[C2-9]** TechRepublic Staff, "Leaked Disney Document Points to Hulu App Shutdown After Disney+ Transition," TechRepublic, 29 May 2026 (reporting on Business Insider). https://www.techrepublic.com/article/news-hulu-app-shutdown-disney-transition/ — accessed 2026-08-29. `[documented, second-hand]`
- **[C2-10]** Lucas Manfredi, "Disney Cuts Staff in Product and Technology Division," TheWrap, 25 Jun 2025. https://www.thewrap.com/disney-product-technology-layoffs/ — accessed 2026-08-29. `[documented]`
- **[C2-11]** Matthew Keys, "Disney shakes up streaming executive team following key departure," The Desk, 27 Apr 2026. https://thedesk.net/2026/04/disney-streaming-shake-up-arora-leaving/ — accessed 2026-08-29. `[documented — based on an internal memo; single outlet]`
- **[C2-12]** Diana Jerman (with Mark Harrison, Anmeen Leong, Michael Ramm), "Disney Streaming Embraces 3 Key Tenets of Experimentation," Disney Streaming engineering blog (Medium), 4 Jan 2022. https://medium.com/disney-streaming/disney-streaming-embraces-3-key-tenets-of-experimentation-b20bb34c7ad4 — accessed 2026-08-29 (via browser; blocks automated fetch). `[documented]`
- **[C2-13]** Databricks, "Learn How Disney+ Built Their Streaming Data Analytics Platform with Databricks and AWS," Databricks blog (Martin Zapletal, Software Engineering Director, Disney+), 14 Dec 2020. https://www.databricks.com/blog/2020/12/14/learn-how-disney-built-their-streaming-data-analytics-platform-with-databricks-and-aws-to-improve-the-customer-experience.html — accessed 2026-08-29. `[documented, vendor]`
- **[C2-14]** Snowflake, "How Disney Streaming Uses the Data Cloud for Data Governance and Data Sharing" (Anita Lynch, VP Data Governance), 13 Jul 2021. https://www.snowflake.com/en/blog/how-disney-streaming-uses-the-data-cloud-for-data-governance-and-data-sharing/ — accessed 2026-08-29. `[documented, vendor]`
- **[C2-15]** Wikipedia, "Disney+ Hotstar" (Hotstar-platform basis; JioStar JV Nov 2024; JioHotstar 14 Feb 2025), 2026. https://en.wikipedia.org/wiki/Disney+_Hotstar — accessed 2026-08-29. `[documented, tertiary]`
- **[C2-16]** The Core / The Signal newsletter, "The shift in Hotstar's North Star," 24 Feb 2023. https://newsletter.thesignal.co/p/hbo-disney-ipl-jio-viacom-hotstar-4c5a — accessed 2026-08-29. `[inferred — single trade newsletter quoting an unnamed executive]`
- **[C2-17]** ByteByteGo, "How Disney Hotstar (now JioHotstar) Scaled Its Infra for 60 Million Concurrent Users," 18 Nov 2025 (summarizing two JioHotstar Engineering Blog posts, "Scaling Infrastructure for Millions" Parts 1–2). https://blog.bytebytego.com/p/how-disney-hotstar-now-jiohotstar — accessed 2026-08-29. The underlying blog (https://blog.hotstar.com/) was confirmed to exist as a Medium publication but its article pages did not render for this agent. `[documented, secondary]`
- **[C2-18]** Lauren Forristal, "Warner Bros. Discovery CTO and CPO explain how they made Max less buggy," TechCrunch, 5 May 2023. https://techcrunch.com/2023/05/05/warner-bros-discovery-cto-and-cpo-explain-how-they-made-max-less-buggy/ — accessed 2026-08-29. `[documented]`
- **[C2-19]** Amanda Silberling, "Layoffs hit HBO Max as 70 employees lose their jobs," TechCrunch, 15 Aug 2022. https://techcrunch.com/2022/08/15/layofs-hbo-max-discovery/ — accessed 2026-08-29. `[documented]`
- **[C2-20]** Variety, "Warner Bros. Discovery to Lay Off Nearly 1,000 Employees, Cuts to Max Staffers in Single Digits," Jul 2024. https://variety.com/2024/tv/news/warner-bros-discovery-lays-off-1000-employees-finance-max-1236074169/ — accessed 2026-08-29 (browser; article body partially truncated in capture). `[documented]`
- **[C2-21]** Warner Bros. Discovery, "Warner Bros. Discovery Announces 'Olli,' New First-Party Data Platform Powering Converged Audience Solutions," 25 Apr 2024. https://www.wbd.com/warner-bros-discovery-announces-olli-new-first-party-data-platform-powering-converged-audience-solutions — accessed 2026-08-29. `[documented]`
- **[C2-22]** Warner Bros. Discovery Careers, "India Innovation Hub" (Bangalore, Hyderabad, Pune; listed charters). https://careers.wbd.com/global/en/india-innovation-Hub — accessed 2026-08-29. `[documented, recruiting copy]`
- **[C2-23]** Telangana Today, "Warner Bros. Discovery to set up International Development Centre in Hyderabad," 17 May 2023. https://telanganatoday.com/warner-bros-discovery-to-set-up-development-centre-in-hyderabad — accessed 2026-08-29. `[documented]`
- **[C2-24]** Telangana Today, "Warner Bros. Discovery's Hyderabad Capability Centre inaugurated," 20 Sep 2023. https://telanganatoday.com/warner-bros-discoverys-hyderabad-capability-centre-inaugurated — accessed 2026-08-29. `[documented]`
- **[C2-25]** BusinessofGCC, "Warner Bros. Discovery GCC in Hyderabad — Global Capability Center Profile," updated 18 Mar 2026. https://www.businessofgcc.com/gcc-data/companies/warner-bros-discovery-india-hyderabad — accessed 2026-08-29. `[folklore — directory estimates; conflicts with C2-23/24 on founding date]`
- **[C2-26]** Warner Bros. Discovery, "Warner Bros. Discovery to Separate into Two Leading Media Companies," 9 Jun 2025. https://www.wbd.com/news/warner-bros-discovery-separate-two-leading-media-companies — accessed 2026-08-29. `[documented]`
- **[C2-27]** Wikipedia, "Proposed acquisition of Warner Bros. Discovery by Paramount Skydance" (Netflix Dec 2025; Paramount $31/share 27 Feb 2026; shareholder vote 23 Apr 2026; DOJ 12 Jun 2026; state-AG trial Mar 2027; outside date 1 Jun 2027), 2026. https://en.wikipedia.org/wiki/Proposed_acquisition_of_Warner_Bros._Discovery_by_Paramount_Skydance — accessed 2026-08-29. `[documented, tertiary]`
- **[C2-28]** Amazon Web Services, "Peacock Case Study" (quotes Patrick Miceli, Eric Black, Stephen Hildebrand of Peacock; Keith Davidson and Colin Innes of Sky), 2020. https://aws.amazon.com/solutions/case-studies/peacock-case-study/ — accessed 2026-08-29. `[documented, vendor]`
- **[C2-29]** Comcast Corporation, "Peacock's CTO Patrick Miceli Talks Exclusive NFL Wildcard Game, Olympics and The Future of Streaming," 3 Sep 2024. https://corporate.comcast.com/stories/peacock-cto-patrick-miceli-nfl-wildcard-game-olympics-future-of-streaming — accessed 2026-08-29. `[documented, corporate]`
- **[C2-30]** Jeff Baumgartner, "Peacock's global streaming strategy takes flight with Sky," Light Reading, 29 Jul 2021. https://www.lightreading.com/video-broadcast/peacock-s-global-streaming-strategy-takes-flight-with-sky — accessed 2026-08-29. `[documented]`
- **[C2-31]** Sky Careers, "Leeds" and "Sky Group HQ | Osterley" location pages (Tech, Product & Data teams; Peacock and NOW; "And in India"). https://careers.sky.com/locations/leeds and https://careers.sky.com/locations/osterley — accessed 2026-08-29. `[documented, recruiting copy]`
- **[C2-32]** Comcast Careers, "Comcast India Engineering Center (CIEC) Jobs and Careers in Asia." https://jobs.comcast.com/asia — accessed 2026-08-29. `[documented, recruiting copy]`
- **[C2-33]** Jennifer Maas, "NBCU Merges Research, Data Science Ops Across All TV and Streaming Divisions Under Peacock's Will Gonzalez," Variety, 11 Jan 2023 (includes Mark Lazarus's full memo). https://variety.com/2023/tv/news/nbcu-research-data-science-peacock-will-gonzalez-promotion-1235486146/ — accessed 2026-08-29. `[documented]`
- **[C2-34]** NBCUniversal job posting via WayUp, "Manager, Product Experimentation, Peacock" (New York). https://www.wayup.com/i-j-NBCUniversal-448809240288921/ — accessed 2026-08-29. `[documented, job posting]`
- **[C2-35]** Peacock job posting via ShowbizJobs, "Director of Data Science, Decision Science" (New York; closed Jul 2022). https://www.showbizjobs.com/jobs/peacock-director-of-data-science-decision-science-in-new-york/jid-rezn47 — accessed 2026-08-29. `[documented, job posting]`
- **[C2-36]** NBCUniversal Together, "NBCUniversal's One Platform Hits Key Operational Milestones…," 16 Nov 2022. https://together.nbcuni.com/insights/news/one-platform-hits-key-operational-milestones/ — accessed 2026-08-29. `[documented, corporate]`
- **[C2-37]** Joe Cornell, "Comcast Completes Spin-Off Of Versant Media Group," Forbes, 6 Jan 2026. https://www.forbes.com/sites/joecornell/2026/01/06/comcast-completes-spin-off-of-versant-media-group/ — accessed 2026-08-29. `[documented]`
- **[C2-38]** Matthew Keys, "Comcast's Sky to eliminate 600 tech jobs amid streaming shift," The Desk, 16 Sep 2025. https://thedesk.net/2025/09/comcast-sky-job-cuts-uk/ — accessed 2026-08-29. `[documented]`
- **[C2-39]** Wikipedia, "Paramount+" (CBS All Access rebrand 4 Mar 2021; Ellison "soft merger" statement Aug 2025), 2026. https://en.wikipedia.org/wiki/Paramount%2B — accessed 2026-08-29. `[documented, tertiary]`
- **[C2-40]** Wikipedia, "Pluto TV" (Viacom acquisition 2019; West Hollywood/Toronto/Berlin; 2026 unified stack), 2026. https://en.wikipedia.org/wiki/Pluto_TV — accessed 2026-08-29. `[documented, tertiary]`
- **[C2-41]** Wikipedia, "Paramount Streaming" (CBS Digital Media/CBS Interactive lineage; Tom Ryan), 2026. https://en.wikipedia.org/wiki/Paramount_Streaming — accessed 2026-08-29. `[documented, tertiary]`
- **[C2-42]** Matthew Keys, "Paramount moving forward with plan to consolidate Pluto TV, Paramount Plus technical stack," The Desk, 11 Jun 2026. https://thedesk.net/2026/06/paramount-pluto-tv-drm-technical-stack-merger/ — accessed 2026-08-29. `[documented]`
- **[C2-43]** Cristian Dina, "Paramount is merging Pluto TV, BET+, and Paramount+ onto one tech stack to prepare for HBO Max," The Next Web, 10 Jun 2026. https://thenextweb.com/news/paramount-streaming-tech-stack-pluto-tv-hbo-max — accessed 2026-08-29. `[documented, no named sources]`
- **[C2-44]** Makenzie Holland, "Paramount CTO steps down," CIO Dive, 18 May 2026. https://www.ciodive.com/news/paramount-cto-steps-down/820515/ — accessed 2026-08-29. `[documented]`
- **[C2-45]** Joao-Pierre S. Ruth, "Paramount CTO on Shedding Legacy Systems for General Compute," InformationWeek, 6 Jun 2024. https://www.informationweek.com/it-leadership/paramount-cto-on-shedding-legacy-systems-for-general-compute — accessed 2026-08-29. `[documented]`
- **[C2-46]** Todd Spangler, "Paramount Consolidation of U.S. TV and Streaming Distribution Teams Results in Staff Cuts," Variety, 11 Dec 2024. https://variety.com/2024/tv/news/paramount-tv-streaming-distribution-layoffs-1236246417/ — accessed 2026-08-29. `[documented]`
- **[C2-47]** Associated Press via CBS News, "Paramount to lay off 2,000 workers shortly after merging with Skydance," 29 Oct 2025. https://www.cbsnews.com/news/paramount-layoffs-merger-skydance/ — accessed 2026-08-29. `[documented]`
- **[C2-48]** Paramount Global, "Paramount Global Announces Worldwide Expansion of 'EyeQ'," PR Newswire, 1 Nov 2023. https://www.prnewswire.com/news-releases/paramount-global-announces-worldwide-expansion-of-eyeq-301973757.html — accessed 2026-08-29. `[documented, corporate]`
- **[C2-49]** Wikipedia, "Discovery+" (US launch 4 Jan 2021; Europe 5 Jan 2021 subsuming Dplay and Eurosport Player; Max 23 May 2023), 2026. https://en.wikipedia.org/wiki/Discovery%2B — accessed 2026-08-29. `[documented, tertiary]`
- **[C2-50]** Deadline, "Paramount Streaming Reorg: Chief Product Officer Rob Gelick Out As Streamer Merges Units," Oct 2023. https://deadline.com/2023/10/paramount-streaming-restructure-pluto-1235582992/ — **headline and URL verified via search only; article body paywalled to this agent and the domain blocked in the browser.** Cited only for the fact of the reorg and Gelick's exit. `[inferred]`

### Not verified / not cited

- Variety's 2020 Peacock launch feature (Sky/NOW TV team built Peacock) — paywalled; the claim is independently supported by C2-28.
- CNBC/Deadline/THR coverage of the Feb 2023 Disney reorg — paywalled/blocked; dates and rationale taken from C2-3 and the Disney press releases.
- Fast Company on the Hulu/Disney+ integration ("70,000 titles encoded differently") — blocked; not cited.
- WBD Warsaw "HBO Max DTC Technology organization" careers page and WBD India job titles — seen in search results only; flagged `[inferred]` in text.
- Technology Magazine piece on NBCU's VP Engineering, Data & Personalization (Manoj Yerrasani) — blocked; not cited.
- Hotstar engineering headquartered in Bangalore; CIEC founded 2005 with 1,000–5,000 staff; Paramount CTO duties split four ways; Dane Glasgow as Paramount CPO — all seen in search summaries, not primary-verified; flagged `[folklore]`/`[inferred]` inline.
- Any primary source stating Max runs on the Discovery+ backend — none found; flagged `[folklore]`.
- Any Paramount or Disney streaming data/engineering site in India post-2024 — none found.
