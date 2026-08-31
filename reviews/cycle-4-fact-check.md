# Cycle 4 — Fact-check verification round (Reviewer B)

Date: 2026-08-30. Scope, per the verification brief: re-open B3-1 … B3-7 against the served pages; re-run `check-citations.py`; scan for `</sup>` immediately followed by a letter/quote/paren; spot-check ten claims touched by the cycle-3 edits; confirm no genericization regression. Source numbers below are the currently rendered `s-N` numbers; `C5-x` are the citation keys in `tools/content/` and `research/sources.json`.

## Summary

Five of the seven B3 items verify. **One blocking cycle-3 fix (B3-2) was not applied**, and the cycle-3 responses' A3-2 disposition ("Applying It §4.5 updated") is also unimplemented on the page it names, leaving a cross-page contradiction in the headline cost number. One minor fix (B3-5) is applied on two of its three claimed locations.

| Check | Result |
|---|---|
| B3-1 … B3-7 verification | 5 verified; **B3-2 not applied (blocking, → B4-1)**; B3-5 applied on index + memo, not on Applying It (→ B4-3, minor) |
| `python3 tools/check-citations.py` | **OK** — pages 7, sources 217, cited ids 200; s-201…s-217 uncited by design (§7.2 further reading) |
| `</sup>` followed by letter/quote/paren | **0** across all 7 docs pages (Python scan, letters + straight/typographic quotes + parens) |
| Spot checks (10) | 9 clean; 1 fails — the §4.5 run-rate delta and CFO sentence (→ B4-2, blocking) |
| Genericization | **Clean** — no employer, person or email in docs/ (grep for name/address patterns); "Identifying details are generalized" footer present; company references are case-study companies only |

**Verdict: NOT zero blocking** — B4-1 and B4-2 below.

---

## Part 1 — B3 verification table

| # | Cycle-3 finding | Claimed fix | Verified? | Evidence |
|---|---|---|---|---|
| B3-1 | `&quot;` inside generated tag attributes on sources.html; `.who`/`.q` styling never applies | `entry_html` rewritten with real quotes; rebuilt | **Yes** | `grep -c 'quot;'` on `docs/sources.html` = 0 (so `quot;who`, `quot;q`, `class=&quot;` all 0). 309 `class="who"` spans, 34 `class="q"` chips; `.src .who` and `.src .q` rules present in `docs/assets/site.css` (lines 313, 317). |
| B3-2 | §5.4 clause "Zinnov's version is the 7:1–8:1 candidate ratio…" cites the wrong Zinnov page (5 Shifts) instead of the talent blog | Citation key changed to the talent blog (C5-9) | **NO — not applied** | See B4-1. |
| B3-3 | Conway pull quote omits "(in the broad sense used here)" unmarked | Parenthetical restored | **Yes** | `docs/foundations.html`: the styled pull reads "…organizations which design systems (in the broad sense used here) are constrained to produce designs…". |
| B3-4 | Index "four other cases" clause lacked Sky and Hotstar sources in its run | Run extended with the Sky and Hotstar citations | **Yes** | `docs/index.html` §1.1: the clause's run is [1, 8, 15] — Hotstar = s-1 (Disney+ Hotstar), Sky-origin = s-8 (AWS Peacock case study, the same source Case Studies uses for "the site the Peacock platform came from"), Boston = s-15 (Echo Nest). |
| B3-5 | Uncited causal cell "Largest: paid-sharing enforcement drove the 2023–25 P&L turns" | Softened to "Largest — the outcome a CFO noticed industry-wide in 2023–25" on the index, Applying It and the memo | **Partial** | Index §1.2f table row (line 237) and `research/recommendation.md` line 51 carry the softened wording (memo adds `[judgment]`). Applying It still carries the causal claim — see B4-3. |
| B3-6 | Applying It §4.3 QoE interface cell cited the Target interview ([16] then; s-17 now) for the memo's own plan | Citation dropped | **Yes** | §4.3 table (lines 201–214): no `s-17` anywhere in the table; the QoE interface cell ("…a decision-rights table under which the staff-level India QoE analytics lead decides definitions…") is uncited plan text. |
| B3-7 | (a) Qualifier rendered twice (note + chip); (b) straight quotes in source metadata | (a) Build strips a note's leading qualifier word; (b) accepted-as-is (verbatim metadata) | **Yes** | Scripted pass over all 34 chips: 0 cases where the note's first word repeats the chip (checked all chip values incl. tertiary ×11, secondary ×5, vendor ×4). No note begins "Tertiary"/"Secondary"/"Vendor". (b) is the standing accepted-as-is rule; not re-litigated. |

