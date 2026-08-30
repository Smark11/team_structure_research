# Cycle 2 — Fact-check and citation audit (Reviewer B)

Date: 2026-08-30. Scope: the rebuilt `docs/*.html`, `research/sources.json`, `docs/sources.html`; every cycle-1 fix (B1–B43) re-opened; ≥ 30 new or rewritten claims re-checked against their sources; second-pass evidence-tag audit; coverage walk of the regions `tools/check-citations.py` exempts; genericization check.

Source numbers below are the `docs/sources.html` `s-N` numbers as rendered on the pages (they changed from cycle 1; e.g. cycle-1 #38 Zinnov "5 shifts" is now [43]).

## Summary

| Check | Result |
|---|---|
| Cycle-1 fixes verified (B1–B43) | 43 opened: **39 applied and correct**, **4 partially applied** (B21, B26, B31, B34) — listed as B2-1 … B2-3 and B2-14 |
| B4 McKinsey article page | **Opens in a browser** (Chrome; WebFetch and curl still time out). All five archetype ranges are on the page: player/coach 3–5, coach 6–7, supervisor 8–10, facilitator 11–15, coordinator 15+. (The page itself mislabels the facilitator line "The typical managerial span for a supervisor is 11 to 15" — McKinsey's typo, the site's reading is right.) |
| URLs changed since cycle 1 | 2 of 216 — [48] McKinsey (article page; 200 in browser) and [163] Cambridge (200). No other `url` differs from `cycle-1-url-check.tsv`. |
| "Consulted, not cited" section | s-204 … s-216 are genuinely uncited on every page (grep). s-107 (TechRepublic) is also uncited but sits inside the cited list — B2-23. |
| New / rewritten claims checked | 47 (index "In two minutes", drill-downs 1.2a–e, T1–T12, phases 0–3; Applying It cost, sensitivity and matrix; Charter Evidence §5.1, §5.4, §5.5, cards; Foundations §3.4–3.7, §3.10; Case Studies Sky, Paramount, WBD, Prime Video, Fig 2.1 alt table 12 rows) |
| SUPPORTED | 35 |
| PARTIAL | 6 |
| NOT SUPPORTED / WRONG SOURCE | 6 (B2-4, B2-5, B2-7, B2-8, B2-9, B2-10) |
| Evidence tags to downgrade (second pass) | 3 (B2-12, B2-13) — the rest of the `documented`-on-qualified-source cases are press-release-backed Wikipedia dates, vendor case studies quoting the company, or recruiting copy the page already labels as such: accepted |
| `check-citations.py` | OK (pages 7, sources 216, cited ids 202, no dangling refs). Manual walk of exempt regions: one caption missing a citation (B2-22), one tripwire with an unsupported factual clause (B2-10); everything else in `<details>`, `<desc>`, alt tables, rails and table cells is assumption/judgment text under a visible judgment label. |
| Genericization | Clean. No employer named; every "we/our" is inside a quotation or is the memo's own voice ("we say so"); "this reader's domains" (Case Studies, Disney) is generic. |

Blocking items: **B2-1 to B2-7**. Four of the seven are one-line fixes (a misquote, a citation pointer, a missing `data-cite`, a stray clause); two are unsupported numbers/claims that must be rewritten (B2-4 the +200k/+110k pair; B2-5 the Herbsleb 2025 "confirms the finding has held"); one is a citation attached to sources that do not contain the claim (B2-7).

The headline numbers the brief asked about all re-verify against their cited pages: 55,000 (Outlook Business, verbatim "around 55,000 people across five Indian cities"; the 1,000 roles in "cloud architecture, cybersecurity and AI data pipelines" and the 2M sq ft Mumbai campus for ~30,000 by 2029 are also on that page); 56/44 and 13/43/39/5 (Zinnov page); 27% — the page says "The compression curve: 27% reach Portfolio Hub in 5 years" and **gives no method**, so the site's "the method behind that figure is not published" is correct on both pages where it appears (index 1.2c, CE §5.1); 86% (Nagappan, cycle 1); 2.5× (Herbsleb & Mockus, cycle 1); 25–40% (HRKatha verbatim "25 to 40 per cent"); two decades / ten years (Target 2005→2026 interview titled "21 Years"; Lowe's 2015→2025); 18–25% "AI and cloud roles" (Zinnov, now correctly labelled on index T2); 7:1–8:1 and "first three hiring decisions" (Zinnov [36]); Sky 600 (The Desk); Disney April 2026 (The Desk). The Paramount "regrouping teams around content, live and monetization" paraphrase that cycle 1 could not locate **is** in The Desk [116] ("reassigning employees … around several 'thematic pillars,' including content, live streaming and monetization") — B8 is fully applied. The NBCU "embedded with and equally accountable to" quotation was verified in cycle 1 against the Lazarus memo in Variety [47]; it is used on index Phase 2, Applying It §4.3 and §4.6 with the same wording and the same citation.

---

## Part 1 — Verification of cycle-1 fixes

