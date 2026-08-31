# Cycle 4 — Reviewer C (editor), verification round

Read: `research/recommendation.md` constants table (the cycle-3 revision: cost +$1.7–3.5M/yr, +$0.1–1.9M vs boutique, T12 ≈ $5.0–6.3M; schedule G0 months 3–4 / no later than 6, G1 = first fiscal-quarter boundary at or after G0 + 6, best case 3/9/18/30, failed Gate 1 re-judged at the next quarter boundary with T11 on the announcement), then every `docs/*.html` as text, with raw-HTML spot checks on Foundations §3.4 and Fig 1.2's SVG. Scanning by Python over tag-stripped extracts; word counts exclude citation superscripts and tag chips.

## Verdict

**Not zero blocking.** Nine of the eleven cycle-3 items are verified fixed on the served pages (C3-1, C3-2, C3-3, C3-5, C3-6, C3-8, C3-9, C3-10, and C3-11's substance). But two are regressions-in-place — C3-4's fix was pasted in without the trimming its edit specified, and C3-7's fix was half-applied, leaving the Conway sentence twice in adjacent blocks — and the constants re-check finds Applying It §4.5 still serving the **pre-A3-2 cost numbers** and Applying It §4.3 still serving the **pre-A3-3/A3-4 schedule wording**, both of which the cycle-3 responses claimed updated. Two blocking items (C4-1, C4-2), three major (C4-3, C4-4, C4-5), one minor (C4-6).

---

## Part 1 — Verification of C3-1…C3-11

| # | Was | Verified? | Served text |
|---|---|---|---|
| C3-1 | blocking | **Fixed** | Index §1.4: "…and half-ownership as a category after Gate 0, with two written exceptions: **the QoE facilitating-mode window and tripwire T3's time-boxed narrowing** (Applying It §4.4)." Fig 1.2 caption: "the two written exceptions — **the QoE facilitating-mode window and tripwire T3's time-boxed narrowing** — are named as exceptions so they cannot become the rule." Zero occurrences of "definition contract" anywhere on the site. Both locations now name the same pair as Applying It §4.4 and the memo. |
| C3-2 | blocking | **Fixed** | Foundations §3.9 rail: "Applying It scores it: **quality of experience goes first on the assumed baseline, with a month-3 re-decision — if counsel clears fraud and the contractors sit in commerce, fraud goes first instead. Otherwise fraud, ads measurement or ML-platform expansion is the month-18 decision**, and the legal review decides which is even eligible." All three Phase 3 candidates; the re-decision present. |
| C3-3 | blocking | **Fixed** | Learning Plan, Kohavi entry: "…which is why the engine — **assignment, exposure logging, metrics computation, and the metric-definition schema with its change process — moves**, and the analysis, the semantic catalog and the review gate stay central as its customers." The v3 line, verbatim in substance. |
| C3-4 | blocking | **Fixed, with a regression** | Charter Evidence §5.5: "The Recommendation's gate is therefore **in heads**, and narrower than the gross rate on purpose: **no more than three regretted departures from the converted cohort in the first year (tripwire T2), with retention grants vesting at G1 + 9 and G1 + 21** — months 18 and 30 on the happy path — as the instrument behind it." No "25% annualized" remains anywhere. But the edit's closing instruction ("minus its duplicate backfill clause") was not executed — see **C4-3**. Also carries "happy path" — see **C4-5**. |
| C3-5 | blocking | **Fixed** | Learning Plan milestone table: "Gate 2→3 / Phase 3 decision (G1+9) | **Playback engineering has decommissioned its own QoE computation and its SLOs read India's tables; at least three India-authored definition changes adopted**; the decision between fraud, ads measurement or ML-platform expansion is made | 18". Matches index Gate 2 and the memo. |
| C3-6 | major | **Fixed** | Applying It §4.2 box: "…and the site is a platform site — **acceptable as a site, a failure of this memo's bet, costed in §4.5**." Zero "not an acceptable outcome" on the site; consistent with index Phase 2's "acceptable as a site, and a failure of this memo's bet, costed at one senior backfill." |
| C3-7 | major | **NOT fixed — regression** | The pull was moved up to open §3.4, but the inline blockquote it was to replace was **not deleted**: the two now sit back-to-back. See **C4-4**. |
| C3-8 | major | **Fixed** | All six cuts verified on the index (quotes in Part 3). Section now 538 prose words, 604 with rail (47) and pull quote (19) — ≈ 2:09 / 2:25 at 250 wpm, at the accepted ≈2:05 floor within counting noise. Accepted-as-is per the cycle-3 disposition; no further cuts proposed. |
| C3-9 | minor | **Fixed** | Tag key on all six pages: "judgment — **this memo's position, not a sourced fact**." Zero "our position" on the site. |
| C3-10 | minor | **Fixed** | Learning Plan: "Dissolution announced | The US QoE team's **dissolution at G1** announced (G1 − 3 is month 6 on the happy path), **with retention to G1 + 3** | 6". Phase-relative as required; the "happy path" label is part of C4-5. |
| C3-11 | minor | **Fixed in substance; one residue** | Fig 1.2 swimlane: "**Fraud · ads · ML expansion** / decided at **gate 2**" — all three candidates as the disposition promised, but "gate 2" is lowercase while every other label on the page capitalizes Gate ("Gate 0", "Gate 1", "Gate 2", "Gate 3" markers in the same SVG). See **C4-6**. |

## Part 2 — Constants re-check (memo constants table, cycle-3 revision)

**Cost.**
- Index §1.1 (two-minute): "**$1.7–3.5M a year more than an MSA-offshore vendor mix** — the site is not cheaper, it is a different thing — with the offset scenario **removing $1.1–1.8M** of that … plus **$1.6–4.4M one-time**" ✓ matches the memo.
- **Applying It §4.5: ✗ — the pre-A3-2 numbers are still served.** See **C4-1**. Three locations: the run-rate row, the CFO sentence, and the T12 one-time subtotal. "$0.1–1.9M" and "$5.0–6.3M" appear nowhere on any served page.
- Index unwind sentence ("re-formed US teams, vendor re-engagement and India severance, order $1.5–3M, not the remaining budget") is the **unwind** cost per A3-12, a different quantity — correct as served; do not "fix" it to $1.7–3.5M.
- Learning Plan Primer entry now carries no number ("a site that costs more than the vendor did is not yet faster than the vendor was") — consistent by omission ✓.

**Schedule.**
- Index §1.3: "target **months 3–4 (best case; the modal case is 4–6), no later than month 6**" ✓; phase ledger: "G1 = **first fiscal-quarter boundary at or after G0 + 6**" ✓; "If Gate 1 fails — on performance or on the managers-started criterion — the failing criterion is named, the gate is **re-judged at the next quarter boundary, and the T11 mechanism applies to the Phase 2 announcement**" ✓ (index is the only page stating the failure rule; it states it as the memo does).
- **Applying It §4.3: ✗ — pre-A3-3/A3-4 wording still served.** See **C4-2**.
- Charter Evidence §5.5: vesting "at G1 + 9 and G1 + 21 — months 18 and 30" ✓ (label drift only).
- Learning Plan intro: "Gate 0 at month 3 (no later than 6), Gate 1 at 9, Gate 2 at 18, steady state at 30 … if Gate 0 slips to month 6, everything after it slips three months" — numbers ✓ (label drift only). Milestone months 1/3/6/9/12/18 consistent with the best-case calendar ✓.
- Fig 1.2: calendar rows carry **3 / 9 / 18 / 30** and **6 / 12 / 21 / 33** ✓; gate markers carry the v3.1 criteria (two manager shortlists at Gate 0; EMs started, decisions halved, ≤2 regretted at Gate 1; decommissioned + ≥3 adopted at Gate 2) ✓. But the first calendar row is labeled "**Happy path**" — see **C4-5**.

**Other constants spot-checked identical:** exceptions pair (C3-1 above); experimentation line (index §1.2e, Applying It §4.2/§4.3, Learning Plan Kohavi all state runtime + definition schema + change process, US analysis as customer) ✓; cohort gates in heads (≤2 Phase 1 by G1 on index Gate 1 and Fig 1.2; ≤3 converted first year on Charter Evidence) ✓; three Phase 3 candidates on every page that names them (index, Applying It Fig 4.2 note, Foundations rail, Learning Plan ×2, Fig 1.2 swimlane) ✓.

## Part 3 — Regression sweep on the cycle-3 edits

- **The reworded two-minute section reads cleanly.** The Amazon sentence now ends at the diagnosis: "Dependencies, not team size, were the failure mode Amazon diagnosed in its own teams." — the trailing half-ownership clause is gone and the paragraph does not dangle. The "Why this shape" sentence absorbed its two added citations without a seam: "…the four other documented sites are different cases — Zurich grew in over about eighteen years, Sky is where Peacock's platform came from, Boston was acquired, Hotstar was a home-market product. [1][8][15]". The other four cuts verified: "makes ownership diffuse by design, and diffuse ownership is the best-replicated defect predictor in the literature"; "Target's India president put the working rule in one sentence — one interview, and…"; "as at every case-study company that published; the engine is a capability India can own"; "so there is a month-3 re-decision: if counsel clears fraud and the contractors sit in commerce, it goes first; otherwise fraud or ads measurement is the month-18 decision."
- **Voice:** zero "our position", "hedge", "landing", "load-bearing", "first draft", "says so". "actually" survives only inside Kniberg's quotation (Case Studies). One "managerial leverage" in the Learning Plan's Grove entry — Grove's own term of art in a book description, not the banned metaphor; note, no item. Zero `&quot;` in any served file (B3-1 holds; 92-note styling intact).
- **New duplications introduced by the edits:** two, both filed (C4-3, C4-4).

---

## Part 4 — Cycle-4 items

### Blocking

**C4-1 — Applying It §4.5 still serves the pre-A3-2 cost numbers; the site contradicts itself on the headline cost.**
Severity: blocking (constants drift and cross-page contradiction on the cost of the whole plan; the A3-2 blocking finding, claimed fixed "index §1.1 **and Applying It §4.5** updated", is still live on one of the two pages).
Locations, all in Applying It §4.5:
1. Run-rate row: "Run-rate, before any offset | $2.4–4.0M | $4.1–5.9M | **+$1.5–3.0M a year against an MSA-offshore mix; roughly +$0.5–1.5M against a boutique mix**". The memo's row is the table's own subtraction: "**+$1.7–3.5M/yr against a $2.4M MSA-offshore mix; +$0.1–1.9M against a $4.0M boutique mix — the subtraction of the two columns, nothing else**". The served deltas are not the subtraction of the served columns (4.1−2.4 = 1.7; 5.9−2.4 = 3.5; 4.1−4.0 = 0.1; 5.9−4.0 = 1.9) — the exact arithmetic error A3-2 flagged.
2. CFO sentence: "on the assumed baseline this costs **$1.5–3M** a year more than the vendor … with the offset, **+$0.5–1.5M**; against a boutique-heavy mix, **closer to neutral**." Memo: +$1.7–3.5M; offset removes $1.1–1.8M; +$0.1–1.9M vs boutique.
3. One-time total: "One-time total — $1.6–4.4M **T12 path: up to $6.8M**". Memo (A3-13): "T12 path, from its own lines … ≈ **$5.0–6.3M** plus two engineer-quarters for runbooks". "$5.0–6.3M" appears nowhere on the site.
Index §1.1 states the v3.1 numbers correctly, so index and Applying It currently disagree on the memo's single most-quoted figure.
Edit: replace the three locations with the memo's own text (constants table and §4.5 table rows, quoted above).

**C4-2 — Applying It §4.3 still serves the pre-A3-3/A3-4 schedule wording.**
Severity: blocking (constants drift on the gate definitions; the "after" vs "at or after" distinction is the substance of A3-3 and can move G1 by a full quarter).
Locations, all in Applying It:
1. Ownership-table caption: "Phases are offsets from G0 (**Gate 0, target month 3**) and G1 (**the first quarter boundary after G0+6**); **happy-path** months in parentheses." Memo: G0 target months 3–4, no later than 6; G1 = first fiscal-quarter boundary **at or after** G0 + 6; the calendar label is "best case".
2. Critical-path line (§4.5 Phase 0 plan): "Gate 1 at **the first quarter boundary after G0+6**." Same "at or after" omission.
Edit: caption → "Phases are offsets from G0 (Gate 0, target months 3–4, no later than 6) and G1 (the first fiscal-quarter boundary at or after G0 + 6); best-case months in parentheses." Critical path → "…Gate 1 at the first fiscal-quarter boundary at or after G0 + 6."

### Major

**C4-3 — The C3-4 fix was applied without its trimming instruction; Charter Evidence §5.5 now says the same two things twice in consecutive sentences.**
Severity: major (duplication introduced by a cycle-3 edit; the box reads as a copy-paste accident).
Location: Charter Evidence §5.5: "…Regretted departures are a subset of the 18–25% gross rate; **the gate detects a vendor-controlled or under-banded transfer, and the backfill line (Applying It §4.5) absorbs normal churn.** At 18–25% on a converted cohort of 30–35, expect 12–18 departures by month 30 regardless; **the gate detects a vendor-controlled or under-banded transfer, it does not prevent normal churn, which is why the plan carries a backfill line for it (Applying It §4.5).**"
Edit: end the closing sentence at the fact it alone carries: "At 18–25% on a converted cohort of 30–35, expect 12–18 departures by month 30 regardless." (The preceding sentence already states the gate's purpose and the backfill pointer once.)

**C4-4 — C3-7 half-applied: Foundations §3.4 opens with the Conway sentence twice, back-to-back.**
Severity: major (the original C3-7 defect, made more visible: the styled pull was moved up as directed, but the inline blockquote it replaces was not deleted, so the pull and the old blockquote are now adjacent siblings).
Location: `docs/foundations.html`, §3.4, immediately after the rail:
```
<blockquote class="pull">…organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations.<span class="who">Melvin Conway, 1968…</span></blockquote>
<blockquote><p>Organizations "are constrained to produce designs which are copies of the communication structures of these organizations."…</p></blockquote>
```
Edit: delete the second (plain) blockquote; the pull stays as the section opener. One pull per essay page then holds site-wide.

**C4-5 — "Happy path" survives on three pages and inside Fig 1.2, where the memo now says "best case" — including a same-page inconsistency on the index.**
Severity: major (constants-vocabulary drift across pages after A3-3's relabel; the memo contains zero "happy path").
Locations: index Fig 1.2 SVG calendar-row label "**Happy path**" and the figure's alt summary ("two calendar rows underneath for the **happy path** and the T1 path") — while index §1.3 prose on the same page says "Two calendars are shown: the **best case** and the tripwire-T1 path"; Applying It §4.3 caption ("**happy-path** months in parentheses" — covered in C4-2); Charter Evidence §5.5 ("months 18 and 30 on the **happy path**"); Learning Plan ×4 (intro "the Recommendation's **happy path**", milestone header "Month (**happy path**)", dissolution row "month 6 on the **happy path**", calendar intro "One month per row on the **happy path**").
Edit: "best case" (noun) / "best-case" (modifier) at all seven spots; Fig 1.2 row label → "Best case".

### Minor

**C4-6 — Fig 1.2's swimlane sub-label reads "decided at gate 2", lowercase.**
Severity: minor (residue of C3-11's edit; the same SVG's gate markers all capitalize "Gate").
Edit: "decided at Gate 2".

### Notes, no item

- The memo's status line still reads "decision memo, **v3** (after review cycle 2…)" while the cycle-3 responses call it v3.1 and its constants are the v3.1 constants. Bookkeeping only; bump the label when the file is next touched.
- Standing accepted-as-is items untouched, as instructed: Applying It length, the two-minute section at ≈2:05–2:10, caption lengths, verbatim straight quotes in source metadata.
- Index's "$1.5–3M" (unwind cost, §1.5/T10 block) is correct per A3-12 and must not be caught by a global find-and-replace when fixing C4-1.

## Final verdict

**Not zero blocking.** Two blocking items (C4-1 cost, C4-2 schedule — both Applying It pages of fixes the cycle-3 responses claimed applied but that are not in the served HTML), three major (C4-3, C4-4, C4-5), one minor (C4-6). Everything else verified fixed; the fixes are mechanical, mostly the memo's own sentences pasted into `docs/applying-it.html`, plus one deleted blockquote, one trimmed sentence, seven label changes, and one capital letter. A cycle-5 verification pass on those two files should close.
