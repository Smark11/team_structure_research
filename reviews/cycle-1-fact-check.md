# Cycle 1 — Fact-check and citation audit (Reviewer B)

Date: 2026-08-30. Scope: `docs/*.html` (six content pages + `sources.html`), `research/sources.json`, research reports C1–C5. Companion file: `reviews/cycle-1-url-check.tsv` (all 216 URLs, keyed by the `sources.html` number, with the `sources.json` index alongside).

Note on numbering: citation numbers on the pages are the `docs/sources.html` `s-N` ids, which are **not** the `sources.json` array order (page [1] = Disney+ Hotstar/Wikipedia; `sources.json` #1 = "Analytics at Netflix"). Every source number below is the page/`sources.html` number.

## Summary

| Check | Result |
|---|---|
| URLs checked | 216 (every entry in `sources.json`; 1:1 match with `sources.html`) |
| Resolve (2xx, or 4xx on HEAD but 200 on GET) | 190 |
| Bot-blocked (403/429/402/405 with a browser UA; not broken) | 24 — Netflix TechBlog ×6, Medium ×2, ACM DL ×5, INFORMS ×4, ScienceDirect, ResearchGate, ir.netflix.net, LinearB ×3, Variety (Tollbit 402) |
| Broken | 1 — #175 Cambridge (HTTP 500). Replacement verified (200). |
| Unreachable, verify manually | 1 — #43 McKinsey spans-of-control PDF (000/timeout for PDF *and* article page; mckinsey.com blocks automated clients, so possibly not dead) |
| Claims sampled (all six pages; every numeric claim on index.html) | 68 |
| SUPPORTED | 41 |
| PARTIALLY supported (number/wording/date off, or clause beyond the source) | 17 |
| NOT SUPPORTED by the cited source (claim or quotation absent) | 6 |
| WRONG SOURCE (claim is true but the citation points at a source that lacks it) | 4 |
| Evidence tags to downgrade | 14 (B12–B25) |
| Uncited or mis-cited factual sentences found by manual walk | 9 (B26–B34) |
| Freshness flags | 4 (B35–B38) |

Blocking items: **B1–B11**. The three headline numbers the brief asked about — 27% / 56%, 2.5×, 86% precision — are supported. JPMorgan 55,000, Zurich ~5,000 / ~18 years, WBD hub figures, the Disney April 2026 move, the Zinnov/EY attrition figures and every Spotify quotation check out. The failures are concentrated in the GCC market-size numbers on Charter Evidence, one pay-premium figure on the Recommendation page, the Hotstar 59M figure, three quotations that no cited source contains, and ~14 claims whose `documented` tag is more confident than the research reports themselves were.

---

## Part 1 — URL resolution

Full table: `reviews/cycle-1-url-check.tsv` (columns: sources_html_no, sources_json_index, http_status, url, verdict).

- 190 OK. Five URLs return 404/405 to HEAD but 200 to GET (#52 TNW, #127 and #203 Thoughtworks, #102 Amazon, #116 ShowbizJobs) — fine for readers.
- 24 bot-blocked: #13, #17, #21, #22, #23, #25, #44, #46, #47, #54, #55, #56, #74, #121, #124, #129, #151, #152, #153, #166, #183, #208, #209, #210. These open in a browser; not broken. Note that `sources.json` already records several of these as "read via browser" or "metadata only" (see Part 3).
- #175 (Cambridge, *Trustworthy Online Controlled Experiments*): HTTP 500 on HEAD and GET, and via WebFetch. **Fix:** replace with `https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59` (200; it is also where `https://doi.org/10.1017/9781108653985` resolves). Update `sources.json` index 144 and `sources.html#s-175`.
- #43 (McKinsey spans-of-control PDF): connection times out (000) for the `/~/media/...` PDF and for the article page `https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/how-to-identify-the-right-spans-of-control-for-your-organization`, from curl with a browser UA and from WebFetch. Web search was unavailable in this session to locate a mirror. **Fix:** open in a browser; if the PDF is live, keep it but add the article-page URL as the primary link (the `/~/media` path is a CDN path that McKinsey has moved before); if dead, cite the article page or an archive.org capture. Until confirmed, this is the one primary-source link on the site that a reader cannot follow.
- Two URLs resolve but do not point at the work cited: #36 Thompson *Organizations in Action* → a 2017 anniversary commentary PDF (amsacta.unibo.it); #133 Urwick HBR 1956 → the Wikipedia "Span of control" article. Both are honest in the `sources.json` notes but the `sources.html` entries present them as the primary work (see B25, B32).

---

## Part 2 — Claim–source fidelity (68 claims)

Method: each claim was checked against the cited page (WebFetch, or local text extraction for PDFs). Where the source is bot-blocked (Netflix TechBlog, Medium, Variety, ACM/INFORMS abstracts) the research report's description of what it read is used and the row says so. "Index" = index.html; "CS" = case-studies.html; "CE" = charter-evidence.html; "F" = foundations.html; "A" = applying-it.html; "LP" = learning-plan.html.

| # | Page · claim | Cited | Verdict | Note |
|---|---|---|---|---|
| 1 | Index/CE: ~27% of India centres reach Portfolio Hub within five years | 7 | SUPPORTED | Zinnov page: "The compression curve: 27% reach Portfolio Hub in 5 years". |
| 2 | Index/CE: 56% of centres are execution shops; ladder 13/43/39/5 | 7 | SUPPORTED | 13% + 43% on the Zinnov page. |
| 3 | CE: 2,117 GCCs, 3,728 units, 2.36M, $98.4B FY26 | 7 | SUPPORTED | Verbatim on page. |
| 4 | CE: 1,700 centres / 1.9M / $64.6B two years earlier; 6,500+ global roles 2024 | 154 | SUPPORTED | Report page confirms (FY2024). |
| 5 | CE: "110–120 new centers open every year" | 38, 155 | **NOT SUPPORTED** | #38: "~110 new GCCs" between early 2024 and late 2025 (≈2 years). #155 (EY): "more than 120 set up since January 2023" (≈3 years). Both give ~40–60/yr, not 110–120/yr. → B1 |
| 6 | CE: "35% of the population was set up in the last two years" | 38, 155 | **NOT SUPPORTED** | #38: "35% of *Mid-market* GCCs established in the last 2 years". Not the population. → B1 |
| 7 | Index/CE/F/A: cross-site work items took ~2.5× as long; more people per item | 14 | SUPPORTED | Herbsleb & Mockus abstract: "about two and one-half times as long"; mechanism = more people involved. The herbsleb.org PDF is a scanned image (CCITT), so C5's "text-verified" is optimistic, but the finding is correct. |
| 8 | Index/F/A: Nagappan 2008 org metrics ≈86% precision / 84% recall, beating churn, complexity, coverage, dependencies | 23 | SUPPORTED | 86.2% / 84.0% in the paper. The TR-2008-11 PDF text could not be machine-extracted for the figure; ACM abstract blocked. Accept on C3 + paper. |
| 9 | Index/F/CE/A: Bird 2009 — negligible failure difference, distributed vs collocated | 13 | SUPPORTED (blocked) | CACM/ACM blocked; C3 documented; matches the paper's abstract. |
| 10 | Index/CE: JPMorgan ~55,000 in India | 4 | SUPPORTED | Outlook Business 23 Jul 2026: "around 55,000 people across five Indian cities". |
| 11 | Index: JPMorgan "technology solutions, business and functional support" (quoted) | 4, 10, 26 | **WRONG SOURCE** | Quote is in #158 (JPMorgan 2023 release), not #4. CE cites 158 correctly. → B29 |
| 12 | CS/Index: Zurich ~5,000, "largest headquarters of the YouTube development team alongside … San Bruno"; ~18 years | 53 | SUPPORTED | Page: ~5,000; quote verbatim; "active in Zurich since 2004" (2004→2022 = 18 yrs, derived). |
| 13 | CS: Zurich "still does not own the analytics function" tagged documented | 53 | PARTIAL | Source says nothing about analytics; C1 tagged this clause inferred. → B14 |
| 14 | Index/CE: Hotstar 25M (25.3M 2019) concurrent | 1 | SUPPORTED | Wikipedia: 25.3M, 2019 CWC semi-final. |
| 15 | Index/CE: Hotstar "later 59 million" / "~59M in 2023" | 1 | **NOT SUPPORTED** | Not in the Wikipedia article as fetched. #111 (ByteByteGo) says "over 61 million" / "60 million". → B5 |
| 16 | Index/CS/CE: Hotstar platform reused for Disney+ in SE Asia, Israel, South Africa, MENA; built on Hotstar's own infrastructure | 1 | SUPPORTED | Wikipedia confirms all four regions and Iger's "take advantage of Hotstar's existing infrastructure". |
| 17 | Index/CS/CE: "Hotstar lost a considerable portion of its technology team" | 3 (and 1) | SUPPORTED, single anonymous source | The Signal, 24 Feb 2023, "an industry executive" unnamed. #3 is tagged inferred; CE tags the sentence documented. → B15 |
| 18 | CS/CE: JioStar Nov 2024, Reliance 63.16% / Disney 36.84%, JioHotstar 14 Feb 2025 | 1 | SUPPORTED | Verbatim. |
| 19 | Index/CE: Target "ownership of outcomes rests with where the center of gravity for the capability sits" (quoted) | 15 | PARTIAL (misquote) | Source: "ownership of outcomes **resting** with where the center of gravity for the capability sits". → B31 |
| 20 | Index: Target "from IT support in 2005 … over about fifteen years" | 15, 31, 26 | PARTIAL | 2005 and "IT capabilities to support the US headquarters" are in #159 (ANSR), not #15; "about fifteen years" appears nowhere — the source is a 2026 interview ("over 21 years"). → B30 |
| 21 | CE: Target 5,700+, ~40% technology, half of new store designs, 80% of remodels, co-located Business/Tech/Product/Data/UX | 15 | SUPPORTED | All verbatim in GCC Pulse. |
| 22 | Index/CE: Lowe's opened Feb 2015, ~500, "one team, multiple locations" (MD Narayan Ram) | 31 | SUPPORTED | PR Newswire 11 Feb 2015. |
| 23 | Index/CE: Lowe's 5,000+, India VPs for Applied AI/Data & Analytics, Omnichannel Platforms, Engineering Platforms, product management, SVP who is CTO and MD | 26 | SUPPORTED | lowes.co.in lists Amit Kapur, Rahul Chokhani, Arun Padmanabhan; Ankur Mittal "SVP, CTO and Managing Director". Index's "VPs owning applied AI and data platforms" is a loose gloss (the platform VP is "Engineering Platforms"). |
| 24 | Index/CS: Disney moved Data Product & Engineering under Tony Donohoe (EVP ad platform), April 2026; CDI alliance dissolved; Atlas; ~1,000 cut | 35 | SUPPORTED | The Desk 27 Apr 2026 confirms all, with 1,000 in a linked companion story. |
| 25 | CS: "…under new CEO Josh D'Amaro" tagged documented | 35 | PARTIAL | CEO not named in the cited article. → B16 |
| 26 | Index/CS/CE: WBD hub "fundamental to building our global technology platforms…"; charters list; Bangalore/Hyderabad/Pune | 10 | SUPPORTED | Verbatim on careers page. |
| 27 | CS/CE: WBD IDC announced 17 May 2023 after minister met SVP Finance; 1,200 in year one; inaugurated 20 Sep 2023 with CFO Wiedenfels; "first Greenfield office in Asia after the merger" | 114, 86 | SUPPORTED | Both Telangana Today pieces confirm. |
| 28 | Index/CE: attrition 18–25% for "data and AI" roles, 18–24-month tenures | 45 | PARTIAL | Zinnov: "In AI and **Cloud** roles specifically, attrition runs between 18–25%"; tenure 18–24 months. "Data" is the site's substitution. → B33 |
| 29 | CE: Zinnov 15.4→13.3→15.1→16%; high-performer 16.5% | 45 | SUPPORTED | Verbatim. |
| 30 | CE: EY 13→11→9%; ~800 avg headcount; 52% shared accountability; 26% consulted; 63% AI/ML; 54% DE/BI | 157 | SUPPORTED | All in the EY release. |
| 31 | CE: ~80% of centres have <10% of leadership roles in India; 77% mid-senior from 63% | 29 | SUPPORTED | VARINDIA (citing EY). |
| 32 | CE: 'second-line managers "who can own outcomes… without constant escalation to the country head"' attributed to Zinnov | 29 | **WRONG SOURCE / quote unlocated** | Attributed to Zinnov but cited to VARINDIA (EY-derived); the fetched VARINDIA page paraphrases the idea but the quoted words were not found there or in #33. → B9 |
| 33 | Index: comp bands "15–40% above IT-services bands at mid-senior levels" | 40 | **NOT SUPPORTED** | HRKatha: "25 to 40 per cent". EY release (#157) and Storyboard18 (#155) contain no premium figure. A already says 25–40%. → B2 |
| 34 | CE: GCC hikes 9.8% avg, AI/ML 21.1%, cyber 20%, NLP 19.2%, top performers 17.2%; niche ~1.7×; Bengaluru 14.3% / Chennai 8.2%; tier-II 10–15% lower | 45, 165 | SUPPORTED | All on the Zinnov June 2026 post; 1.7× on #165. |
| 35 | CE: Infosys 12.9 / TCS 12.3 / Wipro 14.5, Q2 FY25 | 167 | SUPPORTED | |
| 36 | CE: ~80k roles lost at top-5 IT services over 18 months to mid-2025 | 40 | SUPPORTED | |
| 37 | CE: "GCCs +200k FY26 vs IT services +110k" | 40 | PARTIAL (unverified) | HRKatha fetch shows "510,000 professionals in 2026"; the 200k/110k pair was not located. Verify or soften. |
| 38 | CE: two-thirds of Mega GCC heads technical, many dual mandates; six cities 92%; 6,500 → 30,000 by 2030 | 38 | SUPPORTED | Verbatim. |
| 39 | Index/CE/A: "first three hiring decisions shape the center more than the next ninety-seven combined"; centres past 100 with no permanent head; 7:1–8:1 | 33 | SUPPORTED | Verbatim. |
| 40 | Index/CE: Forrester 2007 ">60% … struggling"; expat-going-home pattern | 30 | SUPPORTED | Forrester summary page. |
| 41 | CE: Citi→TCS Oct 2008 (~$505M), Wipro 2009, AXA 600 → Capita, AOL/Aviva/Prudential/Philips; four analyst reasons | 27, 156 | SUPPORTED | CIO 2009 confirms all but the price (price is #156, "verified via search index only"). |
| 42 | Index: "Citi's captive was sold to TCS after a decade as support" | 27 | PARTIAL | "after a decade" not in either source. |
| 43 | Index/CE: Martorelli "simply transfer all of their best people"; Borowski "stagnant with marginal improvements"; Everest 452 in 2023, ~50 sold of 1,450 | 5 | SUPPORTED | Verbatim (CIO, 29 Feb 2024). |
| 44 | Index/CS/CE: Sky 600 tech roles, London/Livingston/Leeds, Sep 2025 | 6 | SUPPORTED | |
| 45 | CS: Sky "cut ~1,000 jobs in 2024" | 6 | **NOT SUPPORTED** | The Desk says ~3,000 since 2023 incl. 2,000 call-centre jobs in 2025; no 2024/1,000 figure. → B7 |
| 46 | CS: Sky "consolidating technology operations across its international presence" (quoted) | 6 | PARTIAL (misquote) | Source: "consolidating some technology operations across its international footprint". → B31 |
| 47 | CS: Stone joined 2020, CTO Oct 2023, CPTO Feb 2026 over "product, engineering and data teams"; Peters quote; after CPO departure | 74, 75 | SUPPORTED | Variety AU confirms (Eunice Kim, Sept 2025). |
| 48 | CS: Warsaw ~300 staff, "only technology hub outside of the United States", infra/gaming/production tech | 8 | SUPPORTED | |
| 49 | CS: "In January 2023 Netflix announced its first engineering hub outside the US" | 73 | PARTIAL | The 2023 release does not say "first"; #8 (2026) supports it. Add 8. |
| 50 | CS: Spotify Jan 2023 ~6%, Söderström CPO "majority of our engineering and product work", "2X"; Dec 2023 ~17%, Ek quotes ×3; Ek never names squads | 77, 78 | SUPPORTED | All verbatim. |
| 51 | CS: Spotify 2013 ABBA; 2017 hack week (flags, ~25% event volume, notebooks, bucket ranges); 2018 platform + Metrics Catalog | 50 | SUPPORTED | |
| 52 | CS: 64% learning rate vs 12% win rate; engagement team "center of excellence for internal customer success"; "adding experiment reviewers" | 20 | SUPPORTED | |
| 53 | CS: 58 teams, 520 experiments on mobile home; separate stacks by API | 101 | SUPPORTED | |
| 54 | CS: Kniberg 2015, Ivarsson 2016, Lee 2020 + Sundén quotations | 99, 100, 48 | SUPPORTED | All verbatim; Sundén correctly flagged second-hand. |
| 55 | CS: Kniberg/Ivarsson 2012 whitepaper — ~30 squads, 3 cities, "smaller than 100 people or so", disclaimer, "metrics and A/B testing" | 76 | SUPPORTED (from the paper; PDF text not extractable) | |
| 56 | CS: NBCU 2023 "embedded with and equally accountable to"; Gonzalez EVP & CDO reporting to Lazarus; windowing trigger | 42 | SUPPORTED (blocked) | Variety is behind Tollbit (402); C2 read the memo. |
| 57 | CS: Vogels — "more than 25 databases…", Galaxy 2019 by finance ops, Andes/EDX | 51 | SUPPORTED | |
| 58 | CS: Bryar & Carr via Schuler — "biggest predictor… not whether it was small"; "somebody's part-time job" | 102, 24 | SUPPORTED (secondary) | Quotes on the Product Leadership page; book not read. Tag question → B21. |
| 59 | CS: Hyderabad campus 15,000 seats, AWS/Kindle/Alexa/Amazon.in/Home Services, Agarwal quote, retail entry 2013 | 63 | SUPPORTED | |
| 60 | CS: Prime Video job — "technical backbone…"; Bengaluru "spanning across X-Ray, playback services, live technologies, player and client testing"; "guide global Prime Video teams on architecture decisions" | 9 | PARTIAL (last quote not verbatim) | Page says "work with other global Prime Video teams" and "provide the needed engineering and architecture guidance". → B31 |
| 61 | CS: Disney DMED 12 Oct 2020 "P&L management and all distribution… data and technology functions worldwide"; DTCI Mar 2018; Adam Smith Aug 2024 from YouTube, "data scientists" in org, triple reporting line | 81, 82, 64 | SUPPORTED | Press releases confirm. "BAMTECH (technology and digital products center)" wording not confirmed in the 2018 release, minor. |
| 62 | CS: Paramount — "opted not to use Pluto TV's existing technology" / "two distinct technical systems"; two clouds; summer 2026; "reorganizing internal teams around key pillars like content, live streaming and monetization"; no layoffs | 94, 52, 93 | PARTIAL | Two clouds, mid-/summer-2026 and no-layoffs confirmed. The "key pillars" quotation and the "opted not to use Pluto TV's technology" wording were not found in the fetched #94 or #52. → B8 |
| 63 | CS: "Paramount did not replace the CTO" (documented); remit split (inferred) | 95 | PARTIAL | CIO Dive reports the exit only; says nothing about replacement. → B17 |
| 64 | CS: Skydance closed 7 Aug 2025 "with a $2B synergy target"; ~2,000 layoffs from 29 Oct 2025 | 96 | PARTIAL | CBS/AP confirms 2,000 and 29 Oct; no $2B figure. → B28 |
| 65 | CS: WBD split into "Streaming and Studios" and "Discovery Global (CNN, Discovery, Discovery+)" | 87 | PARTIAL | June 2025 release names the second company "Global Networks"; "Discovery Global" is a later rename not in the cited source. |
| 66 | CS: Paramount $110.9B on 27 Feb 2026; vote 23 Apr; DOJ 12 Jun; 12 state AGs, trial Mar 2027; outside date 1 Jun 2027 | 88 | SUPPORTED | Wikipedia confirms every date. "HBO Max… not before mid-2027" is not in #88 or #52 → B18. |
| 67 | F: Graicunas 5→100, 6→222, max five/probably four; 1933; Urwick 1956 disclosed helping | 132, 133 | PARTIAL | All of it is on the Nickols page (#132); none of it is on the Wikipedia page (#133), which is cited for the Urwick quote and the disclosure. → B32 |
| 68 | F: Larson — six to eight; grow to 8–10 then bud into 4–5; "never more than eight"; hands-on managers "three to five"; teams <4 "transitory"/"exploratory"; "cavalier in ignoring the downsides" | 41, 136, 137 | PARTIAL | 6–8, bud, never-more-than-eight confirmed. "Three to five" is not in the 2018 post (it says <4 directs = Tech Lead Manager); the words "transitory", "exploratory" and "cavalier" were not found on the post. They may be in *An Elegant Puzzle* (#137). → B23 |

Additional spot checks that passed with no issue (not tabulated): Google Ananta "from India, for the world" (#2); Netflix Mumbai page lists no engineering (#162); Amazon "Built for India, scaled globally" (#163); Walmart India and 20,000+ WGT / Chennai 2021 (#49, #160); ANSR 2005 (#159); Storyboard18 IT attrition (#167); CIO 2011 Aase "did not retain valuable skills and knowledge" (#164); Comcast CIEC page (#71); Sky Leeds page (#70); Light Reading six markets (#91); Comcast Miceli 70+ countries / 300 live events a day / biggest US live-streamed event (#11); One Platform 200M IDs (#68); AWS Peacock case study names (#90); Olli on Snowflake clean rooms (#67); TechCrunch Max 12 months / 20% faster / four CDNs / no "Discovery+ stack" claim (#85); HBO Max 70 / 14% (#112); TheWrap "<2%" (#110); TechRepublic leaked memo and walk-back (#109); DMED Wikipedia dates (#83); Pluto $340M / offices (#72); Paramount+ 4 Mar 2021, Ellison "soft merger" Aug 2025 (#93); Paramount Streaming lineage (#117); Kohavi "director of data mining and personalization… responsible for Weblab" (#62); AWS two-pizza quotes (#61); Outlook Prime Video India reporting lines, vacancy since July 2024 (#104); Spotify data platform 1.4T / three areas (#57); Confidence "hundreds of squads", "<20 priority experiments" (#58); London hub April 2019 and hub list (#59); Echo Nest (#12); Databricks Kinesis/Flink (#65); Snowflake "single copy of data", Anita Lynch VP Data Governance (#66); WayUp and ShowbizJobs postings (#69, #116); Zinnov 2024 report (#154); DeepMind 20 Apr 2023 quotes (#79); Zurich 2017 (#80); KDD paper — "March 2007" deployment and the experiment-council sentence found in the PDF text (#19); Olson & Olson four concepts found in the PDF text (#46); Thoughtworks Radar Trial July 2014 (#127); Fowler bliki 20 Oct 2022 (#169); Blank 2015 definition (#140); Larson organizational-risk definition (#139); Larson four states (#138); Larson reorg tests and 7-step sequence (#136); DORA loosely-coupled capability page incl. mainframe sentence (#141); DORA 2023 user-centric / code review / generative culture (#142); dbt "works for 10 people… Beyond that, we don't know" and "What, exactly, should be centralized…" (#122); Kaminsky factors (#123); Data Business Partnership HRBP analogy (#143); Thoughtworks 2026 mesh retrospective failure modes (#131); Kwan (#150); TVP wiki-page example (#28); Remote Team Interactions Workbook both quotes (#39); Team Topologies 2e 23 Sep 2025 with new cross-industry cases (#34); DX Priceline Ep. 111 (#192); Macomber 16 Jul 2026 (#197); Iyer 30 Jul 2026 (#198); Pragmatic Engineer AMA 8 Jul 2026 (#194); SE Radio 646, 11 Dec 2024 (#204); Elided Branches post list (#182); lethain August 2026 posts (#171); Miller 1956 is about memory (#134); Project Oxygen page has no span figure (#135).

---

## Part 3 — Numbered findings

Severity: **blocking** = wrong/fabricated claim, broken primary URL, or factual claim with no supporting citation; **major** = mis-tagged or partially supported; **minor** = wording.

### Blocking

**B1 · blocking · charter-evidence.html §5.1 "The base rates", sentence 2 (cites 38, 155)**
Finding: "Something like 110–120 new centers open every year, and 35% of the population was set up in the last two years." Neither number is in the cited sources. #38 (Zinnov) says "~110 new GCCs were established in India" between early 2024 and late 2025, and "35% of Mid-market GCCs established in the last 2 years". #155 (EY via Storyboard18) says "more than 120 set up since January 2023". The annual rate is roughly half what the page states, and the 35% applies to mid-market centres only. The same error is in C5 §1 ("Roughly 110–120 new GCCs are set up per year"), so the fix is upstream too.
Fix: replace with "Zinnov counts about 110 new centres opened between early 2024 and late 2025, EY more than 120 since January 2023 — roughly 50 a year — and 35% of mid-market centres were set up in the last two years.<sup>38 155</sup>" Also fix CE §5.4 "new mid-market GCCs (35% set up in the last two years)" — that one is already correctly scoped; leave it.

**B2 · blocking · index.html §1.3 Phase 0, last sentence (cites 40); charter-evidence.html §5.1 paragraph 3 and the talent table row "GCC pay premium" (cites 157, 40)**
Finding: "15–40% above IT-services bands at mid-senior levels". The cited HRKatha piece says "25 to 40 per cent"; the EY release (#157) and Storyboard18 (#155) contain no premium figure at all. applying-it.html already says 25–40% citing the same source, so the site contradicts itself. C5 §2 is the origin of "15–40%".
Fix: index → "25–40% above IT-services bands at mid-senior levels.<sup>40</sup>"; charter table cell → "25–40%" with the caveat "EY GCC Pulse 2025 via secondary reporting (HRKatha)"; delete "the same reporting also cites 25–40%"; charter §5.1 → "GCCs now pay 25–40% above IT services at mid-senior levels".

**B3 · blocking · sources.html #175 / sources.json index 144 (Kohavi, Tang & Xu)**
Finding: URL returns HTTP 500. Fix: `https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59` (verified 200; DOI 10.1017/9781108653985). Learning-plan.html #175 inherits the fix via the build.

**B4 · blocking (pending manual check) · sources.html #43 / sources.json index 108 (McKinsey spans of control)**
Finding: both the `/~/media/...pdf` path and the article page time out for every automated client tried. This is the sole source for the five-archetype span table used on foundations.html §3.6 and applying-it.html §4.5. Fix: confirm in a browser; switch the primary URL to `https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/how-to-identify-the-right-spans-of-control-for-your-organization` (keep the PDF as a secondary link); if both are dead, use an archive.org capture and say so in the note. Add the archetype ranges to the `sources.json` note so the claim survives link rot.

**B5 · blocking · index.html §1.2a first sentence; charter-evidence.html Hotstar card (both cite 1)**
Finding: "later 59 million concurrent viewers" / "~59M in 2023" is not in the Wikipedia article as fetched (it lists 18.6M and 25.3M for 2019). The 2023 Cricket World Cup peak exists but is only in #111 (ByteByteGo: "over 61 million", headline "60 Million"). Fix: "…scaled to 25 million (2019) and about 60 million (2023 Cricket World Cup) concurrent viewers<sup>1 111</sup>"; same on the charter card ("25.3M in 2019, ~60M in 2023<sup>1 111</sup>").

**B6 · blocking · case-studies.html Fig. 2.2 caption**
Finding: "Zurich<sup>53 80</sup>; Hotstar<sup>13</sup>." #13 is Bird et al., *Does Distributed Development Affect Software Quality?* — nothing to do with Hotstar. Fix: "Hotstar<sup>1 3</sup>".

**B7 · blocking · case-studies.html §2.7 "How it changed and why", last sentence (cites 6)**
Finding: "Sky cut ~1,000 jobs in 2024 and 600 technology roles…" The Desk article contains no 2024/1,000 figure; it says Sky has cut ~3,000 positions since 2023 including 2,000 from call-centre closures earlier in 2025. Fix: "Sky has cut about 3,000 positions since 2023, including 2,000 call-centre roles earlier in 2025, and in September 2025 announced 600 technology roles (London, Livingston, Leeds) while 'consolidating some technology operations across its international footprint'<sup>6</sup>". (C2 §3.1 carries the same unsupported 2024 figure.)

**B8 · blocking · case-studies.html §2.8 "How it changed and why", "Consolidation, finally" paragraph (cites 94, 52, 93)**
Finding: the quotation "the company is reorganizing internal teams around key pillars like content, live streaming and monetization" was not found in #94 (The Desk) or #52 (TNW) as fetched, nor in #93. Also "opted not to use Pluto TV's existing technology for Paramount Plus" and "two distinct technical systems" (earlier paragraph, cites 94) were not found verbatim; The Desk says Paramount "opted instead to simply relaunch CBS All Access under the Paramount Plus name". Fix: either locate the pillars sentence (it may be in the TNW body the fetch summarised) and cite only the source that contains it, or drop the quotation marks and paraphrase: "Paramount says it is regrouping teams around content, live and monetization". For the first quote, use The Desk's actual wording.

**B9 · blocking · charter-evidence.html §5.4 "Leadership seeding" (cites 29)**
Finding: 'Zinnov's sharpest scarcity call is second-line managers "who can own outcomes… without constant escalation to the country head."' The sentence attributes the quote to Zinnov but cites #29 (VARINDIA, which reports EY's GCC Pulse). The quoted words were not found on the VARINDIA page (it paraphrases: centres "remain dependent on escalating decisions to top leadership") or on Zinnov #33. Fix: "EY's 2025 survey, as reported by VARINDIA, names the missing layer as second-line managers who can run complex teams without escalating to the country head<sup>29</sup>; Zinnov's version is the 7:1–8:1 candidate ratio and hiring 'across the pyramid'<sup>33</sup>." Drop the quotation marks unless the exact words are found. The talent-table row "Mid-to-senior share… second-line managers are the binding constraint<sup>29 33</sup>" is fine.

**B10 · blocking · foundations.html §3.9, Stancil sentence (cites 146)**
Finding: "he has separately argued that data mesh is 'delegated', not decentralized, because a central authority still sets standards" — #146 ("Disband the analytics team") does not discuss data mesh, and no other source in the list contains this quotation. C3 §8 asserts it without a citation. Fix: delete the clause, or add the specific Stancil post that says it (not identified in this review) and cite that.

**B11 · blocking · foundations.html §3.9, dbt sentence (cites 122, 144); sources.html/sources.json #144 metadata**
Finding: "Handy's version is central platform, 'data expertise everywhere'." #144 ("Data teams: embedded or centralized? Reactive or self-directed?") is by **Anna Filippova**, not Tristan Handy, and does not contain the quoted phrase; its thesis is to build data culture through systems rather than move people between embedded and central seats. `sources.json` lists the author as "Handy, T." Fix: (a) sources.json index 127 / sources.html #144 author → "Filippova, A."; (b) rewrite: "the dbt Roundup's answer is to stop moving people between central and embedded seats and build the systems that make either work<sup>144</sup>" and drop the quotation. Also foundations.html §3.9 "Locally Optimistic … 'Data Business Partnership'" is fine (Adam Stone, 2022).

Also blocking by the rubric's "wrong claim" test: **B22** below (DORA 2023 / platform engineering) — listed under tags because it is a one-clause fix.

### Major — evidence-tag downgrades (task 3)

**B12 · major · case-studies.html §2.0 para 3 and §2.3 "Global sites"**
Zurich "…and still does not own the analytics function<span documented>" (cites 53). #53 says nothing about analytics; C1 marked the clause "documented + inferred". Downgrade that clause to `inferred`. (The Fig. 2.2 right-column note carries the same claim untagged — add `inferred`.)

**B13 · major · case-studies.html §2.8 "How it changed and why"**
"When Wiser left in May 2026 Paramount did not replace the CTO<span documented>" (cites 95). CIO Dive reports the exit only. Downgrade to `inferred` (C2 itself: "documented for the exit; the split is from a search summary — treat as inferred").

**B14 · major · case-studies.html §2.8, same paragraph**
"The unified stack is explicitly the blueprint for absorbing HBO Max, now not before mid-2027<span documented>" (cites 52, 88). #52 says the WBD deal is expected to close in Q3 (2026); #88 gives an outside date of 1 June 2027. "Not before mid-2027" is the site's inference and conflicts with #52. Change to "…absorbing HBO Max once the WBD deal closes — expected Q3 2026, with a 1 June 2027 outside date<sup>52 88</sup>" and tag `inferred` for any timing beyond that.

**B15 · major · charter-evidence.html Hotstar card**
'"Hotstar lost a considerable portion of its technology team" … <span documented><sup>3 1</sup>'. #3 is a single anonymous-source trade newsletter and is tagged `inferred` in sources.html; index.html and case-studies.html correctly tag the same sentence `inferred`. Downgrade to `inferred`.

**B16 · major · case-studies.html §2.5 "How it changed and why"**
"…all during a ~1,000-person cut under new CEO Josh D'Amaro<span documented><sup>35</sup>". The Desk article does not name the CEO. Either add a source for D'Amaro's appointment or drop the name; keep `documented` only for what #35 says.

**B17 · major · charter-evidence.html §5.4 "The distributed-work research" and foundations.html §3.10**
Cummings, Espinosa & Pickering "(108 teams, 22 countries) found that time-zone separation hurts performance more than spatial separation<span documented><sup>25</sup>"; Ramasubbu & Balan "dispersion 'significantly reduces development productivity'<span documented><sup>166</sup>"; Carmel & Agarwal tactics "<span documented><sup>16</sup>". `sources.json` notes for #203/#204 say "findings via search summary" and for #133 "metadata verified via Semantic Scholar only"; the ACM/INFORMS abstracts were blocked in this review too. Either fetch the abstracts in a browser and record it in the note, or tag these three sentences `inferred`. The 108/22 figures in particular should not be stated as verified until someone has read the abstract.

**B18 · major · case-studies.html §2.4 "Structure"**
"Bryar and Carr's Working Backwards records the correction… <span documented>; this record has the book only through a secondary summary.<sup>102 24</sup>" — the sentence admits the book was not read. Tag `inferred` (or `documented` with the citation limited to #24, the page that was actually read and contains the quotes).

**B19 · major · case-studies.html §2.6 "Structure" and "Global sites"**
"'Olli'… sits in Digital Ad Sales under Ryan Gould<span documented><sup>67</sup>" — the release quotes Gould as Head of Digital Ad Sales but does not state where Olli sits organisationally; tag the placement `inferred`. "Warsaw carries an 'HBO Max DTC Technology organization'… seen in search results only<span inferred><sup>10</sup>" — #10 is the India hub page and does not mention Warsaw; either add the Warsaw careers page as a source or remove the citation so the sentence is visibly unsourced.

**B20 · major · sources.html tags on tertiary/vendor/secondary sources presented as primary**
`documented` is used for Wikipedia (#1, #72, #83, #88, #89, #93, #117, #133, #161), vendor case studies (#65 Databricks, #66 Snowflake, #90 AWS, #159 ANSR "vendor marketing"), secondary summaries (#24 Product Leadership; #109 TechRepublic reporting on Business Insider; #111 ByteByteGo), a retail page standing in for a book (#102), and sources verified only via search index (#156) or summary page (#30, #165). The `sources.json` notes already say "Tertiary", "Vendor", "Secondary", "Verified via search index only"; the rendered `sources.html` shows the note text for some but the tag pill still reads `documented`. Recommend a fourth pill state or a visible qualifier ("documented · tertiary", "documented · vendor") so that page-level `documented` tags resting solely on these (index §1.2a Hotstar, CE Hotstar card, CS Paramount lineage, CS Disney data platform) are honest. Where Wikipedia is the *only* source for a consequential claim (index §1.2a; Fig 2.2), add the underlying primary (Disney/Star India press releases) or tag `inferred`.

**B21 · major · foundations.html §3.7 Larson (cites 41, 137)**
Quoted words "transitory", "exploratory", "cavalier in ignoring the downsides" and the "hands-on technical managers three to five" range were not found in the 2018 post (#41). They may be in *An Elegant Puzzle* (#137). Cite the book for those and the post only for 6–8 / bud / "never more than eight"; otherwise remove the quotation marks. applying-it.html §4.5 repeats "three to five directs if hands-on" citing 41, 136 — same fix.

**B22 · major (wrong clause) · foundations.html §3.8 (cites 142)**
"The 2023 report … treats platform engineering as a first-class topic." The 2023 DORA report page lists user focus, code review speed, culture, reliability, flexible infrastructure and AI; platform engineering was the 2024 report's headline topic. Delete the clause or cite the 2024 report.

**B23 · major · foundations.html §3.4 Cataldo (cites 129)**
"modification-request resolution time falls by roughly a third" — abstract blocked; C3 gives "~30%" without a page reference. Verify against the ESEM 2008 paper or soften to "falls significantly".

**B24 · major · foundations.html §3.6 Urwick (cites 133)**
The Urwick quotation and "disclosed he had helped Graicunas write the 1933 paper" are cited to #133, whose URL is the Wikipedia *Span of control* article; the disclosure is on the Nickols page (#132) and the quotation is from Urwick's HBR article, which was not fetched. Cite 132 for the disclosure; for the quotation either cite Nickols if it reproduces it, or mark the source as "quoted in secondary sources".

**B25 · major · sources.html #36 (Thompson) and #133 (Urwick)**
The entries present a 2017 commentary volume and a Wikipedia page as the primary works. Add "via:" wording in the visible entry (the `sources.json` note for #133 already says "Verified via secondary sources"; #36 has no note).

### Major — coverage: uncited or mis-cited factual sentences (task 4)

**B26 · major · index.html §1.2c and §1.6c**
"Target went from IT support in 2005 to an 'integrated global headquarters' over about fifteen years" (cites 15, 31, 26). The 2005 start and "IT capabilities to support the US headquarters" are in #159 (ANSR), not #15; "about fifteen years" is nowhere. Fix: "…from IT support in 2005<sup>159</sup> to an 'integrated global headquarters' over roughly two decades<sup>15</sup>" (the interview is titled "21 Years"). §1.6c "the celebrated cases took ten to fifteen" → "ten to twenty".

**B27 · major · index.html §1.2b, first sentence (cites 4, 10, 26)**
The JPMorgan quotation "technology solutions, business and functional support" is from #158. Add 158.

**B28 · major · case-studies.html §2.8 "How it changed and why" (cites 96)**
"$2B synergy target" is not in the CBS/AP piece. Add a source (Paramount Skydance's August 2025 investor materials) or delete the figure. Same paragraph: "more than 95% cloud-native" (cites 119) was not confirmed by the InformationWeek fetch — verify.

**B29 · major · case-studies.html §2.2 "Global sites" (cites 59, 12)**
"Spotify lists Bangalore, Gurgaon and Mumbai among its offices" — neither cited source is the locations page. Add `https://www.lifeatspotify.com/locations` (C1 read it) to sources and cite it.

**B30 · major · case-studies.html §2.3 "Structure"**
"Data-science roles are titled by product area ('Data Scientist, Product,' 'Data Scientist, Core Compute,' 'Business Data Scientist, gTech')… ML engineering sits under software engineering<span inferred>." Tagged inferred but has no source at all for the job titles. Either cite Google Careers listings or reduce to "Google publishes nothing about YouTube's data org; job titles suggest…" with the `inferred` tag and no specifics in quotation marks.

**B31 · minor · misquotations (three places)**
(a) index.html §1.1 and charter-evidence.html Target card: "ownership of outcomes rests with…" → source reads "ownership of outcomes resting with where the center of gravity for the capability sits" — either quote exactly or move the quotation marks to start at "where". (b) case-studies.html §2.7: "consolidating technology operations across its international presence" → "consolidating some technology operations across its international footprint". (c) case-studies.html §2.4 "Global sites": "guide global Prime Video teams on architecture decisions" is not on the posting; use "provide the needed engineering and architecture guidance" and "work with other global Prime Video teams".

**B32 · minor · case-studies.html §2.6 (cites 87)**
"Discovery Global (CNN, Discovery, Discovery+)" — the June 2025 release names it "Global Networks"; the rename came later. Write "Global Networks (later renamed Discovery Global)" or add the rename source.

**B33 · minor · index.html §1.5 tripwire month 12 (cites 45, 5)**
"Data and AI roles already run 18–25% attrition" → source says "AI and Cloud roles". Write "AI and cloud roles — the closest published proxy for data roles — run 18–25%…".

**B34 · minor · learning-plan.html §6.5 "Dropped or could not verify"**
Checkable factual statements with no citation: Monday Morning Data Chat ended; leaddev.com/podcast 404s; PriorityZero's last episode 13 Jan 2025; skamille.medium.com returns 403. The section is labelled judgment but these are facts; add `data-cite="none"` deliberately or cite the pages checked. Also index.html §1.2b "Citi's captive was sold to TCS after a decade as support" — "after a decade" is in neither #27 nor #156; drop it or source it.

### Minor — dates and freshness (task 5)

**B35 · minor · index.html §1.4 and applying-it.html §4.6 vs foundations.html §3.9**
Netflix's data org is "ten times this org's scale" (index, applying-it) and "roughly thirty times this org's scale" (foundations). Neither is sourced (the analytics-engineering post body is 403). Pick one figure, mark it `judgment`, or remove the multiplier.

**B36 · minor · index.html §1.4 (cites 44, 21)**
"the Netflix shape, which … still keeps platform, metric definitions and experiment review central" — present tense resting on a 2020 post and a January 2022 post. Add "as of its 2020–2022 posts" or cite the May 2026 "Data Projects" post (already in sources #183 note) for the platform half.

**B37 · minor · foundations.html §3.9**
"Mode's 'pulmonary model' rotates analysts…" — the Mode post is December 2015 and attributes the model to Clare Corthell. Write "a 2015 Mode post, crediting Clare Corthell, describes a 'pulmonary model'…". Likewise "Locally Optimistic's 'One Size Fits None' says…" is 2018 and "Data Business Partnership" is 2022 — fine, but the section's present tense ("The practitioner canon converges…") should carry one dated anchor.

**B38 · minor · case-studies.html §2.2 "Structure" (cites 56) and §2.7 "Global sites" (cites 70, 71)**
Spotify Product Insights post is undated Medium (the Medium mirror C1 saw dates it ~2018) — say "an undated (c. 2018) Spotify Insights post"; Sky and Comcast careers pages are undated recruiting copy used in present tense — the text already says "careers pages say", which is adequate; add "(page undated, accessed 2026-08-29)" in sources.html for #70/#71.

### Minor — housekeeping

**B39 · minor** · applying-it.html §4.2 Test 1 cites "<sup>14 14</sup>" (duplicate); charter-evidence.html evidence table cites "<sup>10 10</sup>" for WBD. Dedupe in the build.
**B40 · minor** · case-studies.html §2.1 "Global sites": add #8 to the "first engineering hub outside the US" sentence (the 2023 release does not say "first"; the 2026 one says "only").
**B41 · minor** · foundations.html §3.4: "Thoughtworks' (Leroy and Simons, 2010…)" — the Radar page (#127) does not name them; Fowler's bliki (#169) does. Add 169.
**B42 · minor** · case-studies.html §2.5 "How it changed and why": "with 7,000 cuts" is cited to the Wikipedia DMED page (#83); the fetch did not show the figure. Cite Disney's 8 Feb 2023 earnings release or verify the Wikipedia text.
**B43 · minor** · sources.json #131/C5 "PDF fetched and text-verified" for Herbsleb & Mockus: the herbsleb.org PDF is a CCITT scan with no text layer; the claim is correct but the verification note overstates what was done. Add the DOI landing page (10.1109/TSE.2003.1205177) as the citable abstract.

---

## What did not reproduce a problem (for the record)

- Every direct quotation from Spotify (Kniberg 2012/2015, Ivarsson 2016, Lee 2020, Sundén via Lee, Söderström/Ek 2023, Rydberg 2020, Bellato et al. 2025, Zhao & Schultzberg 2026) is verbatim.
- Every Netflix quotation could not be fetched (403) but matches C1's transcriptions; the Stone timeline and Peters quote are verbatim in Variety AU.
- All Disney press-release quotations (2018, 2020, 2024) and the April 2026 memo details are verbatim; the "Hulu tech stack and app will be decommissioned" leak and Disney's walk-back are as described.
- WBD hub dates, headcount and both Telangana Today quotations; the WBD careers-page charters and quotation; TechCrunch Max interview; HBO Max 70/14%.
- NBCU/Peacock: AWS case-study names, Miceli title/70+ countries/300 events a day, One Platform 200M IDs, six European markets, CIEC page, Sky Leeds page.
- Paramount: all deal dates in #88, Pluto $340M and offices, 4 Mar 2021, Ellison "soft merger", Oct 29 2025 layoffs, Wiser exit.
- All Zinnov/EY/HRKatha/Storyboard18 figures except those in B1, B2; all CIO 2009/2011/2024 and Forrester 2007 quotations.
- The KDD 2010 "March 2007" deployment and the experiment-council sentence were found in the PDF text; Olson & Olson's four concepts were found in the UCI PDF text.