| # | Fix | Status | Where checked |
|---|---|---|---|
| B1 | ~110 (2024–25) / >120 since Jan 2023 / ~50 a year / 35% of mid-market | **Applied** | CE §5.1 sentence 2, cites [43 146] (Zinnov 5-shifts; Storyboard18/EY) — correct sources |
| B2 | 25–40% everywhere | **Applied** | index Phase 0 [45]; CE §5.1 and talent table; Applying It §4.5 and cost table [45] |
| B3 | Cambridge URL | **Applied** | sources.json idx 144 → `…/D97B26382EB0EB2DC2019A7A7B518F59`, HTTP 200; DOI in note |
| B4 | McKinsey primary → article page; ranges in note | **Applied and confirmed in browser** | sources.json idx 108; note carries the five ranges; page opened in Chrome and the ranges match |
| B5 | Hotstar 59M removed | **Applied** (numbers removed rather than re-cited; CE card now says "record concurrency" with no figure) | index 1.2a, 1.6a; CE Hotstar card |
| B6 | Fig 2.2 caption Hotstar → [1 27] | **Applied** | case-studies Fig 2.2 caption |
| B7 | Sky sentence to the Desk's figures | **Applied** | CS §2.8 "How it changed": 3,000 since 2023; 2,000 call-centre 2025; 600 tech Sept 2025 |
| B8 | Paramount quotations | **Applied** | CS §2.9: "opted instead to simply relaunch CBS All Access under the Paramount Plus name" [116] verbatim; "regrouping teams around content, live and monetization" — paraphrase, and the wording is in [116] |
| B9 | EY-via-VARINDIA attribution | **Applied** (one citation gap, B2-18) | CE §5.4 Leadership seeding |
| B10 | Stancil data-mesh clause | **Applied** (deleted) | Foundations §3.9 |
| B11 | Filippova author; quotation dropped | **Applied** | sources.json idx 213 "Filippova, A." with note "Author corrected in review"; Foundations §3.9 no longer cites it; entry now in "Consulted, not cited" |
| B12 | Zurich analytics → inferred | **Applied** (sentence now garbled, B2-16) | CS §2.4 Global sites; Fig 2.2 text "analytics function not documented as Zurich-owned (inferred)" |
| B13 | Paramount CTO non-replacement | **Applied** (sentence removed) | CS §2.9 |
| B14 | HBO Max timing | **Applied** | CS §2.7 and §2.9: "expected Q3 2026 by one report, with a 1 June 2027 outside date [40 94]" — TNW says "expected in the third quarter" |
| B15 | Hotstar drain → inferred on CE | **Applied** | CE Hotstar card and §5.6 table (a) |
| B16 | D'Amaro dropped | **Applied** | CS §2.6 |
| B17 | Cummings / Ramasubbu / Carmel → inferred | **Applied on CE and Foundations** (index still `documented`, B2-13) | CE §5.4; Foundations §3.10 |
| B18 | Bryar & Carr via Schuler | **Applied** | CS §2.5: "as summarized by Schuler … {inferred} [9]" |
| B19 | Olli placement inferred; Warsaw sentence | **Applied** (Olli "appears to sit in ad sales {inferred}"; the WBD-Warsaw sentence was removed) | CS §2.7 |
| B20 | Visible qualifier on Sources page | **Applied** ("tertiary", "vendor", "secondary", "index only", "summary only", "metadata only", "recruiting copy", "blocked; title-level", "via secondary") — one mis-derived qualifier, B2-15 | sources.html |
| B21 | Larson book vs post | **Applied on Foundations** ([46] for 6–8/bud/"never more than eight"; [132] for "three to five", "transitory", "exploratory", "cavalier"); **not applied on Applying It §4.5** — B2-2 | Foundations §3.6, §3.7; Applying It §4.5 |
| B22 | DORA platform-engineering clause | **Applied** (deleted) | Foundations §3.8 |
| B23 | Cataldo "significantly" | **Applied** | Foundations §3.4, §3.11, principle 5 |
| B24 | Urwick disclosure → Nickols; quote "quoted in secondary sources" | **Applied** | Foundations §3.6 cites [128 129]; quotation line reads "Urwick, 1956, quoted in secondary sources. [129]" |
| B25 | "Via" wording on Thompson and Urwick | **Applied** | [41] "Via a 2017 anniversary commentary volume"; [129] "Quoted via secondary sources (Nickols; Wikipedia)" |
| B26 | Target 2005 → ANSR; "roughly two decades"; "ten to twenty" | **Applied on index** (1.2c [34] … "over roughly two decades"; 1.6c "ten to twenty years"; Fig 1.1 "10–20 years"); **CE still says "reached after ~15 years" and "10–15 years" twice** — B2-14 | index; CE Target card, §5.6 |
| B27 | JPMorgan quotation → [28] | **Applied** | index 1.2b |
| B28 | "$2B synergy" and ">95% cloud-native" | **Applied** (both deleted) | CS §2.9 |
| B29 | Spotify India-offices clause | **Applied** (dropped; hub list cites [62 15]) | CS §2.3 Global sites |
| B30 | Google job titles | **Applied** (no quoted titles; `inferred`) | CS §2.4 Structure |
| B31 | Three misquotations | **(b) and (c) applied**; **(a) applied on index only** — CE Target card still reads "rests with" — B2-1 | index 1.1 pull quote "resting"; CS §2.8 "consolidating some technology operations across its international footprint"; CS §2.5 Prime Video "provide the needed engineering and architecture guidance" / "work with other global Prime Video teams" |
| B32 | "Global Networks (later renamed Discovery Global)" | **Applied in prose**; timeline table row still says "Discovery Global" for June 2025 — B2-17 | CS §2.7; Fig 2.1 alt table |
| B33 | "AI and cloud roles — the closest published proxy" | **Applied** | index T2 (one table label still says "data", B2-20) |
| B34 | LP dropped list `data-cite="none"`; Citi "after a decade" | **Index clause removed**; **`data-cite="none"` is not present anywhere in learning-plan.html** (the items are `<li>`, which the script does not inspect, so it passes by accident) — B2-3; the same "after a decade" clause survives on CE §5.6 — B2-6 | learning-plan.html §6.5; CE §5.6 table (b) |
| B35 | "An order of magnitude larger" | **Applied** | index 1.4; Applying It §4.6, Fig 4.2 caption; Foundations §3.9 |
| B36 | "as of its 2020–2022 posts" | **Applied** | index 1.4 |
| B37 | Mode 2015 / Corthell | **Applied by removal** (the Mode sentence was cut with the §3.9 trim) | Foundations §3.9 |
| B38 | Undated notes | **Applied** ("An undated (c. 2018) Spotify Insights post"; [74] [75] "Page undated recruiting copy; accessed 2026-08-29") | CS §2.3; sources.html |
| B39 | Duplicate citations | **Applied** (build collapses runs; no `N N` pairs found) | all pages |
| B40 | [10] added to "first engineering hub" | **Applied** | CS §2.2 Global sites [10 79] |
| B41 | Fowler bliki for Leroy & Simons | **Applied** | Foundations §3.4 [123 124] |
| B42 | "7,000 cuts" | **Applied** (dropped) | CS §2.6 |
| B43 | Herbsleb DOI in note | **Applied** (note: "abstract at DOI 10.1109/TSE.2003.1205177 confirms the 2.5x finding") | sources.json idx for [8] |

