---
name: pharma-daily
description: Produce one day's pharma/biotech finance brief end-to-end — run the tools/pharma-daily pipeline, draft the post from the data pack under the editorial rules in tools/pharma-daily/EDITORIAL.md, fact-check against the pack, pass site QC, and stop at the human review gate before any video or git step. Use when writing the daily pharma brief on the jaimeyan.com Astro site.
---

# Pharma Daily brief — agent workflow

Produce one day's brief, from pipeline run to human review gate. Site root is
the Astro repo (this file lives at `.agents/skills/pharma-daily/SKILL.md`).
The binding style/method bible is `tools/pharma-daily/EDITORIAL.md` — read it
first and follow it exactly.

## Red lines (never cross, no exceptions)

- **No invented facts.** Every number, date, name, and claim in the post comes
  from the data pack JSON, or from an evidence card written in step 4 (whose
  source you actually retrieved this session). Outside knowledge may
  shape the *framing* of the One Take but never introduces a factual claim
  that is not in one of those two places.
- **Undisclosed stays undisclosed.** Null pack fields render as "undisclosed".
  Never estimate, infer, or smooth over a null. A Datasource query that
  returns nothing means the fact stays out of the post — do not guess.
- **No full-text copying.** Summarize and link first-hand sources; never
  reproduce filings, press releases, or wire text beyond a short attributed
  fragment.
- **No investment advice.** No buy/sell/hold language, no price targets, no
  trading signals.
- **No git mutations** (commit, push, rebase, reset, branch changes) without
  explicit owner approval.
- Do not edit `tools/pharma-daily/` Python code, `scripts/new-post.mjs`, or
  the QC/video scripts as part of this workflow — report gaps instead.

## Steps

1. **Run the pipeline** (from site root):

   ```bash
   cd tools/pharma-daily && uv run python daily.py --days 1 --filing-text
   ```

   Load the data pack: `tools/pharma-daily/out/pack/<date>.json`. The pack is
   the factual backbone; step 4's evidence cards are the only other factual
   input allowed.

2. **Check provenance.** If `provenance.sources_failed` is non-empty, the post
   must name the failed source(s) and state what coverage is missing — in the
   TL;DR caveat and again in the Sources footer. If the pack itself is missing
   or empty, stop and report; do not draft from memory.

3. **Grill the pack (question generation).** Follow
   `tools/pharma-daily/prompts/grill.md`: read the pack as a skeptical BD
   editor and write 5–10 questions, each triggered by a specific pack row, to
   `tools/pharma-daily/out/questions/<date>.json`. Questions only — no prose,
   no new facts. If the pack is thin, fewer questions; never pad.

4. **Retrieve evidence (budget-disciplined).** Follow
   `tools/pharma-daily/prompts/retrieve.md`: answer the grill questions into
   evidence cards at `tools/pharma-daily/out/evidence/<date>.json`. Channels
   in priority order: our own deals DB (`data/pharma.db`, free) → web
   first-hand sources → Kimi Datasource (local sessions only, at most 5
   queries, and only for facts that will appear in the final post — Chinese
   pharma background via Wind/Caixin/Xinhua remains a differentiator).
   Every card carries publisher + source_url + as_of. An unanswered question
   stays unanswered; the fact stays out of the post.
   Operational notes (learned 2026-09-04): realtime prices only during
   active trading hours — default to the historical-price API for the last
   ~5 sessions instead. Ticker suffixes differ by API: realtime uses `.US`,
   historical/financials use `.O` (Nasdaq) / `.N` (NYSE) — verify the
   exchange before querying, never guess.

5. **Draft the post.** Start from `templates/daily-template.md` (copy it
   manually — `scripts/new-post.mjs` has no "daily" kind; do not use it and do
   not edit it). Slug: `pharma-daily-<date>`; title:
   `Pharma Daily — <Month D, YYYY>`; kind stays `note`. Fill every section in
   the fixed order from EDITORIAL.md: hook → TL;DR → Deals (table + comp
   paragraph with upfront-vs-milestone honesty and percentile context;
   flag thin samples, n < 30) → Approvals → Readout Calendar → Market
   Reaction → One Take → Key takeaways → FAQ → Sources + provenance footer.
   Keep sections short and keep the narrative-essential content in the first
   three columns of each table — the video extractor narrates only those.
   Every figure gets a takeaway caption (a conclusion).

   **Insight-first drafting (EDITORIAL.md §3, binding):** read
   `pack.insights[]` before writing anything. The TL;DR's "most important
   pattern" and the One Take must each lean on at least one computed insight,
   citing its numbers; Key takeaways must contain at least one computed
   relationship (ratio, percentile, delta vs baseline) rather than raw counts
   alone. If `insights[]` is empty, say so in the review-gate summary and
   write the One Take from comp/market relationships you compute yourself —
   never restate the deal table as prose. A draft that lists numbers without
   a "so what" fails review.

   **Evidence-aware drafting:** an answered grill question whose evidence
   card strengthens a section belongs in that section with its publisher
   cited; evidence cards extend — never replace — the pack as the factual
   base. `confidence: medium` cards are hedged in prose.

6. **Self fact-check pass (mandatory, separate from drafting).** Re-read the
   draft. For every number and factual claim: locate the exact pack field or
   evidence card it came from, and confirm the value matches (units, dates,
   spellings, money formatting). List any claim without provenance, then
   delete or fix each one. Verify figure captions match `figures[].takeaway`
   in the pack. (In CI a second, cross-vendor model then runs the
   adversarial critique from `tools/pharma-daily/prompts/critique.md`;
   locally, if no second model session is available, say so at the review
   gate.)

7. **Copy figures and write the post.** Copy the figures listed in
   `figures[].path` (`tools/pharma-daily/out/figures/<date>/*.png`) to
   `public/figures/pharma-daily-<date>-<name>.png` and reference them as
   `/figures/pharma-daily-<date>-<name>.png` (verify names against the
   existing post `content/posts/pharma-daily-2026-09-04.md`). Write the
   finished post to `content/posts/pharma-daily-<date>.md`.

8. **Generate the audio version.** Run:

   ```bash
   cd tools/pharma-daily && uv run python make_audio.py pharma-daily-<date>
   ```

   This synthesizes `public/audio/pharma-daily-<date>.mp3` (edge-tts, prose
   only — tables/figures are skipped by design) and stamps
   `audioPath: /audio/pharma-daily-<date>.mp3` into the frontmatter, which
   makes the article page render the "Listen to this article" player under
   the TL;DR (above the YouTube embed). Re-runs are cached by narration
   hash; use `--force` after editing the post text.

9. **QC and build** (from site root):

   ```bash
   npm run qc:blog
   npm run build
   ```

   Fix every error (banned phrases, missing frontmatter fields, h1 in body,
   missing inward `/blog/` link) and re-run until clean. Warnings worth
   fixing: description 120–170 chars, title ≤ 70 chars.

10. **STOP — human review gate.** Present to the owner: the TL;DR, the One
   Take, the fact-check list from step 6 (pack fields + evidence cards used),
   the grill questions that went unanswered, whether the cross-vendor
   critique ran, and every caveat (thin samples, failed sources,
   undisclosed-heavy deal rows). Do not proceed to video, commit, or push
   without explicit approval.

11. **After approval only** — hand off to the video pipeline for script review:

   ```bash
   npm run video:build -- pharma-daily-<date> --script-only
   ```

   Present `temp/videos/pharma-daily-<date>/script.md` for the owner's script
   gate. Rendering, upload, and any git step remain owner-triggered actions,
   not agent actions.
