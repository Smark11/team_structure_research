# Source map: merges and URL choices for `sources.json`

Built 2026-08-29 from the `## Sources` sections of C1–C5. 230 local keys → 216 unique sources (14 merges, all pairs). Every local key appears exactly once. Array order is by report and key of first appearance (C1, then remaining C2, C3, C4, C5); numbering is left to the site script.

## Merges (same work cited in two reports)

| Keys merged | Work | URL chosen | Why |
|---|---|---|---|
| C1-10 + C3-48 | Kniberg & Ivarsson, "Scaling Agile @ Spotify" (2012) | `blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf` (C1) | The whitepaper PDF is the work itself; C3 pointed at the Crisp blog announcement post. |
| C1-13 + C3-49 | Lee, "Spotify's Failed #SquadGoals" (2020) | identical | C1's qualifier ("second-hand for the Sundén quote") kept in `note`. |
| C1-30 + C3-50 | Bryar & Carr, *Working Backwards* (2021) | Amazon product page (C1) | Neither report had the St. Martin's Press page; a retailer page beats Goodreads (C3). Note records "retail page verified only". |
| C2-15 + C5-33 | Wikipedia, "Disney+ Hotstar" | `…/Disney%2B_Hotstar` (C5 form) | Same page; C2 used the raw `+`. Percent-encoded form chosen as the safer link. Tag `documented`, note "Tertiary". |
| C2-22 + C5-31 | WBD Careers, "India Innovation Hub" | identical | C2's "recruiting copy" qualifier kept in `note`. |
| C2-24 + C5-32 | Telangana Today, WBD Hyderabad Capability Centre inaugurated (Sep 2023) | identical | — |
| C3-13 + C4-1 | Skelton & Pais, *Team Topologies* | IT Revolution 2nd-ed. page (both reports listed it) | Publisher page; year set to 2019 (first ed.), note records 2nd ed. 2025 and the 1st-ed. `teamtopologies.com/book` link. |
| C3-22 + C4-2 | Larson, *An Elegant Puzzle* (2019) | identical (Stripe Press) | — |
| C3-28 + C4-9 | Forsgren, Humble & Kim, *Accelerate* (2018) | `itrevolution.com/product/accelerate/` (C3) | Publisher page over Simon & Schuster distributor page (C4). |
| C3-32 + C4-7 | Dehghani, *Data Mesh* (2022) | O'Reilly library page (C4) | Publisher page over Thoughtworks book page (C3). |
| C3-35 + C4-17 | Stancil, "Disband the analytics team" (2024) | post URL (C3) | C4 cited the *benn.substack* newsletter as a whole with this post as its example; merged per brief, note records the newsletter-level citation. |
| C3-41 + C4-16 | Sanderson, "The Rise of Data Contracts" | post URL (C3) | C4 cited the *Data Products* newsletter as a whole plus this post and "The Shift Left Manifesto – v2"; merged per brief, note records both. |
| C3-43 + C5-18 | Herbsleb & Mockus, IEEE TSE 29(6) (2003) | `herbsleb.org/…/Herbsleb-Empirical-2003.pdf` (C5) | C5 fetched and text-verified the PDF; C3's ACM DOI page and 2025 retrospective recorded in `note`. |
| C3-45 + C5-20 | Carmel & Agarwal, IEEE Software 18(2) (2001) | `ieeexplore.ieee.org/document/914734/` (C3) | C3 accessed the publisher page; C5 verified metadata via Semantic Scholar only (DOI kept in `note`). |

## Pairs checked and deliberately NOT merged

- **Cummings, Espinosa & Pickering (2009)** — appears only as C5-19.
- **Mintzberg**: C3-4 ("Structure in 5's", *Management Science* 1980 article) vs C4-29 (*Structure in Fives*, 1983 book) — different works.
- **Galbraith**: C3-3 (*Organizational Dynamics* 2010 article) vs C4-5 (*Designing Organizations*, 3rd ed. 2014 book) — different works.
- **Larson**: C3-23…26 (four specific lethain.com posts) vs C4-11 (the blog as a whole, no specific post named in the source entry) — kept separate; a whole-blog entry cannot be merged into four distinct posts.
- **Netflix TechBlog**: C1-1…4, C3-53 (specific posts) vs C4-18 (blog as a whole; its example post "Data Projects…" is not cited elsewhere) — separate.
- **Spotify Engineering**: C1-14…18 vs C4-21 (blog as a whole) — separate.
- **Analytics Engineering Roundup**: C3-39 (Handy post) vs C4-19 (publication as a whole) — separate.
- **Locally Optimistic**: C3-36, C3-37 (posts) vs C4-23 (site as a whole) — separate.
- **Team Topologies site**: C3-14, C3-15 (key-concepts pages) vs C4-12 (news/blog) — different pages.
- **Kohavi**: C1-32 (HBR 2017, with Thomke) vs C4-10 (book, 2020) vs C4-24 (companion site) — different works.
- **Telangana Today**: C2-23 (May 2023 announcement) vs C2-24/C5-32 (Sep 2023 inauguration) — different articles.
- **Business of GCC**: C1-28 (Google profile) vs C2-25 (WBD profile) — different pages.
- **Outlook Business**: C1-37 (Prime Video India) vs C5-27 (JPMorgan) — different articles.
- **Nickols `graicunas.htm`** is the URL for both C3-17 (Graicunas 1933) and C3-18 (Urwick 1956) — different works; both kept.

## Tag handling

- Tags come from the report(s); qualifiers were moved to `note` (e.g. "Vendor", "Tertiary", "Recruiting copy", "Verified via search index only, page not fetched").
- C3's source list carries no per-source tags; its sources are all verified primary/peer-reviewed, so they are `documented`, except **C3-53** (Netflix analytics-engineering post: HTTP 403, body marked `[inferred — post body not fetched]`) → `inferred`, and **C3-18** (Urwick, verified via secondary sources) → `documented` with a note.
- C4 assigns no evidence tags; all its entries are fetched books, blogs and podcasts → `documented`.
- No merged pair had conflicting tags.


## Added in review
- C2-51 — Wikipedia, *Warner Bros. Discovery* (tertiary): added in cycle 2 (fact-check B2-8) to source the Fig 2.1 timeline rows for April and August 2022.