---

## Part 2 — New and rewritten claims (47 checked)

"S" = supported, "P" = partial, "N" = not supported / wrong source.

| # | Page · claim | Cited | Verdict |
|---|---|---|---|
| 1 | Index 1.1: JPMorgan ~55,000 | 3 | S — verbatim |
| 2 | Index 1.1 / 1.2c / CE §5.1: 56/44; 13/43/39/5 | 7 | S |
| 3 | Index 1.2c / CE §5.1: Zinnov "27% reach its portfolio-hub tier within five years", method not published | 7 | S — sentence present; no method on the page |
| 4 | Index 1.2c / 1.6c: Target 2005 [34] → "integrated global headquarters" over roughly two decades [17]; Lowe's 2015 → VPs in ten [26 35] | 34, 17, 26, 35 | S |
| 5 | Index 1.1 / 1.2a / Fig 5.2: 2.5×, more people per item | 8 | S (cycle 1) |
| 6 | Index 1.2c: 86% precision, beats churn and complexity | 6 | S (cycle 1) |
| 7 | Index Phase 0: 25–40% above IT-services bands | 45 | S — "25 to 40 per cent" |
| 8 | Index Phase 0: two-thirds of "mega" centre heads technical, many run a global portfolio | 43 | S (cycle 1 item 38) |
| 9 | Index T2: AI and cloud roles 18–25%, 18–24-month tenures | 50 | S |
| 10 | Index T1/T10/1.2d: "first three hiring decisions…"; centres past 100 with no permanent head | 36 | S |
| 11 | Index T7: Disney moved the data platform under the ad-platform EVP, April 2026, ~1,000 cut | 39 | S |
| 12 | Index T9: momentum "can quickly sag as a result of executive turnover" | 5 | S (truncated quote; full sentence on CE) |
| 13 | Index T11: "Every legacy-media company in the case studies had [a hiring freeze] in the period covered" | 12 | **N** — [12] is the WBD careers page; no source on the site documents a hiring freeze at any of the four → B2-10 |
| 14 | Index 1.1: Zurich ~eighteen years; Sky and Boston origin/acquired | 10–15 | S |
| 15 | Index 1.2e: "Ads measurement is what Disney and Paramount pulled their data platforms toward in 2026" | 39, 40 | **P** — Disney yes; TNW says the unified stack "will bring together content discovery, user data, recommendations, and ad technology" and that advertisers gain "measurement" — not a re-orientation of the data platform toward ads measurement → B2-11 |
| 16 | Index 1.2e / Applying It §4.2: "The India evidence named QoE and sessions telemetry as a capability [18]"; "Both case-study tracks named QoE or sessions … [24 39]" | 18, 24, 39, 20 | **N** — these are statements about the site's own research reports; [18] is Carmel & Agarwal 2001, [24] the Disney experimentation blog, [39] The Desk on Disney's reorg; none contains the claim → B2-7 |
| 17 | Index 1.2a: "time-zone separation hurt more than distance" tagged documented | 8, 25 | **P** — [25] is "metadata only"; the same finding is `inferred` on CE and Foundations → B2-13 |
| 18 | Index 1.2d: X-as-a-service "the interaction mode designed for remote customers" | 38 | **P** — Team Topologies defines X-as-a-Service as the minimal-collaboration mode; nothing on [38] says it was designed for remote customers → B2-21 |
| 19 | Index 1.3: Phase 1 = telemetry + experimentation engine; Phase 2 QoE + DQ; gates months 3/9/18/30 — internally consistent with Applying It §4.3, §4.5 and the LP milestone table | — | S (consistency) |
| 20 | Index 1.4 / cost line: $0.7–1.5M one-time; $1–2M/yr without offset; 45–50 / 90–95 | — | S — matches Applying It cost table (run-rate +$1.0–1.8M, offset −$1.1–1.8M); judgment-labelled |
| 21 | Applying It cost table: "25–40% over IT-services rates [45]" is the only cited number; $60k, $55k, $110–140k, $220k, 0–25%, ~20% carry no citation and sit under `judgment · assumption` | 45 | S — no invented number carries a citation |
| 22 | Applying It sensitivity table (20/40/60; commerce concentration) | — | S — all assumption-labelled, no citations |
| 23 | Applying It Fig 4.1 `<desc>` vs alt table vs §1.2e table vs prose: QoE partial/pass/pass; sessions fail/pass/fail; fraud partial/pass/partial; ads partial/pass/partial; "?" on ML, fraud, ads, commerce | — | S — all four representations agree; the four "?" text marks in the SVG match the desc |
| 24 | Applying It §4.2 Test 3 / §4.5 / Foundations §3.11: the 2026 mesh retrospective "found most organizations ended up with a thick central platform doing the domain work" | 127 | **N** — the article names IT re-badging teams as "domains", over-built platforms, governance stalls, project-based budgets and reversion to shadow IT; it does not say most organizations ended up with a thick central platform → B2-9 |
| 25 | Applying It §4.5: Larson "three to five directs if hands-on and five to eight if people-focused, never more than eight" | 46, 134 | **P** — [46] says "Managers should support 6-8 engineers", "<4 → TLM", "never … more than eight"; "three to five" is attributed to the book on Foundations; "five to eight" is in neither → B2-2 |
| 26 | Applying It §4.5: McKinsey five archetype ranges | 48 | S — browser-verified |
| 27 | Applying It §4.3 / §4.6 / index Phase 2: NBCU "embedded with and equally accountable to" | 47 | S (cycle 1, Lazarus memo) |
| 28 | Applying It §4.3: X-as-a-service, Team API, three interaction modes (C3-13/14) | 37, 38 | S — matches Team Topologies key concepts |
| 29 | Applying It Fig 4.3: PDT 16:00–01:00, EDT 13:00–22:00, IST 03:30–12:30; ≤ 2.5 h if IST to 19:30 and EDT from 07:30; gap 9.5–13.5 h | — | S — arithmetic checks |
| 30 | CE §5.1: 2,117 / 3,728 / 2.36M / $98.4B FY26; 1,700 / 1.9M / $64.6B | 7, 145 | S |
| 31 | CE §5.1: ~110 (early 2024–late 2025), >120 since Jan 2023, ~50/yr, 35% mid-market | 43, 146 | S |
| 32 | CE §5.4 cross-border-data paragraph | none | S — visibly unsourced under `judgment`; no citation invented; DPDP Act 2023 is the only fact in it and it is stated as general knowledge |
| 33 | CE §5.5: 12–18 departures at 18–25% on 30–35 by month 30 | — | S — 30×(1−0.82^2.5)=11.7; 35×(1−0.75^2.5)=17.9 (survival arithmetic over 2.5 years; slightly high given the cohort converts at months 3 and 9, but "expect 12–18" is defensible) |
| 34 | CE §5.5: "GCCs +200k FY26 vs IT services +110k" (table and prose "GCCs added ~200k net in FY26") | 45 | **N** — HRKatha says GCCs "are on track to hire more than 510,000 professionals in 2026"; no 200k/110k pair (cycle-1 item 37 flagged this as unverified; it was not fixed) → B2-4 |
| 35 | CE §5.5: −80k at top-5 IT services over 18 months to mid-2025 | 45 | S — verbatim |
| 36 | CE JPMorgan card: 50,000+ Aug 2023; ~55,000; ~1,000 in cloud/cyber/"AI data pipelines"; 2M sq ft Mumbai for ~30,000 by 2029 | 3, 28 | S — all on [3] |
| 37 | CE Target card quotation "rests with" | 17 | **P** — source reads "resting with" → B2-1 |
| 38 | CE §5.6 (b): "Citi CGSL sold to TCS after a decade as a captive" | 4 | **N** — "after a decade" not in [4] or [147] → B2-6 |
| 39 | Foundations §3.10: "a 2025 retrospective in the same journal confirms the finding has held" | 8 | **N** — the retrospective exists (Herbsleb & Mockus, IEEE TSE 51(3), March 2025, DOI 10.1109/TSE.2025.3533977, read in a browser) but its abstract says "radical changes in business and technical environments have substantially changed how the challenges of GSD manifest" and that citations "declined for its second" decade; it does not say the 2.5× finding has held, and it is not in sources.json → B2-5 |
| 40 | Foundations §3.6: Graicunas 5→100, 6→222; Urwick disclosure via Nickols; quote via secondary | 128, 129 | S |
| 41 | Foundations §3.7: Larson book-vs-post split | 46, 132 | S (book not read; attribution is explicit) |
| 42 | Foundations §3.4: Cataldo "significantly"; Inverse Conway Leroy & Simons via Fowler | 126, 123, 124 | S |
| 43 | CS §2.8: Sky sentence and quotation | 29 | S |
| 44 | CS §2.9: Paramount Desk wording; "two different clouds with no connectivity"; Q3 2026 / 1 June 2027 | 116, 40, 94 | S |
| 45 | CS §2.7: "Global Networks (… later renamed Discovery Global)" | 93 | S in prose; alt-table row inconsistent → B2-17 |
| 46 | CS §2.5: Prime Video quotations | 11 | S |
| 47 | CS Fig 2.1 alt table, 12 rows: Netflix 2020/Jan 2023/Oct 2023/Feb 2026 [78 79 80]; Spotify Oct 2012 [81], Mar 2014 [15], Apr 2019 [62]; Amazon Aug 2019 [66]; Disney Feb 2023 [88]; NBCU Jan 2019 [14] ("In January 2019, NBCUniversal and Sky announced they would partner"), Jul 2021 [95]; WBD Apr 2022 and Aug 2022 [91] | as listed | 10 S; **2 N** — the TechCrunch Max interview [91] mentions neither the April 2022 merger close nor an August 2022 single-service announcement → B2-8 |

