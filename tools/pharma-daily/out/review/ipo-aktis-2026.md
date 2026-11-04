# Critique — ipo-aktis-2026.md

Scope: no pack for this article, so per instruction the linked sources are the
evidence base. I fetched every first-hand source (pricing release, S-1/A Jan 5,
S-1/A Jan 7, 424B4, Q2 10-Q, Q2 8-K + exhibit 99.1 press release, Lilly 13D),
both ClinicalTrials.gov records (via API v2), and BioPharma Dive. Price/tape
figures were additionally cross-checked against the Yahoo Finance daily series
for AKTS — the feed the draft's provenance footer cites. Internal `/blog/`
targets were checked for `draft: true`. No banned phrases, no red-line
identifiers, no structural failures (`blog-qc.mjs`: 0 errors, 0 warnings).

Violations found (reported only, draft not modified):

## 1. "$10M of equity" — no provenance in any linked source

Body, Lilly-relationship paragraph: "a May 2024 collaboration ($60M upfront
plus $10M of equity, up to $1.2B of milestones and tiered royalties)".

- The 424B4 (and both S-1/A amendments) describe the collaboration as "$60.0
  million upfront cash payment in addition to an **equity investment**" — no
  dollar amount for the equity.
- The Lilly Schedule 13D shows Lilly's pre-IPO preferred was **$10.0M**
  (2,500,000 Series A-1 shares) **plus $2.0M** (500,000 Series B shares) =
  $12.0M total — not "$10M of equity."
- The "$10M" figure is not stated anywhere in the linked evidence base.
  Violation: unsupported number.

## 2. "first-in-human imaging and dosimetry data disclosed August 13" — wrong date (×3)

Occurs three times (asset section; "What would change the story"; FAQ).

The Aug 13, 2026 8-K exhibit 99.1 press release itself says the AKY-2519
first-in-human clinical imaging and dosimetry data was "Presented … at the
American Society of Clinical Oncology (ASCO) Annual Meeting in **May 2026**."
August 13 is the Q2-results press-release date, not the first disclosure of
that data. Violation: misattributed disclosure date.

## 3. "MPM entities bought $20.0M and Vida Ventures 812,455 shares, per their own 13Ds" — no linked source

Anchor paragraph. No MPM or Vida Ventures 13D (or any other document stating
these amounts) appears in the article's Sources list or among the linked
sources. The $20.0M and 812,455-share figures cannot be traced to the evidence
base. Violation: no provenance.

## 4. "1.1x the class median" — arithmetic is ~1.08x

Deal paragraph: "At $318M the deal was 1.1x the class median."

The linked parent post (`biotech-ipo-class-2025-2026`) states the class median
raise at $295M (exact $294.8M). $318M / $295M = **1.08x** (1.078), not 1.1x.
Violation: minor numeric overstatement.

## Non-blocking interpretive note

"the earliest-stage profile among the class's winners" — the same parent post
notes Scribe priced at Phase 1 and trades +90% (also a Phase 1 winner), so
"earliest-stage … among the winners" is not strictly unique. Soft/interpretive,
not a hard number violation; flagged for the writer's judgment only.

VERDICT: needs-human
