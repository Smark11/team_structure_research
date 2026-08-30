# Cycle 1 — Reviewer C (editor)

Read in order: index → case-studies → foundations → applying-it → charter-evidence → learning-plan → sources (skimmed). Site plan and `research/recommendation.md` used as the reference for intended positions.

## Verdict

1. It reads as one argument on pages 1, 4 and 5. Page 2 and page 3 are research reports wearing the memo's clothes, and page 6 was written before the decision was made: it treats the charter as open and schedules an "extension to ownership" review the recommendation explicitly rejects.
2. The biggest structural problem is the distributed-work evidence (Herbsleb 2.5×, Cummings, Carmel & Agarwal, Bird, Nagappan). It is laid out in full three times — foundations 3.10, charter-evidence 5.4, applying-it 4.2 — and clipped in a dozen more places. The site spends roughly 1,500 words proving one thing.
3. Numbers drift between pages: India steady-state FTE 45–50 vs 45–55; Netflix "ten times" vs "thirty times" this org; the time-zone gap is 10.5, 12 and 12.5 hours on different pages; GCC pay premium 15–40% vs 25–40%; tolerable platform-team span 6–7 vs 8–10.
4. The memo voice is right where the memo is speaking (index, applying-it, the "Why it matters here" boxes). Case-studies and foundations drop into literature-review register — "the post could only be read through a search excerpt", "the exact pages were not fetched" — which belongs in Sources, not in the argument.
5. The two-minute section delivers the answer, the reason and the one thing, but it is 540 words plus a figure and a 90-word caption: three minutes, with "what the US stops doing" last instead of second. Rewrite below.

---

## Blocking

### C1 — The Learning Plan argues for the rejected option and runs on a different calendar
**Severity:** blocking (contradiction between pages)
**Location:** `learning-plan.html`, intro judgment: "a ~140-person data org … standing up an India site and choosing between domain ownership, platform ownership, and an extension that graduates"; milestone table ("Charter decision — month 2"; "First graduation review — Extension to ownership assessed against written criteria — month 9"; "Conversion wave and first handover — month 6"); calendar row 7 "Define graduation criteria"; row 8 "decide experimentation ownership"; Kohavi entry: "Only if experimentation is a candidate platform capability for India; otherwise it drops to optional"; Bungay entry: "This book is why extension-to-ownership should be framed as widening the scope of intent given"; Fundamentals of Data Engineering: "hand it to the site lead and every converted FTE in month 5".
**Problem:** The index decides the charter now (hybrid), transfers the experimentation platform backend at month 3, requires ≥60% of conversion offers accepted before month 3, and gates at months 3, 9 and 18. The learning plan has the charter undecided until month 2, conversions at month 6, experimentation ownership undecided at month 8, and a "graduation" review of an extension at month 9. A reader who takes page 6 at face value plans the option page 1 rejected.
**Edit:**
- Intro: "This ranking is for this decision: a ~140-person data org at a large streaming/media company that has chartered its India site on three platform components plus one domain (Recommendation, §1.3) and now has to execute the phases. It is not a general management syllabus."
- Replace the milestone table with the phased-path gates:

| Milestone | What has to be true | Month |
|---|---|---|
| Charter written and announced | Ownership decisions dated; Team APIs drafted for every team on both sites | 1 |
| Gate 0→1 | Site head in seat; two second-line managers; ≥60% of wanted conversion offers accepted | 3 |
| Phase 1 transfer | Telemetry, data quality and experimentation-platform backend owned in India with on-call | 3 |
| Gate 1→2 | Two quarters of DORA metrics within 30% of baseline; <30% of items need a US decision | 9 |
| Phase 2 transfer | Sessions & QoE owned end to end; US QoE team dissolved | 9 |
| Org-wide review | Rewards, planning and ladder checked against the tripwires | 12 |

- Calendar row 2 → "Charter written; Phase 0 hiring"; row 5 → "Conversion offers out (gate 0→1 is month 3)"; row 6 → "Phase 1 transferred; first on-call rotation in India"; row 7 → "Phase-1 gate metrics reviewed"; row 8 → "Pre-gate review; QoE PM hired"; row 9 → "Gate 1→2; Phase 2 transfer".
- Kohavi: "Read before the experimentation platform backend transfers at month 3. Kohavi's case is that trustworthy experimentation is a platform discipline, not a set of analysts — which is why the backend moves and the analysis and review gate stay central." Move to month 2 in the calendar.
- Bungay: "This book is why each phase gate should be framed as widening the scope of intent given to the site, not as a change in reporting lines."
- Accelerate: replace "graduation review" with "phase gate"; "harder for a US team to block with 'they're not ready yet'" stays.
- Fundamentals of Data Engineering: "month 3, at the Phase 1 transfer".
- Team Topologies entry, "a team that starts in collaboration mode … has, by definition, graduated": replace with "Collaboration mode across a twelve-hour gap is time-boxed by definition; the Phase 1 gate is the point at which a team's interface becomes X-as-a-service."