---

## Part 3 — Numbered findings

Severity: **blocking** = wrong/fabricated claim, invented citation, broken primary URL, uncited factual claim, or a cycle-1 fix not applied; **major** = mis-tagged or partially supported; **minor** = wording.

### Blocking

**B2-1 · blocking · charter-evidence.html §5.2 Target card (B31a not applied)**
Finding: `The operating rule its president states: "ownership of outcomes rests with where the center of gravity for the capability sits."` The source [17] reads "resting with". Index 1.1 was corrected; the card was not.
Fix: `The operating rule its president states: "…ownership of outcomes resting with where the center of gravity for the capability sits."<sup>17</sup>` (or move the opening quotation mark to "where").

**B2-2 · blocking · applying-it.html §4.5 first sentence (B21 mis-applied)**
Finding: "a manager should run three to five directs if hands-on and five to eight if people-focused, never more than eight.<sup>46 134</sup>" — [46] (the 2018 post) gives 6–8, "<4 → TLM" and "never … more than eight"; [134] is the reorg post and contains no span numbers; "three to five" is attributed to *An Elegant Puzzle* [132] on Foundations; "five to eight" appears in neither source and contradicts Foundations §3.6 ("people managers six to eight").
Fix: "Larson's rule is that a team is six to eight people, below four it is a project, and a manager should run six to eight directs if people-focused — never more than eight — and, per *An Elegant Puzzle*, three to five if hands-on.<sup>46 132</sup>"