## Part 2 — Mechanical checks

- `python3 tools/check-citations.py` → `RESULT: OK`, exit 0. pages 7 · sources 217 · cited ids 200; the 17 uncited ids are exactly s-201…s-217 (the further-reading block).
- `</sup>` followed immediately by a letter, quote (straight or typographic) or paren: **0 matches** across `docs/*.html` (Python regex scan, all 7 files).

## Part 3 — Spot checks on cycle-3-edited claims

1. **Index §1.1 cost headline** — "$1.7–3.5M a year more than an MSA-offshore vendor mix… offset removing $1.1–1.8M… plus $1.6–4.4M one-time": no citation, sits under a visible `{judgment}` chip, and matches the table's own subtraction ($4.1–5.9M − $2.4M = +$1.7–3.5M; − $4.0M = +$0.1–1.9M). Clean on the index and in `recommendation.md` (lines 125, 135, 230). **Fails on Applying It §4.5 — see B4-2.**
2. **§4.5 derivation labels** — every unsourced figure ($60–100k seats, 30–40% vendor margin, 1.3× load, $58–77k loaded, $0.2–0.3M stipends, $0–0.6M severance) carries "assumed"/derivation basis; only sourced figures cite (25–40% premium [48 HRKatha], signing/backfill [52 Zinnov]). No invented number carries a citation.
3. **Gate 2 "adopted" definition (index, line 390)** — "at least three changes the US adopted: at least one a metric (not dimension) change, each altering a playback SLO threshold, a release-gate criterion, or an executive-reported number" — plan text, no citation.
4. **Gate 2 attestation scope (index)** — "the attestation names systems: no QoE computation in the player SDK, the observability stack, or a third-party QoE service used for playback decisions, other than as an India-owned contract" — plan text, no citation. Learning Plan Gate 2 row states the decommissioning-plus-three-adopted-changes gate, uncited.
5. **T9 unwind cost** — "re-formed US teams, vendor re-engagement and India severance, order $1.5–3M, not the remaining budget" — fallback plan text, uncited; the only citation in T9 is the verbatim "can quickly sag" quote [30, CIO]. Visibly the memo's own figure.
6. **Gate 1 failure rule (index)** — "If Gate 1 fails — on performance or on the managers-started criterion — the failing criterion is named, the gate is re-judged at the next quarter boundary, and the T11 mechanism applies to the Phase 2 announcement." Plan text, no citation.
7. **G1 definition and gloss** — "G1 = first fiscal-quarter boundary at or after G0 + 6"; "a one-month Gate 0 slip can cost three" (index line 306) — both present, uncited plan text.
8. **G0 target restated** — "target months 3–4 (best case; the modal case is 4–6), no later than month 6" — present, judgment-tagged paragraph.
9. **T12 fallback** — `{folklore}{judgment}`, uncited; the fallback's own lines (net-new hiring, +12–18 months, double-running $2.4–3.6M under T12, two engineer-quarters for runbooks, one-time "up to $6.8M" in the §4.5 table) are plan text. The ≈$5.0–6.3M T12 subtotal appears in the memo (`recommendation.md` line 230), which is where A3-13 landed.
10. **Boutique-saving margin assumption (§4.5)** — "a $60k bill rate at a 30–40% vendor margin pays the engineer $36–42k… Against a boutique-heavy mix billing $80–100k a seat, conversion is a per-head saving" — the margin assumption is stated and marked assumed; premium cited to [48].