### C2 — India steady-state headcount: 45–50 vs 45–55
**Severity:** blocking
**Location:** `index.html` §1.3 Phase 3 gate: "India site at 45–55 FTE with at most eight directs per manager" vs Fig 1.2 label "45–50 India FTE", §1.4 "landing at 45–50 India FTE and 90–95 US", `applying-it.html` §4.5 "roughly 45–50 India FTE" and the table total "~45–50".
**Problem:** The research memo carries the same inconsistency; the site inherited it.
**Edit:** Phase 3 gate → "India site at 45–50 FTE with at most eight directs per manager".

### C3 — Netflix is "ten times" this org on two pages and "thirty times" on a third
**Severity:** blocking
**Location:** `index.html` §1.4 "the Netflix shape, which at ten times this org's scale"; `applying-it.html` §4.6 "a data organization ten times this size"; `foundations.html` §3.9 "hub-and-spoke at roughly thirty times this org's scale; the post body could not be fetched".
**Problem:** Neither multiplier is sourced, and they disagree by 3×.
**Edit:** All three → "an order of magnitude larger than this org". Foundations: cut "the post body could not be fetched, so this is inferred from the title" — that is a Sources note, not argument.

### C4 — The time-zone gap is 10.5, 12 and 12.5 hours depending on the page
**Severity:** blocking
**Location:** `foundations.html` Fig 3.2 column header "What 10.5 hours of distance does" and §3.5 so-what "Collaboration mode across 10.5 hours"; `index.html` §1.4 "remote directs across a twelve-hour gap"; `applying-it.html` §4.4 "A remote direct across a 12-hour gap"; `charter-evidence.html` §5.6 judgment "shared ownership of the same work across a 12.5-hour gap"; Fig 4.3 shows PDT−IST = 12.5 h, EDT−IST = 9.5 h.
**Problem:** Four numbers for one fact. 10.5 is EST−IST in winter, which no other page uses.
**Edit:** State the range once, in the Fig 4.3 caption: "9.5 to 13.5 hours depending on coast and season". Everywhere else use the shorthand "the twelve-hour gap". Foundations Fig 3.2 header → "What a twelve-hour gap does"; §3.5 → "across a twelve-hour gap".

### C5 — Charter Evidence gives Pacific an overlap window that Fig 4.3 says does not exist
**Severity:** blocking
**Location:** `charter-evidence.html` §5.4 judgment: "For a US-Pacific/IST split the working-hours overlap is 0–2.5 hours, which is the worst case in the Cummings data." vs `applying-it.html` Fig 4.3 caption: "At nominal 09–18 hours the overlap with India is zero; the 2.5-hour ceiling exists only if both Eastern and India stretch, and Pacific never reaches it."
**Edit:** "For a Pacific/Eastern-to-IST split the overlap is zero at nominal hours and at most 2.5 hours if Eastern and India both stretch; Pacific never reaches it (Fig 4.3). Cummings found temporal separation costs more than distance, and this is about as separated as two sites get." Drop "worst case in the Cummings data" — the paper does not rank cases.

### C6 — GCC pay premium: 15–40% vs 25–40%
**Severity:** blocking
**Location:** `index.html` Phase 0: "15–40% above IT-services bands at mid-senior levels"; `charter-evidence.html` §5.1 "15–40%" and table row "15–40% … the same reporting also cites 25–40%"; `applying-it.html` §4.5 "GCCs pay 25–40% over IT-services rates at mid-to-senior levels".
**Edit:** Applying-it → "15–40%"; keep the "same reporting also cites 25–40%" caveat only in the charter-evidence table.

### C7 — Tolerable span for platform teams: 8–10 on Foundations, 6–7 on Applying It
**Severity:** blocking
**Location:** `foundations.html` §3.6 judgment: "Platform teams doing standardized work tolerate 8–10; domain analytics-engineering teams doing interlocked, uncertain work want 5–7." vs `applying-it.html` §4.5: "Data-platform work sits near the coach end: standardized enough for a span of six or seven, not standardized enough for ten," and the index/table ceiling "at most eight directs".
**Edit:** Foundations → "Platform teams doing standardized work tolerate the top of Larson's range, seven to eight; domain teams doing interlocked, uncertain work want five to seven. Nothing on either site should run at ten."

