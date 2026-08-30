# Cycle 3 — Fact-check and citation audit (Reviewer B) — exit-criteria cycle

Date: 2026-08-30. Scope: rebuilt `docs/*.html` (collapsed citation runs, chips after citations, smart-quote build step); every cycle-2 fix (B2-1 … B2-25) re-opened; 45+ new/rewritten claims sampled with priority on the v3 changes; `check-citations.py` run plus a scripted walk of the exempt regions; smart-quote sanity; sources page 7.1/7.2 split and qualifier sample; genericization.

Source numbers are the rendered `s-N` numbers (they shifted again from cycle 2; e.g. HRKatha is now [47], the Zinnov attrition blog [51], The Desk Sky cuts [30]).

## Summary

| Check | Result |
|---|---|
| Cycle-2 fixes verified (B2-1 … B2-25) | 25 opened: **23 applied and correct**; **1 applied in data but broken in rendering** (B2-15 → B3-1); **1 mis-applied** (B2-18 → B3-2) |
| New / rewritten claims checked | 45+ (index "In two minutes" incl. every number, the five-hub sentence's seven-citation run 8–14, and the pull quote verbatim "…ownership of outcomes resting with…" [16]; drill-downs 1.2a–1.2f incl. the compact scoring table; phases 0–3 and Gates 0–3; T1–T12 incl. T11's expanded run; Applying It baseline, three tests, matrix, ownership table, §4.4, Phase 0 plan table, cost table, Fig 4.3, §4.7; the three walk-throughs; the "India decides unilaterally" column; CE §5.1; Foundations and Case Studies pull quotes; WBD alt-table rows [92]) |
| `check-citations.py` | OK — pages 7, sources 217, cited ids 200, no dangling refs, no coverage misses (now audits `<li>` too) |
| Exempt-region walk | Timeline alt-table cells all carry a source cell; gate/tripwire lists cite or are plan text; one uncited factual cell found (B3-5, minor); "Who is counting" rail is meta-commentary, fine |
| Smart quotes | Prose fully converted; no curly quotes inside any tag or URL (0 hits across 7 files); no primes mangled (only possessives like "7's"); `<title>`/`<desc>` clean. **But** the build emits literal `&quot;` inside generated tags on sources.html — markup corruption, B3-1 |
| Sources page 7.1/7.2 | 7.1 = s-1…s-200, every one cited at least once (checker); 7.2 = s-201…s-217, every one uncited everywhere (checker + grep), intro says "17 sources", `<ol start="201">` correct; TechRepublic (now s-106) is back in the cited list with 1 citation in case-studies — B2-23 resolution holds |
| Qualifier sample (20) | s-7 secondary, s-12/59(careers)/75 recruiting copy, s-17/24 metadata only, s-6 abstract only, s-23 (Disney blog) no qualifier, s-29(Working Backwards JSON idx) retail page only, s-33/59 vendor, s-45 via secondary, s-47/107/143 secondary, s-92 and the Wikipedia entries tertiary, s-137-class blocked/title-level, s-192-class summary only, s-217 metadata only — all correctly derived from the explicit `qualifier` field; [24→s-23] no longer mislabelled "via secondary" |
| T11 (special check) | The run renders as 30 + range 52–55 = five sources: Sky cuts [30, The Desk], Disney cuts [52, TheWrap], WBD ~1,000 layoffs [53, Variety], Paramount 2,000 layoffs [54, CBS News], WBD hub inauguration [55, Telangana Today]. **Each named company's headcount cut is supported** — B2-10 fully applied |
| Cost table (special check) | Only sourced numbers: 25–40% premium [47, HRKatha, verbatim "25 to 40 per cent"] in the derivation and Phase-0 bands row; 9.8% / 21% wage inflation and 18–25% backfill [51, Zinnov]. Every other figure ($60–100k, 30–40% margin, 1.3× load, $110–140k, $220k, 0–25% fee, ~20%) sits under `{assumption}` with "assumed" in the basis column — no invented number carries a citation |
| Walk-throughs | All three changes are `{judgment}` with hand-off counts; only [42] (Team Topologies key concepts) cited, on the X-as-a-service definition — no invented citations. "India decides unilaterally in Phase 1" column is plan text; its only factual citations ([41] Team API, [20 23 42] interface precedent, [15 45] Bird/Thompson, [43 44] Disney/Paramount T7 argument) check out; [16] on the QoE row is loose — B3-6 |
| Genericization | Clean. No employer, person, or email anywhere in docs/ (grep); footer says "Identifying details are generalized"; company references are all to the case-study companies |

