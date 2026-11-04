# Review — ipo-generate-2026.md

No data pack or evidence cards exist for this draft. Evidence base = the linked
sources plus the two inward links (`biotech-ipo-class-2025-2026.md`,
`ipo-kailera-2026.md`). Price history checked against Yahoo Finance daily
series for GENB; registry figures checked against ClinicalTrials.gov API v2.
Per instruction, violations are reported only — nothing was rewritten.

Every core deal, financial, and price figure checked out (pricing $16.00 /
25,000,000 sh / $400M; range $15–17 = $375–425M; 15% greenshoe 3,750,000 sh
unexercised; net proceeds $369.3M after $30.7M; ticker GENB vs the class
table's GBIO; $457.4M cash; $67.3M net loss; $64.3M R&D; H1 2028 runway; Amgen
$50M / up to $370M-per-program; Novartis $50M / $25.1M FY2025; SOLAIRIA 786 × 2
with Dec-2028 / Jan-2029 primary completions; first dose Jan 26, 2026; all tape
closes from $12.65 debut through $16.39 Sep 4). QC script: 0 errors, 0 warnings.

## Violations

1. **"Kailera and Parabilis upsized and priced above range"** (deal section).
   Wrong for Kailera. The linked `/blog/ipo-kailera-2026.html` states Kailera
   priced "$16.00, the top of its $14–16 range" — at the top, not above.
   Parabilis "priced above range" is not supported by the class post, which
   records only "upsized twice; $771M as-exercised." Fix: change to "upsized
   and priced at the top of range" (or drop the above-range claim for Parabilis
   until a source supports it).

2. **"first closed back above the offer in late June ($16.47 on June 26)"**
   (tape section). The $16.47 value is correct, but "first" is not. Yahoo
   GENB closes show the first close above $16.00 was **June 24 at $16.23**,
   followed by $16.42 (Jun 25) and $16.47 (Jun 26). Fix: "first closed back
   above the offer on June 24 ($16.23)" or "closed above the offer in late
   June ($16.47 on June 26)."

3. **"raised over $934M before the IPO ($805.3M in preferred stock plus $110M
   in collaboration payments)"** (asset section). The two figures are correct
   individually, but the parenthetical does not reconcile to $934M
   ($805.3M + $110M = $915.3M). The 424B4 lists four components: $805.3M
   preferred stock, $12.0M term loan, $7.5M convertible notes, $110.0M
   collaboration payments. Fix: include the omitted $12.0M + $7.5M, or drop
   the incomplete breakdown.

4. **"Amgen and Novartis paid $100M combined upfront"** (FAQ). Understates.
   The 424B4 shows Amgen received an additional $5.0M upfront payment
   (Dec 2023 amendment) on top of the $50.0M initial upfront; Novartis
   received $50.0M. Combined upfront = $105M. Fix: "$105M combined upfront"
   or qualify as "initial $50M up-fronts."

5. **"the May 13G filings are Flagship entities and the CEO — insider
   ownership reports, not new money"** (tape section). No provenance. No linked
   source supports the identity of the May 13G filers, and the issuer's SEC
   filing index (the only candidate source) does not contain 13G filings —
   those are filed under the holders' own CIKs, not the issuer's. This is an
   unsourced factual claim and should be deleted or backed by the actual 13G
   documents.

## Notes (low severity, for human)

- **"both initiated in December 2025."** The prospectus groups SOLAIRIA-1 and
  SOLAIRIA-2 as "initiated in December 2025," but ClinicalTrials.gov lists
  SOLAIRIA-2's actual start date as **2026-01-20** (SOLAIRIA-1 = 2025-12-03).
  "Initiated" vs registry "start date" can legitimately differ; flag for a
  human to confirm the intended meaning.
- **"1.4x the class median."** Class median is $294.8M computed ($295M stated)
  in the parent post; 400/294.8 ≈ 1.36x, which rounds to 1.4 only at one
  decimal. Acceptable rounding, but worth a precise "1.36x" if exactness is
  preferred.

VERDICT: needs-human