### C8 — "Every remote site holds a capability charter" vs "7 of 9"
**Severity:** blocking
**Location:** `index.html` §1.1: "Every remote engineering site in the eight case studies holds a capability charter — Netflix Warsaw, Prime Video Bengaluru, WBD's India hub, Sky's platform organization for Peacock, Spotify Boston." vs `case-studies.html` Fig 2.2: "7 of 9 documented sites" with Zurich and Hotstar as the exceptions.
**Edit:** "Seven of the nine documented remote sites in the case studies hold capability charters — Netflix Warsaw, Prime Video Bengaluru, WBD's India hub, Sky's platform organization for Peacock, Spotify Boston. The two exceptions are a home-market product (Hotstar) and an eighteen-year build (Google Zurich)."

### C9 — Hotstar's tech drain is "inferred" on two pages and "documented" on the third
**Severity:** blocking (characterization)
**Location:** `index.html` §1.2a tags the drain "inferred"; `case-studies.html` Disney §Global sites: "per a single trade newsletter — inferred"; `charter-evidence.html` Hotstar card: "'Hotstar lost a considerable portion of its technology team' to the Jio side; the business is now a Reliance-majority JV. documented31" and §5.6 table: "Hotstar's tech team drained to a competitor when the rights economics turned. documented3". Source 3 is itself tagged inferred in Sources.
**Edit:** Charter-evidence, both places → tag "inferred", and in the card: "per one trade newsletter quoting an unnamed executive".

### C10 — "Every source says half-ownership fails" is a judgment printed as a fact
**Severity:** blocking (judgment asserted as fact)
**Location:** `index.html` §1.1 "What the US stops doing": "Half-ownership is the one configuration every source in the research says fails.2324" — no judgment label. Same sentence labeled judgment on `foundations.html` §3.11 and `index.html` §1.6d. Also `applying-it.html` §4.4 opening: "Every source that describes a distributed-ownership failure describes the same one: the sending site kept a hand on the work.23" — one citation, no label.
**Problem:** No source says "half-ownership fails". Nagappan says diffuse ownership predicts defects; Amazon says dependencies predict failure. The leap from those to "half-ownership" is the memo's — the right leap, but it has to wear the label, because it is the claim the whole recommendation hangs on.
**Edit (index §1.1):** "Diffuse ownership is the best-replicated defect predictor in the software-engineering literature, and dependencies were the failure mode Amazon diagnosed in its own teams.2324 Half-ownership is diffuse ownership by design. judgment"
**Edit (applying-it §4.4):** "The distributed-ownership failures in the record share one feature: the sending site kept a hand on the work.2324 judgment So the transfer is written as a list of things the US organization ceases to do…"

### C11 — "43% that never leaves the execution tier" is neither Zinnov's number nor the site's
**Severity:** blocking (number contradiction and unlabeled causal claim)
**Location:** `applying-it.html` §4.5: "Bands set at vendor-plus rather than GCC market are how a site ends up in the 43% of the population that never leaves the execution tier.7"
**Problem:** 43% is the Satellite share today; "never leaves" is not in the source. The rest of the site says 56% execution shops (Outpost + Satellite). And the causal claim (bands → tier) is asserted with a citation that does not make it.
**Edit:** "Bands set at vendor-plus rather than centre-market rates are one way a site stays in the 56% that are still execution shops.7 judgment"

### C12 — A fact about the reader's own site is tagged "documented"
**Severity:** blocking (judgment/assumption as fact)
**Location:** `index.html` §1.2a: "The site also lacks today the three things the documented domain owners hired first: a site head with a global title, product management, and second-line managers.1526 documented"
**Problem:** The citations document what Target and Lowe's hired. That this site lacks them is an assumption, flagged as such on Applying It §4.1.
**Edit:** "The documented domain owners hired three things first — a site head with a global title, product management, second-line managers1526 documented — and, on the assumed baseline, this site has none of them today."

### C13 — Foundations names fraud as the first domain; the site's answer is QoE
**Severity:** blocking (which domain goes first)
**Location:** `foundations.html` §3.9 so-what: "Defense work (fraud, commerce data quality, subscriber-state modeling) is coordinated by standardized outputs and is the plausible full-ownership candidate; offense work (experimentation analysis, browse, funnels) is adhocratic and belongs where the stakeholders sit."
**Problem:** Stated as the page's conclusion with no pointer to the resolution. A reader of Foundations leaves with a different first domain than a reader of the Recommendation.
**Edit:** append: "That is the canon's vote, and it loses on the third test: fraud's outputs standardize but its decisions are denominated in dollars and signed off in the US. Applying It §4.2 scores it, and sessions/QoE wins; fraud is the gated second domain."

