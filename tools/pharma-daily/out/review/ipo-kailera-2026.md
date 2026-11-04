# Critique — Kailera IPO deep-dive (2026-09-05)

Draft: `content/posts/ipo-kailera-2026.md`
Mode: report-only (no pack; linked sources treated as the evidence base). Per
instruction, violations are reported, not rewritten.

## Violations found

1. **First-day market cap uses the wrong share count (substantive).**
   Line 46 computes a ~$3.4B market cap "on the 129.5M shares outstanding after
   the offering" for the April 17 session. The 424B4 states 123,677,939 shares
   outstanding immediately after the offering, or 129,537,314 if the
   underwriters' option is exercised in full. The greenshoe exercise was only
   announced in the April 20 closing release, so on April 17 the outstanding
   count was ~123.7M, not ~129.5M. At $26.00, that is ~$3.2B, not ~$3.4B.
   Either correct the share base to 123.7M, or date the 129.5M figure to after
   the April 20 greenshoe close.

2. **Schedule 13D source labels are swapped (link accuracy).**
   The Sources section attributes `8,398,438 shares ($134.4M)` to accession
   `000119312526174330` and `1,562,500 shares ($25.0M)` to
   `000119312526174293`. The filings contain the reverse:
   - `...174330/primary_doc.xml` → 1,562,500 shares at $16.00 for $25,000,000.
   - `...174293/primary_doc.xml` → 8,398,438 shares at $16.00 for $134,375,008.
   The body totals ($159.4M) are correct; the link-text mapping is not.

3. **Private-raise figure conflicts with a cited secondary source.**
   The draft states Kailera "raised $900M privately since its May 2024
   inception," sourced to the S-1/A (which does say "$900 million"). The cited
   BioPharma Dive article says the company "raised more than $1 billion in
   private funding." The S-1/A is the primary and more authoritative source, so
   $900M is defensible, but the discrepancy with a linked source should be
   acknowledged rather than left silent.

## Notes / near-misses (not counted as violations)

- **"Weakest hold among the class's large single-asset deals"** is an inference,
  not a quote from any single source. It is supported by the parent piece
  ("the marginal name and the canary") and the BioBucks "marginal name at +1%"
  framing, but it is the draft's own characterization.
- **September 4 mark (+1.4%, $16.23, volume 98,468)** is consistent with the
  draft's stated stock_finance_data feed, but could not be independently
  cross-checked from the linked public sources (BioBucks/parent piece are
  marked to Aug 28 at +1.3%). Not a violation, but the tape figures rest on the
  feed rather than a web source.

## Verified clean

- Pricing/close: 39,062,500 shares at $16.00 = $625.0M; full greenshoe
  44,921,875 shares = $718.8M (GlobeNewswire pricing + Kailera closing release).
- S-1/A: range $14–16; 33,333,334 shares (≈$533M at top); $225M non-binding
  anchor indication; $100.0M upfront + $10.0M tech transfer; $200.0M clinical/
  regulatory + $5.725B commercial milestones; royalties mid-single-digit to
  low-tens; $96.4M fair value of Hengrui shares (19.9% at issuance); $900M
  raised since inception; KaiNETIC enrollments (≈2,340 / 1,156 / 1,200, with
  open-label semaglutide 2.4 mg in the 1,200-arm trial).
- ClinicalTrials.gov: NCT07284875 (2,340, recruiting), NCT07284901 (1,156,
  recruiting), NCT07284979 (1,200, recruiting), NCT07709910 (382, not yet
  recruiting), NCT07458269 (actual 264, active-not-recruiting, primary
  completion May 2027).
- 10-Q: Q2 net loss $111.3M; R&D $101.1M; injectable ribupatide R&D $70.6M
  ($70,569K); cash + marketable securities $1,171.8M; runway "into mid-2028".
- Net proceeds ~$662.1M with full greenshoe (424B4); 2.1x $295M median
  ($625/295 = 2.12); +62.5% and +1.4% arithmetic checks out.
- Internal `/blog/` links all resolve to published posts (no `draft: true`):
  `biotech-ipo-class-2025-2026`, `ipo-parabilis-2026`, `pharma-daily-2026-09-04`.

VERDICT: needs-human
