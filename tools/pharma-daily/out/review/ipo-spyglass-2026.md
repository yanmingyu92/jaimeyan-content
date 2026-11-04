# Critique report — ipo-spyglass-2026.md

Draft: `content/posts/ipo-spyglass-2026.md`
Evidence base: linked sources only (no pack). Every number/date/name was checked against the fetched links; the two "stock_finance_data / Yahoo" closes were checked against the Yahoo Finance daily series for SGP.

## Violations (hard — must be corrected)

### 1. License fee "$100,000" is wrong — the one-time fee is $60,000

Locations: "Origin" paragraph ("…an exclusive worldwide license to the dispenser patents that cost a one-time $100,000 fee") and Key takeaway 5 ("…cost a one-time $100,000 fee — the cheapest origin story in the class").

Evidence — SpyGlass S-1 (linked): "In consideration for the rights granted by the License Agreement, we paid a **one-time, non-refundable $60,000 license fee** in conjunction with the second amendment to the License Agreement on March 22, 2023." The S-1 also states the company issued CU shares, pays an annual license fee of up to $50,000, and owes milestone payments of up to $1.05 million per product. No "$100,000 fee" appears anywhere in the S-1 (the only "$100,000" hits are "100,000 shares" in an option grant and "$100,000,000 gross proceeds").

Required fix: replace "$100,000" with "$60,000" in both places; the "cheapest origin story" framing is also weakened since the fee is $60k plus shares/annual fees/milestones. (Also, "dispenser patents" is not the source's term — the S-1 uses "Licensed Patents" covering drug elution/product design/methods/packaging.)

### 2. Net proceeds "≈ $156.5M" is wrong — the 10-Q says $157.7M

Locations: Table 1 caption ("…full greenshoe; net ≈ $156.5M") and Sources (Q2 10-Q entry: "…net ≈$156.5M…").

Evidence — Q2 2026 10-Q (linked): "net cash provided by financing activities for the six months ended June 30, 2026 was $157.8 million and primarily related to **$157.7 million in net cash proceeds from our IPO** and proceeds of $0.1 million from the exercise of stock options." The S-1/A's estimate (also linked) was "approximately **$156.1 million**" if the greenshoe was exercised in full. The draft's "$156.5M" matches neither figure.

Required fix: change "net ≈ $156.5M" to the 10-Q's "$157.7M net cash proceeds" (or clearly attribute $156.1M as the S-1/A estimate).

### 3. "The closing 8-K's only other content was a director appointment" is false

Location: "The deal" section ("The closing 8-K's only other content was a director appointment: Habib Dable, the former Acceleron CEO.").

Evidence — the linked Feb 9 closing 8-K contains three material items, not just the director appointment:
- Item 5.02 — Habib Dable appointment (Feb 5, 2026; the draft's "former Acceleron CEO" is accurate).
- Item 5.03 — filing of the amended/restated certificate of incorporation and adoption of the amended/restated bylaws.
- Item 7.01 — Regulation FD press release announcing the IPO closing of 10,781,250 shares (the full-greenshoe disclosure itself lives here).

Required fix: remove "only other content" — the 8-K also discloses the charter/bylaw amendments and the closing press release; the greenshoe close is Item 7.01, not a standalone fact.

## Minor notes (precision / caveats — flag for writer, not numeric errors)

4. **"the smallest deal in this series"** (Key takeaway 1, and the "class's small-deal proof" / "small-deal" framing). True only of the 10 per-company companion posts. In the parent post's 21-deal class table, three deals are smaller than SpyGlass's $172.5M: Vogenx ($81.3M), Scribe ($129M), and BlossomHill ($150M). Recommend "smallest of the per-company deep-dives" or similar to avoid contradicting the parent table.

5. **"two decades approved" / "a 20-year-approved API"** (body + Key takeaway 2). Bimatoprost was FDA-approved topically in 2001; 2001 → 2026 is 25 years. "Two decades" understates by five years; "approved since 2001" (used elsewhere) is correct.

6. **"initiated in July 2025"** ("The asset" section). Traces to the S-1/A ("we initiated two registrational Phase 3 clinical trials in July 2025"), but ClinicalTrials.gov shows Rhine start date 2025-10-15 (ACTUAL) and Rhone 2025-10-28 (ESTIMATED), and the March 8-K says first patients were randomized in January 2026. Not a hard error (faithful to the S-1/A) but worth a one-line caveat that the registry start dates are October 2025.

7. **"33.4M-share count"** (used for float mechanics). Spans two distinct figures: 33,317,414 shares outstanding immediately after the greenshoe (S-1/A / 424B4) versus 33,446,315 issued and outstanding at June 30, 2026 (10-Q). Both round to 33.4M, but the single number elides which one is meant.

## Spot-checked clean (no violation)

- Pricing: 9,375,000 shares at $16.00 = $150.0M gross; greenshoe 1,406,250 → 10,781,250 total = $172.5M. Range $15–17 ($141–159M). Syndicate Jefferies/Leerink/Citigroup/Stifel. All match the pricing release and S-1/A.
- All five closes via Yahoo Finance daily series for SGP: debut $26.40 (+65.0%), Feb 19 $29.68 (max close), Jun 16 $17.56 (min post-debut close, +9.75% vs offer = "within 10%"), Aug 28 $26.42 (+65.1%), Sep 4 $28.94 (+80.9%). Percentages recomputed against $16.00 all correct.
- Clinical: FIH 37% at 36 mo / 95% off drops; Phase 1/2 37%/36% at 3 mo / 97% off drops; 12-month 34% (78-mcg) & 42% (39-mcg) vs 35% timolol, 97% off drops, 100% BCDVA 20/32. Matches S-1/A and the March 9 8-K.
- Rhine = NCT07218783, Rhone = NCT07218796, each 400 patients vs timolol, primary completions 2029-03-31 / 2029-05-31. Tigris = NCT06120842 (Phase 1/2 acronym "Tigris"). BIM-DRS = NCT07641296, Phase 1, NOT_YET_RECRUITING, pseudophakic. All match ClinicalTrials.gov.
- Cash + short-term investments $234.2M at June 30, 2026; runway through 2028; BIM-DRS FIH H2 2026. Match the Q2 results release and 10-Q.
- Private capital "roughly $167M across C-1, C-2, and D (2023–2025)": computed from the S-1 round disclosures — C-1 28,285,209 × $1.41452 = $40.01M; C-2 28,283,795 × $1.76815 = $50.01M; D 33,247,796 × $2.32574 = $77.33M; sum $167.35M ≈ $167M. Not a violation (the S-1 summary's "~$200M since inception" is the broader total including earlier rounds).
- Ownership NEA 28.6% / RA 19.2% / Vensana 14.0% appear in the S-1 principal-stockholders table.
- Founded 2019 by Malik Kahook & Glenn Sussman, developed at the University of Colorado's Sue Anschutz-Rodgers Eye Center. Habib Dable = former Acceleron President & CEO (Dec 2016–Nov 2021). Correct.
- Inward links `/blog/biotech-ipo-class-2025-2026.html`, `/blog/ipo-avalyn-2026.html`, `/blog/ipo-veradermics-2026.html` all point to published posts (no `draft: true`).

VERDICT: needs-human