### C14 — Foundations promises a cross-reference Applying It never makes
**Severity:** blocking (contradiction between pages)
**Location:** `foundations.html` §3.12 intro: "The Applying It page scores each candidate charter against this list; the numbers are stable references." Applying It scores three tests and never cites a principle number.
**Edit:** Make it true — it stitches the two pages together at almost no cost. In `applying-it.html` §4.2 add to each test heading: Test 1 "(principles 1, 4)"; Test 2 "(principles 1, 7)"; Test 3 "(principles 2, 5)"; the gate "(principles 3, 14)". Otherwise cut the sentence.

### C15 — Genericization: "direct competitor"
**Severity:** blocking by rule; low actual risk
**Location:** `learning-plan.html`, Netflix Technology Blog entry: "Direct-competitor relevance: how a streaming company draws the platform/domain line for data."
**Problem:** The only place the site states the reader's employer's market position relative to a named company. The site already says "streaming/media", so this adds little, but it is the kind of detail that accumulates.
**Edit:** "Peer relevance: how a streaming company draws the platform/domain line for data." No other slips found: "this reader's domains" (case-studies, Disney) and "paid sharing" are generic enough.

---

## Major — redundancy and structure

### C16 — The distributed-work research is written out three times
**Severity:** major
**Location:** `foundations.html` §3.10 (332 words); `charter-evidence.html` §5.4 "The distributed-work research" (four paragraphs + Fig 5.2 + judgment, ~450 words); `applying-it.html` §4.2 Test 1, Test 3 and the gate (~400 words). The 2.5× itself appears fourteen times across the site.
**Edit:** The canon lives in full on Foundations §3.10. Charter-evidence keeps Fig 5.2 and its judgment box, and replaces the four paragraphs with: "The distance research (Foundations §3.10) gives the base rate for the alternative: cross-site work items took about 2.5× as long at Lucent because more people were needed per item, not because anyone was slower;14 temporal separation costs more than distance;25 and Microsoft found no quality penalty for distributed work once ownership was site-level and tooling identical, while diffuse ownership predicted defects at 86% precision.1323" Applying It keeps one derivation sentence per test (it is the application, so the tests must show their source) and cuts the Bird/Nagappan/Amazon restatement in "The gate" to: "A unit that passes all three is still not transferable unless one team on one site owns it whole — the Vista finding and Amazon's, from opposite ends.2324"

### C17 — Hotstar in full on three pages
**Severity:** major
**Location:** `index.html` §1.2a (concurrency numbers, market list, JV); `case-studies.html` Disney §Global sites (full narrative); `charter-evidence.html` Hotstar card (concurrency numbers, market list, JV again); plus §1.1, §1.6a, Fig 2.2, §5.6 table.
**Edit:** Full story stays on case-studies (Disney §Global sites). Index §1.2a first paragraph → "Hotstar is the proof that an India engineering organization can own a streaming product at record concurrency and export its platform (case studies, Disney) — and it was a home-market product with a local P&L, not a charter handed to a centre.1 Google's Bengaluru post says the same thing in its own words: 'building from India, for the world.'2 The pattern is India-first products that later globalized, not global products handed over. inferred" Charter-evidence card → keep the H3, then: "Built in India from 2015, scaled to record concurrency, platform reused across Disney+ markets; a home-market product with local P&L, not a GCC charter.1 After the 2022 IPL rights loss its technology team drained toward Jio (one newsletter, inferred3) and the business is now a Reliance-majority JV. Full account: Case Studies, Disney." Cut the "Reported 2023 tech layoffs … could not be verified" line — that is a Sources note.

### C18 — The 27% base rate is stated four times on Charter Evidence alone
**Severity:** major
**Location:** `charter-evidence.html` §5.1 body ("only about 27% reach Portfolio Hub … within five years"), Fig 5.1 in-figure note ("Roughly 27% of centers reach Portfolio Hub within five years"), §5.6 table row (c), §5.6 judgment ("against a 27%-in-five-years base rate"); plus `index.html` §1.1, §1.2c, §1.6a ("roughly three-quarters of sites never complete"), §1.6c, §1.7.
**Edit:** In full once, §5.1 body, with the ceiling caveat. Cut the in-figure note; §5.6 table row (c) → "~27% in five years (§5.1)"; §5.6 judgment → "on a 10–15-year clock against the §5.1 base rate". Index keeps the §1.1 clause and §1.2c sentence; §1.6c "The base rate is about 27% in five years and the celebrated cases took ten to fifteen.7" stays (it is the rebuttal); §1.7 stays (it is the caveat).