**Blocking items: 2 — B3-1 and B3-2.** The site does **not** yet meet the zero-blocking exit criterion. Both are mechanical, single-line fixes (one f-string in `build.py`; one citation key in the charter-evidence fragment), and nothing else found this cycle blocks.

---

## Part 1 — Verification of cycle-2 fixes

| # | Fix | Status | Where checked |
|---|---|---|---|
| B2-1 | Target quotation "resting with" | **Applied** | index 1.1 pull quote and CE §5.2 Target card both read "…ownership of outcomes resting with where the center of gravity for the capability sits." [16] |
| B2-2 | Larson span misattribution on Applying It §4.5 | **Applied** (by rewrite: §4.5 now opens "Larson's floor of six and ceiling of eight, and McKinsey's rule that span follows standardization (Foundations §3.6, §3.11)"[48 49]; the "three to five / five to eight" sentence is gone; Foundations carries the correct book/post split: [48] post 6–8/"never more than eight", [128] book 3–5 hands-on/"transitory"/"cavalier") | applying-it §4.5; foundations §3.6, §3.7 |
| B2-3 | `data-cite="none"` on the LP dropped list; script audits `<li>` | **Applied** | `tools/content/learning-plan.html` line 279 `<ul data-cite="none">`; `check-citations.py` `p_re` now matches `(?:p|li)` |
| B2-4 | 200k/110k pair removed | **Applied** | CE §5.5 row: "−80k at top-5 IT services (18 mo. to mid-2025); GCCs on track to hire 510,000+ in 2026" [47]; prose matches the proposed rewrite, cites [47 146] |
| B2-5 | Herbsleb 2025 retrospective claim | **Applied** | foundations §3.10: "reflects on the paper's influence and notes that changes … have altered how the challenges of distributed work manifest — the delay mechanism is the durable part, not the multiplier"[6]; [6] note now carries DOI 10.1109/TSE.2025.3533977 and "does not re-test the multiplier" |
| B2-6 | Citi "after a decade" | **Applied** | CE §5.6 (b): "Citi sold Citigroup Global Services to TCS in October 2008, tied to a multi-year service contract. documented [28 145]"; no "after a decade" anywhere (grep) |
| B2-7 | Track-summary citations | **Applied** | index 1.2f and applying-it §4.2: canon clause cites [19] only; the India-evidence/case-study-track sentences carry no citation and no documented chip; both paragraphs end `{judgment}` |
| B2-8 | WBD 2022 rows | **Applied** | [92] = Wikipedia WBD, qualifier "tertiary", note "added in review cycle 2 for the April 2022 merger close and the August 2022 single-service [announcement]"; Apr 2022 row cites [92 93], Aug 2022 row cites [92] |
| B2-9 | Thick-central-platform gloss | **Applied** | foundations §3.11: retrospective characterized by its named failure modes, "which is how a thick central platform ends up doing the domain work. {judgment}" [114 123]; applying-it Test 3: "the 2026 data-mesh retrospective's failure modes (unfunded domains, re-badged IT teams) are how such a boundary ends with a central platform doing domain work anyway"[45 123]; §4.5: "that arithmetic is the mesh retrospective's unfunded-domain failure mode"[123] |
| B2-10 | T11 headcount-cut citations | **Applied** | Sentence reads "cut headcount in the period covered — Disney, WBD, Sky and Paramount — and WBD stood up its hub during cuts." Raw run = 30 + 52–55 (five sources); Sky [30], Disney [52], WBD [53], Paramount [54], hub [55] — every clause supported |
| B2-11 | Disney/Paramount ads sentence | **Applied** | index version removed (1.2f now says "ads measurement is the candidate a future P&L owner would depend on"); applying-it §4.3 row: "Disney moved its streaming data platform under its ad platform in 2026 and Paramount's 2026 stack consolidation unifies user data with ad technology — the dependence argument behind T7."[43 44]; T7 itself ("during a thousand-person cut"[43]) is supported |
| B2-12 | Hotstar full-stack / Sky origin downgrades | **Applied** | CS §2.6: "full-stack, full-domain engineering org from 2015 … {inferred}[107]"; CS §2.8: origin-site sentence "{inferred}[59 75]"; Fig 2.2 alt table "origin site … {inferred}[59]"; index 1.1 keeps the accepted wording ("Sky's platform organization is where Peacock's platform came from") — residual citation-run gap noted as B3-4 |
| B2-13 | Index 1.2a chip split | **Applied** | "cross-site work items took about 2.5 times as long … {documented}[6]. Time-zone separation hurt more than distance.[24] {inferred}" |
| B2-14 | Graduation clock 10–20 | **Applied** | CE Target card "reached over roughly two decades"; §5.6 (c) "took ten to twenty years"; closing judgment "on a 10–20-year clock"; §5.2 "10–20-year stories"; index unchanged and consistent |
| B2-15 | Explicit qualifier field | **Applied in `sources.json`** (all 217 entries carry the field; [23] Disney blog renders no qualifier; Working Backwards "retail page only"; Storyboard18 [143] "secondary") — **but the rendering markup is corrupt, B3-1** | sources.json; docs/sources.html |
| B2-16 | Zurich sentence | **Applied** | CS §2.4: "whether Zurich owns YouTube's analytics function is not documented.[13] {inferred}" |
| B2-17 | Alt-table Global Networks row | **Applied** | "Split into Streaming and Studios and Global Networks (later Discovery Global) announced" [94] |
| B2-18 | Zinnov source on the 7:1–8:1 clause | **Mis-applied — B3-2** | CE §5.4 cites [32 141]; [141] (Zinnov "5 Shifts", fetched this cycle) contains neither "7:1" nor "pyramid"; the ratio is on [40] (Zinnov talent blog), which the §5.5 table row cites correctly |
| B2-19 | Pay-premium caveat cell | **Applied** | "HRKatha, citing EY GCC Pulse 2025; the EY release itself gives no premium figure.[47]" — no duplication, no [148/146] |
| B2-20 | Row label proxy | **Applied** | CE §5.5: "AI / cloud roles (proxy for data roles)"; index T2: "AI and cloud roles — the closest published proxy for data roles" |
| B2-21 | X-as-a-service wording | **Applied** | index 1.2e: "the minimal-collaboration interaction mode Team Topologies calls X-as-a-service: the provider evolves the service on its own roadmap.[42]" |
| B2-22 | Fig 3.1 caption | **Applied** | caption cites [6 15 18 35 45] — Bird ([15]) included for the Vista line |
| B2-23 | TechRepublic placement | **Applied** | now s-106, cited once (case-studies); build recomputes the split; 7.2 holds exactly the 17 uncited entries |
| B2-24 | McKinsey note | **Applied** | note: "The page's facilitator paragraph is mislabelled 'supervisor' (McKinsey typo); ranges read in a browser 2026-08-30" |
| B2-25 | Forrester 2011 chip split | **Applied** | CE §5.6 (d): "consultant constructs documented [151] with no documented follow-up. inferred" |