**B2-3 · blocking · learning-plan.html §6.5 (B34 not applied)**
Finding: The response says the dropped list is "marked `data-cite="none"` deliberately"; `grep -c 'data-cite="none"' docs/learning-plan.html` returns 0. The five `<li>` items (Monday Morning Data Chat ended; leaddev.com/podcast 404; PriorityZero last episode 13 Jan 2025; skamille.medium.com 403; no "Data Leaders" title verified) are checkable facts with no citation; `check-citations.py` passes only because it inspects `<p>`, not `<li>`.
Fix: add `data-cite="none"` to the `<ul>` (or each `<li>`) in the content source for §6.5 and extend the script's coverage check to `<li>` inside `<main>` so the exemption is deliberate rather than accidental.

**B2-4 · blocking · charter-evidence.html §5.5 talent table "Supply shock" row and the paragraph after it (cites 45)**
Finding: "GCCs +200k FY26 vs IT services +110k" and "GCCs added ~200k net in FY26" are not in HRKatha [45] (fetched again: the page says GCCs "are on track to hire more than 510,000 professionals in 2026" and that "more than 80,000 roles disappeared in the eighteen months to mid-2025"). Cycle-1 item 37 flagged the pair as unlocated; it survived the rebuild. The −80k half of the row is verbatim and fine.
Fix: table cell → "−80k at top-5 IT services (18 mo. to mid-2025); GCCs on track to hire 510,000+ in 2026<sup>45</sup>"; prose → "~80,000 roles disappeared at the top five IT services firms over 18 months to mid-2025 while GCCs are on track to hire more than 510,000 people in 2026, and 63% of GCCs are hiring niche AI/ML and 54% data engineering<sup>45 148</sup>". If the 200k/110k pair has a source (EY/Xpheno), add that source; do not keep it on [45].