### C19 — Spotify's retrospectives re-run on Foundations
**Severity:** major
**Location:** `foundations.html` §3.11 "Case studies vs. frameworks" (whole H3, ~150 words) repeats case-studies §2.0, §2.2, §2.4 and §2.1 in miniature.
**Edit:** Cut the H3 body; keep only the judgment box, re-headed "What the case studies say back" and opened with: "Across the eight companies (Case Studies §2.0): what survived had a single accountable owner per separable unit of work; what failed had autonomy without ownership — Spotify's 'responsibility without accountability', Amazon's 'dependencies, not size'.4824 Whatever India owns, the US org must be re-cut to not own it. judgment"

### C20 — Target's "center of gravity" quoted three times
**Severity:** major
**Location:** `index.html` §1.1 (full quote), §1.6d ("Target's 'center of gravity' rule is a hybrid and it worked"), `charter-evidence.html` Target card (full quote).
**Edit:** Full quote stays on the Target card and in §1.1 — it is the best line on the site and the two-minute reader should hear it. §1.6d → "Target's operating rule (Charter Evidence §5.2) is a hybrid and it worked".

### C21 — "What the US stops doing" is written four times; "rewards decide" twice verbatim
**Severity:** major
**Location:** `index.html` §1.1 paragraph, §1.4 paragraph ("What the US stops doing is listed, because it is the part that fails…"), `applying-it.html` §4.4 section and the ownership table's last column. Rewards: `index.html` §1.4 last paragraph and `applying-it.html` §4.6 last two paragraphs are near-verbatim ("own hiring budget and a promotion cycle on the same calendar and ladder … on-call compensation is identical … Without those, the charter is a slide").
**Edit:** The list in full lives on Applying It §4.4 (the operative page). Index §1.1 keeps its paragraph — it is the one thing the reader must do. Index §1.4 → cut both paragraphs to: "The transfer is written as a list of things the US stops doing — owning, gatekeeping and on-call for the three components; the US QoE team; India directs; and half-ownership as a category (Applying It §4.4). Rewards and processes decide whether it holds, not the chart:32 the India site gets the same ladder, calendar and on-call terms as the US, or the charter is a slide. judgment"

### C22 — Index §1.2e and Applying It §4.2's judgment box are the same 300 words
**Severity:** major
**Location:** `index.html` §1.2e (two paragraphs) vs `applying-it.html` §4.2 intro + judgment box "How the scoring resolves the disagreement".
**Edit:** Index §1.2e → "The research tracks disagreed: the canon voted for defence-heavy fraud, the India evidence for telemetry-shaped work, both case-study tracks for QoE or sessions.161822 They were applying one criterion without naming it — few US decision-makers per change, standardizable outputs, separability from the warehouse. Sessions and QoE passes all three; fraud passes two; commerce, funnels, browse and search fail the first. judgment The scoring is on Applying It §4.2." Keep Fig 1.3 there.

### C23 — Zinnov and Forrester quotes repeated in full
**Severity:** major
**Location:** "the first three hiring decisions shape the center more than the next ninety-seven combined": `index.html` §1.2d, `applying-it.html` §4.6, `charter-evidence.html` §5.3. "centres run past 100 people with no permanent head": index §1.2d, tripwire 1, applying-it §4.4, charter-evidence §5.3. Forrester "will not be anxious to simply transfer all of their best people": index Phase 0, applying-it §4.5, charter-evidence §5.3.
**Edit:** Full quotes once, on charter-evidence §5.3 (it is the failure-mode catalogue). Elsewhere one clause with the citation: index §1.2d "the leadership vacuum Zinnov documents33"; applying-it §4.6 "hired first, because the first hires set the centre's ceiling33"; index Phase 0 "on the evidence that the vendor withholds its best people5"; applying-it §4.5 "the vendor controls who is offered5".

### C24 — The US QoE team dies at month 9, 9–12, or 12
**Severity:** major
**Location:** `index.html` Phase 2 (month 9): "The US QoE team is dissolved into this"; §1.4: "ceases to exist as an owning team by month twelve"; `applying-it.html` §4.4: "ceases to exist as an owning team at month 9–12".
**Edit:** One rule everywhere: "dissolved at the month-9 transfer; no US owning team after month 12" — or just "at month 9". Pick one and use it in all three places.