## Part 2 — Spot checks that came back clean (for the record)

- Index "In two minutes": 55,000 [3]; 56/44 and the tier split [5]; 2.5× stat card [6]; 86% (1.2c) [4]; Amazon dependencies [7]; the five-hub sentence's run is a true seven-source range 8–14 (Warsaw [8], London [9], Hyderabad [10], Bengaluru [11], WBD hub [12], Zurich [13], Echo Nest/Boston [14]); "as at Google, Spotify, Netflix and Disney" is the range 20–23, one source per company; cost line is `{judgment}` and matches the §4.5 table (+$1.5–3.0M / +$0.5–1.5M with offset / $1.6–4.4M one-time).
- Drill-downs 1.2a–1.2f: every factual clause cited or chip-tagged; Hotstar "record concurrency" (no figure) [1]; 27% sentence appears once on index and once on CE, both with "the method behind that figure is not published"; 1.2b Citi/stagnant/Sky trio [28 30] `{inferred}`; 1.2c matches B26/B2-14 wording.
- Phases 0–3 and Gates 0–3: Phase 0 cites [40] (veto/first-hires), [29] (vendor release), [46] (Team APIs), [47] (25–40% bands); Phase 1 [7 15 48]; Gate 3 [49] (≤8 directs); gate criteria are plan text; the T1-path arithmetic in Fig 1.2 (3/9/18/30 vs 6/12/21/33) is internally consistent.
- T1–T12: T2 [29 51], T3 [15], T4 [6], T5 [35], T6 [7], T7 [43], T8 [17 24], T9 [29 — "can quickly sag" verbatim], T10 [40], T12 `{folklore}{judgment}` uncited — all support their clauses.
- CE §5.1: 2,117/3,728/2.36M/$98.4B [5]; 1,700/1.9M/$64.6B [142]; ~110 [141 — verbatim "~110 new GCCs … between early 2024 and late 2025", re-fetched]; >120 since Jan 2023 and 35% mid-market [143]; Everest 452 / ~50 sold of 1,450 [29]; the Forrester 2007 paragraph [144] and divestiture cohort [28 145].
- Case Studies pull quote: "…the best way to fail at inventing something is by making it somebody's part-time job." — verbatim match to C1-31's quotation in `research/c1-streaming-native-case-studies.md`, attributed "Bryar & Carr, as summarized by Schuler" [7], and the §2.5 prose keeps the "as summarized by Schuler … {inferred}" framing.
- WBD alt-table 2022 rows [92], June 2025 row [94], and the §2.7 prose all agree.
- Fig 4.1 desc / alt table / index 1.2f table / judgment box agree on every mark, including the four "?" cells (ML, fraud, ads, commerce).
- Fig 4.3 UTC arithmetic re-checked: PDT 16:00–01:00, EDT 13:00–22:00, IST 03:30–12:30; 9.5–13.5 h; ≤2.5 h stretched.
- §4.7 sensitivity table: all `{judgment}`/assumption, no citations, and the 60-contractor row invents no vendor-placement claim ("this memo does not know").