**B2-5 · blocking · foundations.html §3.10 first paragraph (cites 8)**
Finding: "a 2025 retrospective in the same journal confirms the finding has held." The retrospective exists — Herbsleb & Mockus, "Retrospective: An Empirical Study of Speed and Communication in Globally Distributed Software Development," *IEEE TSE* 51(3): 833–835, March 2025, DOI 10.1109/TSE.2025.3533977 (C3's source list records the DOI; it is not in `sources.json` and the [8] note does not mention it) — but it is a three-page reflection on the paper's influence. Its abstract says "radical changes in business and technical environments have substantially changed how the challenges of GSD manifest" and that citation counts "declined for its second" decade. It does not re-test or confirm the 2.5× result; the sentence as written is wrong.
Fix: replace the clause with "a 2025 retrospective by the same authors in the same journal reflects on the paper's influence and notes that changes in business and technical environments have altered how the challenges of distributed work manifest — the delay mechanism is the durable part, not the multiplier<sup>8</sup>", and add the retrospective DOI to the [8] note (or as its own entry). Applying It §4.2 and index 1.1 cite 2.5× without the "has held" claim and need no change.

**B2-6 · blocking · charter-evidence.html §5.6 table (b), "Strongest documented failure" (cites 4)**
Finding: `Citi CGSL sold to TCS after a decade as a captive. documented [4]` — "after a decade" is in neither [4] nor [147]. B34 removed the identical clause from index 1.2b; this copy survived.
Fix: "Citi sold Citigroup Global Services to TCS in October 2008, tied to a multi-year service contract. documented<sup>4 147</sup>"

**B2-7 · blocking · index.html §1.2e first paragraph; applying-it.html §4.2 first paragraph**
Finding: Sentences describing what the site's own five research tracks concluded are cited to external sources that say nothing of the kind: "The India evidence named QoE and sessions telemetry as a capability.<sup>18</sup>" ([18] = Carmel & Agarwal 2001); "Both case-study tracks named QoE or sessions as candidates for graduating domain ownership, and one of them listed fraud first.<sup>24 39</sup> documented" ([24] = Disney Streaming's experimentation post; [39] = The Desk on Disney's April 2026 reorg); Applying It repeats the three-track summary with "<sup>18 20</sup>". [20] (DalleMule & Davenport) legitimately underlies the canon's offence/defence vote, so it can stay on that clause only. The `documented` chip on a sentence about the memo's own research is a category error.
Fix: index — "The organization-design canon favoured defence-heavy work — fraud, commerce data quality — because it is coordinated by standardized outputs.<sup>20</sup> The India evidence named QoE and sessions telemetry as a capability; both case-study tracks named QoE or sessions as candidates for graduating domain ownership, and one of them listed fraud first. No track named a day-one domain. The choice is this memo's… [judgment]" — no citation and no `documented` chip on the track summary (the tracks are `research/c1–c5`, which the site does not cite). Applying It — same: keep <sup>20</sup> on the canon clause only.

### Major

**B2-8 · major · case-studies.html Fig 2.1 alt table, WBD rows "Apr 2022" and "Aug 2022" (cite 91)**
Finding: [91] (TechCrunch, May 2023 Max interview) confirms 12 months of planning, "20% faster", four CDNs and the merged teams, but mentions neither the April 2022 merger close nor an August 2022 announcement of a single service. Both rows are true and both are unsourced on the site (C2 §3.2 asserts them without a citation either).
Fix: cite the WBD press releases (merger completion, 8 April 2022; Q2 2022 earnings/strategy update, 4 August 2022) or the WBD Wikipedia entry with a "tertiary" note; add to `sources.json`.

**B2-9 · major · foundations.html §3.11 "stream-aligned bias" and applying-it.html §4.2 Test 3, §4.5 (cite 127)**
Finding: "the 2026 data-mesh retrospective found most organizations ended up with a thick central platform doing the domain work" / "which is the mesh retrospective's finding about why most organizations ended up with a thick central platform". The Thoughtworks article as fetched names the failure modes the site lists in §3.9 (IT re-badging teams as domains, over-built platforms, governance stalls, project-based budgets, reversion to shadow IT) but does not state that most organizations ended up with a thick central platform. That conclusion is `research/synthesis.md`'s gloss.
Fix: Foundations §3.11 — "The Thoughtworks retrospective says domains lack data-competent staff and will not fund them, and that 'domains' get created by re-badging IT teams; the practitioner literature says most orgs cannot staff data-competent domain teams<sup>118 127</sup> — which is how a thick central platform ends up doing the domain work. [judgment]". Applying It §4.2 — "…and the 2026 data-mesh retrospective's failure modes (unfunded domains, re-badged IT teams) are the mechanism by which a boundary through the warehouse produces a central platform doing domain work anyway<sup>41 127</sup>". §4.5 — "which is the arithmetic behind the mesh retrospective's unfunded-domain failure mode<sup>127</sup>".

**B2-10 · major · index.html §1.5 tripwire T11 (cites 12)**
Finding: "A hiring freeze. Every legacy-media company in the case studies had one in the period covered; WBD stood up its hub during cuts.<sup>12</sup>" No source on the site documents a hiring freeze at Disney, WBD, NBCU/Sky or Paramount; the case studies document layoffs. [12] is the WBD India Hub careers page and supports neither clause.
Fix: "A hiring freeze. Every legacy-media company in the case studies cut headcount in the period covered — Disney, WBD, Sky and Paramount — and WBD stood up its hub during cuts.<sup>29 92 98 108</sup>" (or tag the sentence [judgment] and keep it uncited).

**B2-11 · major · index.html §1.2e last paragraph (cites 39 40) and applying-it.html §4.3 "Ads measurement" row (cites 39 40)**
Finding: "Ads measurement is what Disney and Paramount pulled their data platforms toward in 2026 … documented". Disney: supported ([39], data platform moved under the ad-platform EVP; Atlas "tighter integration with ad technology systems"). Paramount: [40] says the unified stack "will bring together content discovery, user data, recommendations, and ad technology" and that advertisers gain "improved campaign management, measurement, and targeting" — a stack consolidation that includes ad tech, not a data platform pulled toward ads measurement.
Fix: "Disney moved its streaming data platform under its ad platform in 2026, and Paramount's 2026 stack consolidation unifies user data with ad technology — which makes ads measurement the candidate that would give the site leverage in a future reorg.<sup>39 40</sup>" Same softening in the §4.3 row ("the data the 2026 P&L-driven reorgs pulled toward ad tech").

**B2-12 · major · evidence tags on qualified sources (task 5)** — two consequential downgrades; the rest accepted
(a) case-studies.html §2.6 Global sites: "Hotstar was a full-stack, full-domain engineering org from 2015 with its own infrastructure and data platform documented<sup>109</sup>". [109] is ByteByteGo, "Secondary; summarizes two JioHotstar Engineering Blog posts whose pages did not render". The underlying primary is an engineering blog nobody on the project read, not a press release, and the claim is the domain-ownership proof the recommendation leans on. → `inferred`, or add the two JioHotstar engineering posts to `sources.json` and cite them.
(b) case-studies.html §2.8 Global sites: "The UK (Osterley, Leeds) is the platform's engineering core and its origin: the platform was built there first, so this is not a remote site that was handed a charter but the site the charter came from documented<sup>14 74</sup>". [14] (AWS, vendor) says joint NBCU and Sky teams built Peacock in 12 months and quotes Sky's Keith Davidson and Colin Innes; [74] is recruiting copy. Neither says the platform was built in the UK first; the NOW TV lineage is tagged `inferred` two paragraphs earlier. → `inferred`. The same "origin site" framing appears in Fig 2.2 and index 1.1 (tagged `documented` with [10–15]); index 1.1 should read "Sky's platform organization and Spotify Boston were origin or acquired sites, not new hubs<sup>10–15</sup> inferred" or drop the Sky clause from the documented run.
Accepted as `documented` with the visible qualifier: DMED/JioStar/Discovery+/Paramount+ dates via Wikipedia (press-release-backed); Disney data platform via Databricks/Snowflake (the company's own engineers quoted); Target via ANSR (direct quotation, vendor label visible); WBD charters via recruiting copy (page says "recruiting copy, so the charter is aspirational"); Forrester 2007 via the summary page (the quotation is on it); Experiment-X via the Disney Streaming blog ([24] — first-party, see B2-15).

**B2-13 · major · index.html §1.2a second paragraph (cites 8 25)**
Finding: "…and time-zone separation hurt more than distance. documented<sup>8 25</sup>". [25] (Cummings et al.) is "metadata only"; B17 downgraded the identical finding to `inferred` on Charter Evidence and Foundations but the index copy kept `documented`. Applying It §4.2 and Fig 4.3 cite [25] without a chip, which is fine.
Fix: split the chip: "…work items spanning sites took about 2.5 times as long … documented<sup>8</sup>, and time-zone separation hurt more than distance inferred<sup>25</sup>."

**B2-14 · major · charter-evidence.html Target card "Lesson" and §5.6 table (c) / closing judgment (B26 partial)**
Finding: The Target card says "reached after ~15 years"; §5.6 (c) says "the two celebrated graduations took 10–15 years" and the closing judgment "on a 10–15-year clock", while §5.2's synthesis paragraph says "10–20-year stories", index 1.6c says "ten to twenty" and Fig 1.1 says "10–20". Target's own source is a 2026 interview titled "21 Years"; Lowe's is ten.
Fix: card → "reached over roughly two decades"; §5.6 (c) → "took ten to twenty years"; judgment → "on a 10–20-year clock".

**B2-15 · major · docs/sources.html qualifier derivation ([24]; [144])**
Finding: [24] (Jerman et al., Disney Streaming engineering blog, first-party, note "Read via browser; blocks automated fetch") renders "documented · via secondary" — the build's qualifier rule matched the word "via" in "via browser". It mislabels a primary source as second-hand and makes the Experiment-X paragraph look weaker than it is. Conversely [144] (Working Backwards, note "Book; retail page verified only") renders with no qualifier, and [146] (Storyboard18 reporting EY) renders none although it is secondary reporting.
Fix: derive the qualifier from an explicit `qualifier` field in `sources.json` (or match "via secondary"/"via a" rather than bare "via"); set [24] to none, [144] to "retail page only", [146] to "secondary".

### Minor

**B2-16 · minor · case-studies.html §2.4 Global sites** — "the best example in this set of a non-HQ site owning product surface area, and it analytics function not documented as Zurich-owned (inferred) inferred" is ungrammatical and carries the word "(inferred)" plus the chip. Fix: "…owning product surface area; whether Zurich owns YouTube's analytics function is not documented. inferred<sup>13</sup>".

**B2-17 · minor · case-studies.html Fig 2.1 alt table, WBD "Jun 2025" row** — "Split into Streaming and Studios and Discovery Global announced" vs the prose "Global Networks (… later renamed Discovery Global)". Fix: "Split into Streaming and Studios and Global Networks (later Discovery Global) announced".

**B2-18 · minor · charter-evidence.html §5.4 Leadership seeding** — "…without escalating to the country head; Zinnov's version is the 7:1–8:1 candidate ratio and hiring across the pyramid.<sup>31</sup>" — the Zinnov clause needs [36] (the talent table row has [31 36]). Fix: `<sup>31 36</sup>`.

**B2-19 · minor · charter-evidence.html §5.5 talent table "GCC pay premium" row** — caveat cell reads "EY via secondary reporting; EY GCC Pulse 2025 via secondary reporting." (duplicated) and cites [45 148]; the EY release [148] contains no premium figure (cycle-1 B2). Fix: "HRKatha, citing EY GCC Pulse 2025; the EY release itself gives no premium figure.<sup>45</sup>".

**B2-20 · minor · charter-evidence.html §5.5 talent table row label** — "AI / cloud / data roles | 18–25%" — Zinnov says "AI and Cloud roles"; "data" is the site's proxy (the prose two lines down already says "Use … 18–25% for the data and ML roles the org needs [judgment]"). Fix: label "AI / cloud roles (proxy for data roles)".

**B2-21 · minor · index.html §1.2d** — "X-as-a-service with a versioned contract — the interaction mode designed for remote customers —". Team Topologies does not describe X-as-a-Service as designed for remote customers. Fix: "— the interaction mode with the least collaboration, and the one the Remote Team Interactions Workbook favours across time zones<sup>38 44</sup> —" or simply "— the minimal-collaboration interaction mode —".

**B2-22 · minor · foundations.html Fig 3.1 caption** — the figure's own text says "Vista: no measurable quality penalty" but the caption cites [8 19 41 51] and not Bird [16]. Fix: add 16 to the caption run.

**B2-23 · minor · docs/sources.html** — s-107 (TechRepublic, Hulu leak) is cited on no page since the case-studies trim, yet sits in the cited list; the "Consulted, not cited" heading says "13 sources" while 14 entries are uncited. Fix: move [107] into the consulted section (renumbering is automatic) or restore its citation in CS §2.6.

**B2-24 · minor · sources.json note for [48] (McKinsey)** — add "the page's facilitator paragraph is mislabelled 'supervisor' (McKinsey typo); ranges read in browser 2026-08-30" so the next auditor does not re-open it.

**B2-25 · minor · charter-evidence.html §5.6 table (d)** — "Forrester's 2011 'captive +1' and augmentation hybrids were consultant constructs with no documented follow-up. documented<sup>153</sup>" — the models are documented; "no documented follow-up" is the site's search result. Fix: chip → `inferred`, or split: "…were consultant constructs documented<sup>153</sup> with no documented follow-up inferred".

---

## What did not reproduce a problem (for the record)

- Cost table (Applying It §4.5): the only sourced number is 25–40% [45], which matches HRKatha; every other figure is explicitly assumed and uncited.
- Sensitivity table: entirely assumption-labelled; no citations.
- Fig 4.1 desc, alt table, the §1.2e compact table and the §4.2 judgment box agree on every mark; the SVG's four "?" marks fall on ML platform, fraud, ads and commerce as the desc says.
- Fig 4.3: every UTC conversion and the 2.5-hour stretch window check; the 9.5–13.5 h range is correct for PDT/EDT/PST/EST vs IST.
- Attrition arithmetic (12–18 of 30–35 by month 30 at 18–25%) checks under survival compounding.
- Cross-border-data paragraph (CE §5.4): visibly unsourced under `judgment`; no citation invented. Same for the legal gate on Applying It §4.2.
- "Consulted, not cited" entries s-204 … s-216: none is cited on any page.
- Genericization: no employer, product or first-person company reference anywhere; "our"/"we" occur only inside quotations from Netflix, Spotify, Disney, WBD, JPMorgan, Google and dbt, in the tag key ("our position"), and in "we say so" / "we could verify".
- URLs: only [48] and [163] changed; both resolve (the McKinsey page in a browser only — the note says so).