### C25 — "Tripwire 6" is referenced but tripwires are not numbered
**Severity:** major
**Location:** `applying-it.html` §4.4 "Where it breaks": "Tripwire 6 on the Recommendation page exists for exactly this." Index tripwires are headed by month only.
**Edit:** Number them T1–T8 in the index headers ("T6 · any time — A US team re-creates capacity…") and reference "tripwire T6".

### C26 — Case Studies to ~5,000 words
**Severity:** major
Current 7,570 (page's own count). Cuts, in order of size, none of which removes a fact the recommendation cites:
1. **§2.0 "What all eight have in common" (989 w).** Three paragraphs, the table and the timeline all say the same thing. Cut the paragraphs to a 150-word lead: one sentence per finding, then "the table carries the evidence". Save ~500.
2. **WBD §How it changed (~200 w on the Netflix bid, Paramount Skydance, DOJ, state AGs, trial dates).** Irrelevant to charter. Keep one sentence: "Paramount Skydance's bid for Streaming and Studios closes no earlier than mid-2027.88" Save ~150.
3. **Disney §How it changed, Hulu-stack paragraph (~140 w).** Keep one sentence: "Hulu was absorbed onto the BAMTech-lineage stack over 2023–2026 without a headcount event.10784" Save ~110.
4. **Paramount (560 w).** It is the negative control; it needs 250. Cut the lineage sentence, EyeQ, Wiser's cloud migration, the 2024 and 2025 layoff counts, the CTO-succession detail. Keep: the non-decision, two clouds until 2026, the 2023 org merger without platform merger, the 2026 consolidation, "essentially empty" India. Save ~300.
5. **Google §How it changed (DeepMind merger, ~90 w).** Frontier-ML centralization has nothing to do with this decision. Cut to: "No public YouTube data-org reorg exists; the only Google structure event on record, the 2023 DeepMind merger, is frontier-ML centralization and not relevant here.79" Save ~60.
6. **Amazon §How it changed, Prime Video India business leadership (~60 w).** Cut. Save ~60.
7. **Netflix §How it changed, Stone's promotion history (~110 w).** Keep the point ("the data leader absorbed product and engineering, not the reverse") and one date. Save ~60.
8. **Spotify §Structure (~180 w).** Cut the Product Insights excerpt caveat and the "Missions" folklore line (Sources notes). Save ~60.
9. **Spotify §Where experimentation sits (~230 w).** Keep 2017 diagnosis, 2018 platform, 2023 scale, 2025 reviewers. Cut the January 2026 personalization-separation sentence and the 1.4 trillion data points. Save ~70.
10. **§2.10 "What nobody publishes", paragraphs 2–3 (the not-verified list, ~180 w).** Move to Sources as a "Could not verify" block; keep paragraph 1. Save ~180.
11. **Every "What is attributable" H3.** Fold to one or two sentences each; they currently restate the "Why it matters here" box. Save ~250.
12. **Register cleanup throughout:** "the post could only be read through a search excerpt", "seen in search results only", "both hosts returned 403", "the exact pages were not fetched" — all to Sources. Save ~100.
Total ≈ 1,900–2,000, landing at ~5,500; the remainder comes from tightening sentences in §Structure sections, which run 10–20% long everywhere.

### C27 — Foundations to ~4,000 words
**Severity:** major
Current 5,059. Cuts:
1. **§3.1 (416 w)** → 150. Cut the first two sentences ("The case studies in section 2 show what companies did. This page is the mechanism underneath: why some of it worked.") and the whole "Read each section as two to four claims…" judgment paragraph. Open with the four variables. Save ~250.
2. **§3.11 "Case studies vs. frameworks"** per C19. Save ~120.
3. **§3.7 Larson, reorg-sequence and organizational-debt paragraph (~150 w).** Keep the four reorg tests; cut the seven-step sequence and the Blank/Larson debt distinction. Save ~110.
4. **§3.9 data-org literature (503 w).** The Locally Optimistic/dbt/Mode/Stancil/Sanderson paragraph is a reading list, not an argument; the Learning Plan already has it. Cut to: DalleMule–Davenport (the one theory), Sanderson on contracts (the one mechanism), the mesh retrospective (the one field report). Save ~200.
5. **§3.6 span-of-control lineage (321 w)** → 200. The Graicunas/Urwick/Miller/Oxygen trace is good folklore-busting but runs long; cut the Urwick disclosure and the Miller sentence to clauses. Save ~100.
6. **§3.4 Conway evidence.** Merge Herbsleb & Grinter and Cataldo into one sentence. Save ~50.
7. **§3.2 Galbraith reconfigurable-organization paragraph.** Cut to one clause inside the so-what. Save ~50.
8. **§3.8 DORA 2023 report sentence.** Cut. Save ~30.
9. **Every "So what for the India site" box that restates the section's judgment paragraph** (§3.6, §3.9): keep one or the other. Save ~80.
Total ≈ 1,000.

---

## Minor — line edits, voice, headings

### C28 — Throat-clearing and restated purposes
**Severity:** minor
- `index.html` §1.2 intro: "Each drill-down is the argument the two-minute version compresses. Read them in any order." → cut.
- `applying-it.html` "Where this goes next" box → cut; the top-bar navigation does this.
- `charter-evidence.html` §5.6 judgment, last sentence: "The Recommendation page makes them; this page is what it stands on." → cut.
- `charter-evidence.html` §5.1: "This is not a niche move. It is also not a move with a good track record, once you read the distribution rather than the totals." → "Common, and mostly stuck: read the distribution, not the totals."
- "actually" ×5 (`charter-evidence` H1 and §5.2 lead; `foundations` §3.3 and §3.6 headings, §3.11) → cut each.
- "This is the part that fails in practice" appears in `index.html` §1.1 and as "This is the part that fails in practice" / "Where it breaks" in `applying-it.html` §4.4. Keep the index one.
- "binding constraint" ×6 across pages; "load-bearing", "operative artifact" — consultant register. Replace two or three with plain words ("the scarce thing is second-line managers").

### C29 — Headings, deks and captions that decorate
**Severity:** minor
- `case-studies.html` dek: "Reorgs beat snapshots: what changed, why, and what is plausibly attributable to structure." → "Eight companies, 2012–2026. Every one keeps the platform central; every remote site got a capability, not a domain."
- `charter-evidence.html` H1: "What the India evidence actually discriminates" → "What the India evidence rules out". Dek: "Base rates, reference sites, conversion failure modes, and the distributed-work research." → "Base rates, eight reference sites and the conversion failure modes. The evidence rules out shared ownership and says nothing about which domain."
- `applying-it.html` dek: "Three tests, eight domains, one ownership table." → "Three tests, twelve units of work, one ownership table." (Fig 4.1 scores twelve; the baseline table has eight rows, one of them leadership.)
- `foundations.html` §3.6 heading: "Span of control: what the evidence actually is" → "Span of control: '7' is a 1933 arithmetic exercise".
- Fig 5.1 caption: "GCC maturity distribution. Outpost and Satellite are execution charters; Portfolio and Transformation Hubs own a portfolio." → "56% of India centres are still execution shops; 44% own a portfolio, and only about a quarter of new centres get there within five years.7"
- Fig 2.1 caption is a citation dump. Prefix one finding: "Centralization moves cluster in 2023; every new-site tick on the axis is a capability charter."
- `charter-evidence.html` §5.2 lead: "Eight sites that the evidence actually documents." → "Eight cards, nine companies; one of them is an absence."

### C30 — The two-minute test
**Severity:** minor (but the page's job)
**Timing:** 540 words of prose ≈ 2:10 at 250 wpm; with Fig 1.1 and its 90-word caption inside the section, ~3:00. The answer is in the block above; the reason is paragraph 1–2; the one thing the reader must do is the last paragraph, after the diagram legend.
**Edit:** Cut to ~350 words, put "what the US stops doing" second, and move Fig 1.1 to the top of §1.2 so the two-minute section is prose only. Proposed text:

> **The evidence rules out both pure options and the extension.** No documented case exists of a global consumer domain handed to a new India centre on day one and succeeding; the India organizations that did own a domain end to end — Hotstar, Google Pay — were home-market products with a local P&L, and Hotstar's engineers walked to a competitor when the rights economics turned.123 Platform-only is the modal charter and it scales — JPMorgan runs 55,000 people on it — and it is also the modal drift into a cost centre that gets sold or cut when nothing the parent ships depends on it.456 The graduating extension has a base rate: about 27% of India centres reach portfolio ownership within five years, a number from the firm that sells centre set-ups, so read it as a ceiling.7
>
> **So: three whole platform components and one whole domain, owned in India from the start, and the US stops owning them.** That last clause is the decision. No US on-call for transferred components, no US approval gate on India-owned changes, no US managers with India directs, no "India builds, US approves" past the first phase. Diffuse ownership is the best-replicated defect predictor in the literature, and half-ownership is diffuse ownership by design.2324 judgment
>
> **Why this shape.** Seven of the nine documented remote sites hold capability charters.89101112 The distance research says distance is survivable for separable work with one owner and shared tooling — Microsoft found no quality penalty — and fatal for coupled work with diffuse ownership — Lucent's cross-site items took 2.5× as long.1314 Target's rule after fifteen years, "ownership of outcomes rests with where the center of gravity for the capability sits," is what a working hybrid sounds like.15
>
> **Why one domain, and why sessions and QoE.** A platform-only site has no customer of its own. Sessions and QoE is the one domain with few US decision-makers per change, outputs that standardize (telemetry in, metrics out) and no cross-domain dependency on the warehouse.1617 judgment Fraud and paid sharing is the second candidate, gated at month 18 because its decisions are signed in dollars in the US.18 Experimentation analysis, the metrics catalog and the review gate stay central, as at Google, Spotify, Netflix and Disney; the experimentation platform is a capability India can own.19202122 Commerce, funnels, browse and search stay where pricing and content strategy are set. judgment

### C31 — Overclaims in "Why it matters here" boxes
**Severity:** minor
- `case-studies.html` Disney: "Its one India engineering org of scale owned a whole market end to end, and that is exactly why it drained to a competitor and was JV'd away." → "…owned a whole market end to end, which is what made it possible to lose whole: the team followed the rights, and the business followed the JV." (The source supports the sequence, not the "exactly why".)
- `case-studies.html` Paramount: "bought nothing measurable" — fine, labeled.
- `charter-evidence.html` Netflix card lesson: "Suggestive, not evidence." Good; keep.

### C32 — "Three of the five tracks" reads as two on the index
**Severity:** minor
**Location:** `index.html` §1.2e names three positions — "the organization-design canon", "the India evidence", "the case studies" — then claims "three of the five research tracks independently named" QoE. The research supports three (C1, C2, C5), but the page merged C1 and C2 into "the case studies".
**Edit:** "…both case-study tracks and the India evidence — three of the five — named QoE or sessions independently." (Covered in C22's rewrite.)

### C33 — Evidence-collection notes in the argument
**Severity:** minor
**Location:** `foundations.html` §3.5 "the exact pages were not fetched, so treat the timezone preference as inferred"; §3.9 "the post body could not be fetched"; `case-studies.html` passim (see C26.12); `learning-plan.html` "Her Medium mirror blocks automated fetches".
**Edit:** Move to Sources entries as a "note" field; the argument pages keep only the tag.

### C34 — Figure numbering out of order on Foundations
**Severity:** minor
**Location:** Fig 3.2 (interdependence ladder) appears in §3.1; Fig 3.1 (disagreement map) appears in §3.11.
**Edit:** Swap the numbers, or move the ladder to §3.10 where its 2.5× row is argued.

### C35 — Sentences a reader cannot act on
**Severity:** minor
- `foundations.html` §3.11 "Mintzberg's adhocracy vs. Galbraith": "There is no clean resolution." Then a resolution follows. Cut the first sentence.
- `applying-it.html` §4.5: "Budget decides, as the tension says it would; what is not acceptable is ten-direct spans presented as economy." Good — this is the voice the rest of the site should have. Keep.
- `charter-evidence.html` §5.4 "One gap to name" paragraph and `index.html` §1.7 second bullet say the same thing (decision-rights material is consultant-grade). Keep the index one; on charter-evidence cut to one clause in the judgment box.
- `learning-plan.html` Galbraith entry: "The one book your business peers will recognize." Keep; specific and actionable. Team Topologies news: "A vendor blog, so filter the consulting pitches." Keep.

---

## Cross-reference of the numbers to hold constant

| Fact | Value to use everywhere | Pages to fix |
|---|---|---|
| India steady-state FTE | 45–50 | index Phase 3 gate |
| US steady state | 90–95 | — |
| Netflix vs this org | "an order of magnitude larger" | index §1.4, applying-it §4.6, foundations §3.9 |
| Time-zone gap | "the twelve-hour gap" (range 9.5–13.5 stated once in Fig 4.3) | foundations ×2, charter-evidence §5.6 |
| Overlap window | 0 at nominal hours; ≤2.5 h Eastern-with-stretch; Pacific none | charter-evidence §5.4 |
| GCC pay premium | 15–40% | applying-it §4.5 |
| Platform-team span | ≤8, typically 6–7 | foundations §3.6 |
| Execution-shop share | 56% (13 + 43) | applying-it §4.5 |
| Remote sites with capability charters | 7 of 9 | index §1.1 |
| Hotstar tech drain | inferred | charter-evidence ×2 |
| US QoE team dissolved | month 9 | index §1.4, applying-it §4.4 |
| Phase gates | months 3, 9, 18 | learning-plan milestones and calendar |