## Part 3 — Numbered findings

Severity: **blocking** = wrong/fabricated claim, invented citation, broken URL, uncited factual claim, quote corruption, or a cycle-2 fix not applied; **minor** = wording/cosmetic.

### Blocking

**B3-1 · blocking · docs/sources.html (build output; `tools/build.py` `entry_html`)**
Finding: the generated markup contains literal `&quot;` inside tags: `<span class=&quot;who&quot;>— …</span>` for every note (137 occurrences) and `<span class=&quot;q&quot;>…</span>` for every qualifier chip. In HTML5 these parse as unquoted attribute values, so the class becomes the literal string `"who"` / `"q"` (quote characters included) and the `.who`/`.q` styling never applies — the B2-15 qualifier labels and every source note render as malformed, unstyled spans. This is quote corruption in the served page, introduced by writing HTML-escaped quotes into the Python f-string:
`f'{(" <span class=&quot;who&quot;>— " + note + "</span>") if note else ""}'` and `("<span class=&quot;q&quot;>" + q + "</span>")`.
Fix: in `tools/build.py` `entry_html`, emit real quotes — `' <span class="who">— ' + note + '</span>'` and `'<span class="q">' + q + '</span>'` — and rebuild. One function, two substrings.

**B3-2 · blocking · charter-evidence.html §5.4 Leadership seeding (B2-18 mis-applied)**
Finding: "Zinnov's version is the 7:1–8:1 candidate ratio and hiring across the pyramid.[32 141]" — [141] (Zinnov "5 Shifts", fetched 2026-08-30) contains neither "7:1"/"8:1" nor the pyramid point; the ratio is on [40] (Zinnov, "What No One Tells You About GCC Talent"), which the §5.5 table row cites correctly ("Candidate-to-hire ratio | 7:1 – 8:1 | Zinnov.[40]"). Cycle-2's B2-18 asked for exactly this source; the applied citation points at the wrong Zinnov page.
Fix: change the fragment's citation key so the clause cites the talent blog (renders [32 40]).