## Part 4 — Regressions / unapplied fixes

**B4-1 · blocking · charter-evidence.html §5.4 (B3-2 not applied)**
The clause still reads "…Zinnov's version is the 7:1–8:1 candidate ratio and hiring across the pyramid." citing **[33 141]** — s-141 is Zinnov "5 Shifts Defining India's GCCs Story in 2025", the exact page B3-2 established (fetched 2026-08-30) contains neither the ratio nor the pyramid point. The ratio is on s-41, "What No One Tells You About GCC Talent", which the §5.5 table row ("Candidate-to-hire ratio | 7:1 – 8:1 | Zinnov.[41]") and the post-table prose ([33 41]) correctly cite. Root cause: `tools/content/charter-evidence.html` line 63 still carries `C5-6` + `C5-3`; `research/sources.json` confirms C5-3 = the 5 Shifts blog and C5-9 = the talent blog. The cycle-3 response claims the clause "now cites the Zinnov talent blog (C5-9)" — it does not; the fix was never made in the fragment (the other two 7:1 occurrences already cited C5-9 at cycle 3).
Fix: in the fragment's §5.4 clause, change `C5-3` → `C5-9` (renders [33 41]); rebuild.

**B4-2 · blocking · applying-it.html §4.5 (A3-2 disposition unimplemented on the page it names)**
The cycle-3 response for the blocking arithmetic item A3-2 says "CFO sentence, constants, index §1.1 **and Applying It §4.5** updated." Index §1.1 and the memo carry the corrected subtraction (+$1.7–3.5M vs the $2.4M MSA mix; +$0.1–1.9M vs the $4.0M boutique mix; offset removes $1.1–1.8M). But §4.5 itself — the table the index points to ("Table: Applying It §4.5") — still shows the old numbers:
- Run-rate row delta cell: "+$1.5–3.0M a year against an MSA-offshore mix; roughly +$0.5–1.5M against a boutique mix" (should be +$1.7–3.5M / +$0.1–1.9M, the subtraction of its own two columns);
- CFO sentence: "this costs $1.5–3M a year more than the vendor… with the offset, +$0.5–1.5M; against a boutique-heavy mix, closer to neutral" (should be $1.7–3.5M; with the offset it does not reduce to the boutique delta).
The offset row **was** updated (−$1.1–1.8M a year), so §4.5 now disagrees both with the index/memo and with its own offset row ($1.7–3.5M − $1.1–1.8M ≠ $0.5–1.5M except by coincidence of the old constants). Same stale text in `tools/content/applying-it.html` (2 occurrences).
Fix: update the run-rate delta cell and the CFO sentence in the fragment to the corrected figures; rebuild.

**B4-3 · minor · applying-it.html "Why not fraud first" (B3-5 applied on 2 of 3 claimed locations)**
Line 190, inside the labelled Judgment box: "…it is the outcome a CFO notices: **paid-sharing enforcement drove the 2023–25 streaming P&L turns**." The uncited causal claim B3-5 flagged survives here verbatim, though the disposition says the softening was applied "on the index, Applying It and in the memo" (index and memo verified softened). Minor for the same reason B3-5 was minor — it sits inside the labelled Judgment box — but the causal clause remains uncited anywhere on the site.
Fix: soften to the index wording ("the outcome a CFO noticed industry-wide in 2023–25") or add a source.

## Verdict

**NOT zero blocking.** B4-1 (B3-2 never applied; a wrong citation on a factual claim) and B4-2 (the served §4.5 contradicts the index headline and its own offset row on the memo's central cost number) block; B4-3 is minor. All three are single-spot fragment edits plus a rebuild; everything else from cycle 3 — B3-1, B3-3, B3-4, B3-6, B3-7, the checker, the sup-spacing scan, the Gate/tripwire spot checks and genericization — verifies clean.
