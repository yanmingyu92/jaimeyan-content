# Critique — ipo-braveheart-2026.md

Draft: `content/posts/ipo-braveheart-2026.md`
Method: no pack; linked sources treated as the evidence base. Every number checked
against the fetched sources (424B4, closing 8-K, Hengrui release, the two Phase 2
PRs, Renaissance Capital, ClinicalTrials.gov API, and the two linked Pharma Daily
posts). Violations only — no rewrite performed, per instruction.

## Violations

### 1. LIONHEART-HCM and the metoprolol head-to-head are the same trial (significant)

Draft (line 23) lists three things as if they were separate:

> LIONHEART-HCM, a global Phase 3 in obstructive HCM starting 2H 2026 with an
> interim topline guided for 2H 2027 … A head-to-head Phase 3 against metoprolol is
> registered but not yet recruiting ([NCT07755904], 210 patients, primary
> completion October 2028).

ClinicalTrials.gov API for NCT07755904 shows `acronym: "LIONHEART-HCM"` and the
official title `"BHB-1893 Versus Metoprolol for Symptomatic Obstructive
Hypertrophic Cardiomyopathy"`. The metoprolol comparator is the design of
LIONHEART-HCM itself, not a third trial. The draft double-counts one trial as two
and thereby implies three global Phase 3 programs (LIONHEART, NOBLEHEART, and a
separate metoprolol study) when there are two.

### 2. "86.9M shares" / "~$2.3B market value" has no source and conflicts with the 424B4

Draft (line 45): "about $2.3B of market value on 86.9M shares."

The 424B4 capitalization table gives shares outstanding after the offering as
**73,152,838** (or **76,340,338** with the full greenshoe); fully diluted (adding
the 60M April Series A shares at the 1-for-4.38 split plus options) is ~90M, not
86.9M. No linked source states 86.9M. The market-value claim is therefore
unverifiable against the provided links.

### 3. "$431.8M pro forma cash … after the April Series A tranche" is a misdescription

Draft (line 41): "Pro forma cash after the April Series A tranche and the IPO:
$431.8M."

The 424B4's "pro forma as adjusted" cash is **$431,751K** ($431.8M) **as of
March 31, 2026**, equal to March 31 cash ($80,576K) plus IPO net proceeds
($351.2M). It does **not** include the $60M Series A sale of April 24, 2026
(listed in the filing as a post-March-31 excluded item). The figure is correct;
the "after the April Series A tranche" framing is wrong.

### 4. "$6.0M already incurred by March 31, 2026" understates the incurred tech-transfer milestones

Draft (line 39): "up to $23M of tech-transfer and development milestones ($6.0M
already incurred by March 31, 2026)."

The 424B4 records a **$3.0M** technology-transfer milestone completed December 2025
(paid by March 31, 2026) **plus** a **$6.0M** manufacturing technology-transfer
milestone completed March 2026 — **$9.0M total** incurred by March 31, 2026, not
$6.0M.

### 5. "clinical supply … at Hengrui's cost" is not in the source

Draft (line 39) says "clinical supply and CMC transfer at Hengrui's cost"; the FAQ
(line 76) says Hengrui "supplies clinical material at its own cost."

The 424B4 states only that Hengrui provides "manufacturing process and CMC-related
technology … at its sole cost and expense." It says Hengrui "currently supplies all
drug substance and drug product for our clinical development," but does **not**
state clinical supply is at Hengrui's cost. The clinical-supply-at-cost claim is
unsupported.

### 6. Kailera upfront "$206M" is internally inconsistent with line 39 and mixes components

Line 39: "Kailera's Hengrui deal: $100M cash plus ~$96.4M of equity upfront"
(= **$196.4M**).

Lines 51 and 62 use **"$206M"** as Kailera's upfront cost. $206M only arises by
adding the $10M technology-transfer fee ($100M + $96.4M + $10M = $206.4M), which
line 39 does not include. Meanwhile Braveheart's "$58M of cash plus fair-value
equity" ($32.5M + $25.7M) excludes Braveheart's own tech-transfer milestones
($9.0M incurred). The "$206M vs $58M" comparison therefore adds a component on the
Kailera side it omits on the Braveheart side, and conflicts with line 39's
"$196.4M."

## Minor / caveats (not hard violations, but worth noting)

- **"40 mg BID cohort" (line 21)** is a loose label. The 424B4 and Phase 2 PR
  describe Cohort/Group 2 as "40 mg twice daily (potentially titrated up to 80 mg)"
  = the "40–60–80 mg BID cohort," not a fixed 40 mg BID cohort.
- **OLE transient LVEF<50% omitted.** The 424B4 discloses two transient LVEF <50%
  events in the open-label extension (resolved after dose reduction). The draft's
  core-period claim ("no LVEF below 50% in the 12-week core period") is accurate,
  but the One Take's "safety question answered cleanly" glosses over the OLE events,
  which are not mentioned.
- **Tape prices unverifiable from provided links.** Debut open/close ($30.20 /
  $29.80) and later closes ($30.00, $25.01, $27.44, $26.74) are attributed to "the
  Yahoo Finance daily series" but no fetchable URL is given in Sources, so they
  (and the +65.6% / +48.6% derived from them) cannot be independently checked here.
  This is disclosed in the draft's own provenance note, but remains a provenance gap.
- **One Take "next 20 points" (line 62)** is borderline vs. the no-price-target rule;
  it is framed as a catalyst read rather than a target, so not flagged as a
  violation, but a reviewer should confirm it reads as judgment, not a target.

## Checks that passed

- Deal sizing: 21,250,000 shares at $18.00 = $382.5M; full greenshoe 3,187,500
  shares → 24,437,500 × $18.00 = $439.9M. Matches 424B4 and Renaissance Capital.
- License terms: $32.5M cash + 32.5M non-voting Series A shares (fair value $25.7M);
  up to $23M tech-transfer/dev milestones; up to $1.0B commercial milestones;
  tiered 5–10% royalties; CMC transfer at Hengrui's cost — all confirmed in 424B4.
- Hengrui's "$65M cash-plus-equity" framing confirmed by Hengrui release.
- NCT07021976: 228 patients (actual), ACTIVE_NOT_RECRUITING, primary completion
  2026-09 (estimated) — all match. NCT07755904: 210 (estimated), NOT_YET_RECRUITING,
  primary completion 2028-10 (estimated) — match (identity error is #1 above).
- Stockholders: Forbion 27.8%, OrbiMed 15.6%, a16z 13.9%, Hengrui 11.3% (non-voting),
  Frazier 5.2% — match Principal Stockholders table (an additional 5.2% holder,
  ES Braveheart Aggregator, is omitted but the listed figures are correct).
- Vineeta Agarwala joins board at closing; HI-Bio acquired by Biogen in 2024 for up
  to $1.8B — both confirmed in 424B4.
- FY2025 net loss $66.1M (IPR&D $62.2M); Q1 2026 net loss $14.3M — confirmed.
- Private capital ~$185M; incorporated May 13, 2024, operations began 2025 — confirmed.
- "$1.6B fully diluted at pricing" — confirmed by Renaissance Capital.
- "1.3x the class median" — consistent with the parent post's $295M median.
- Kailera "+1.4%" (Sep 4) — consistent with the Kailera post (parent class table's
  "+1.3%" is the Aug 28 mark, a different date; not a conflict).
- Inward links target published posts (no `draft: true`).

VERDICT: needs-human