### Minor

**B3-3 · minor · foundations.html §3.5 pull quote**
"…organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." — Conway's 1968 sentence has "(in the broad sense used here)" between "systems" and "are constrained"; the omission is unmarked. The body-text quotation in §3.4 (starting "are constrained…") is verbatim and fine. Fix: "…organizations which design systems … are constrained to produce…" or restore the parenthetical.

**B3-4 · minor · index.html §1.1 "Why this shape"**
The `{documented}` run [8–14] covers the five hubs, Zurich [13] and Boston [14], but the same sentence's "Sky's platform organization is where Peacock's platform came from" and "Hotstar was a home-market product" clauses have no source in the run (Sky = [59], Hotstar = [1]); Case Studies tags the Sky-origin claim `{inferred}`. The wording matches the accepted B2-12 disposition, so this is a residual citation-coverage note, not a re-litigation. Fix (optional): extend the run with [1] and [59], or end the documented run before the "four other cases" clause.

**B3-5 · minor · index.html §1.2f scoring table, "Fraud and paid sharing" row**
Cell: "Largest: paid-sharing enforcement drove the 2023–25 P&L turns" — a causal factual claim with no citation anywhere on the site (the Netflix case study explicitly declines to tie anything to the paid-sharing push). The table is announced as the memo's scoring under a visible `{judgment}` chip, and the Applying It twin sits inside the labelled Judgment box, which is why this is minor rather than blocking. Fix: cite it if a source is added, or soften to "Largest — the outcome a CFO noticed industry-wide in 2023–25".

**B3-6 · minor · applying-it.html §4.3 QoE row, interface cell**
The cell describing the memo's own decision-rights design ("a decision-rights table under which the staff-level India QoE analytics lead decides definitions … the India roadmap enters the annual plan.[16]") cites the Target interview, which contains none of this plan. Same category-error shape as B2-7, at table-cell scale. Fix: drop [16] or reword to "…per Target's operating rule[16]".

**B3-7 · minor (cosmetic, safe to ship) · docs/sources.html**
(a) A few entries render the qualifier twice — once from the note ("— Tertiary") and once as the chip ("tertiary") — e.g. s-1. (b) Source metadata (titles, notes, the per-page src-index previews) keeps straight apostrophes/quotes while all prose is typographic; if deliberate (verbatim metadata), leave it, but it reads as an inconsistency next to the converted prose. Neither affects correctness.

---

## Verdict

**Not zero blocking: 2 blocking items (B3-1, B3-2).** Both are single-line mechanical fixes — two substrings in `build.py`'s `entry_html` plus a rebuild, and one citation key in the charter-evidence fragment. Everything else opened this cycle verified: all 25 cycle-2 fixes are otherwise in place, the 45+ sampled claims are supported or visibly judgment/assumption, the coverage checker and exempt-region walk are clean, the 7.1/7.2 split is exact, the qualifier sample is correct, and genericization holds. On a re-run after those two fixes, I expect to report zero blocking items.
