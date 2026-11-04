# Critique — content/posts/ipo-avalyn-2026.md

Method note: no data pack or evidence cards exist for this article, so the linked
sources were treated as the evidence base. Every number, date, and claim below was
checked against the linked SEC filings, press releases, ClinicalTrials.gov records,
and the Yahoo Finance daily series by fetching them.

## Result

All quantitative claims in the draft verify clean against the linked sources. No
wrong numbers, dates, tickers, share counts, or percentages were found. Four minor
non-numeric flags are listed below (none is a factual error in a dollar/percent/share
figure).

## Verified clean (sampled, all matched)

- Deal: 16,666,667 shares at $18.00 = $300M gross (pricing release, 424B4); full shoe
  19,166,667 shares = $345M (closing release). Priced 2026-04-29; S-1 04-08, S-1/A
  04-23 (11.8M shares, $16–18), 424B4 04-30, closing 05-01.
- Syndicate: Morgan Stanley, Jefferies, Evercore ISI, Guggenheim (pricing release).
- Net proceeds ~$316.6M (Q2 release); cash $413.5M at 06-30 and runway into 2029
  (Q2 release).
- MIST: NCT06329401, PPF, Phase 2b, 375 planned / 398 enrolled, FVC primary at 52
  weeks, topline H2 2027 (ClinicalTrials.gov + 8-K 06-17 + Q2 release).
- ATLAS: 91 patients, 2019–2021, intolerant/ineligible for oral antifibrotics, 48-week
  FVC near-stabilization at the high (100 mg BID) dose, HRCT stabilization/improvement
  in >70% (424B4).
- AURA: NCT07194382, IPF, Phase 2, 160 patients, RECRUITING, topline late 2027
  (ClinicalTrials.gov + Q2 release).
- SAIL OLE: NCT06951217 (ClinicalTrials.gov) — see flag 2.
- Company: CEO Lyn Baranowski, Boston, subleases from CRISPR Therapeutics (S-1/S-1/A
  "Sublease Agreement ... CRISPR Therapeutics, Inc., dated August 29, 2025"); ~$389M
  raised, $175M Series C in Sept 2023 / Jan 2024 (424B4).
- Holders: Perceptive 34,137,149 (~34.1M), SR One 27,309,719 (~27.3M), Novo Holdings
  25,899,284 (~25.9M) — all match the 424B4 principal-stockholders table.
- 505(b)(2) pathway: confirmed in 424B4 risk-factor/business text.
- Prices (Yahoo daily close): debut 04-30 $29.49 (+63.8%); 06-17 $29.31 → 06-18
  $31.45 (+7.3%); low $25.68 on 07-16; high $39.25 on 08-14; 08-28 $34.69; 09-04
  $37.39 (+107.7%). All match.
- Internal links (/blog/ipo-hemab, -aktis, -eikon, -generate, biotech-ipo-class-*)
  all resolve to non-draft posts; figure file exists. Class-median ratio $345M /
  $294.8M ≈ 1.17x matches the parent post's median.
- "Wellington 13G/A in August": confirmed — SCHEDULE 13G/A filed 2026-08-06 by CIK
  315066 (Wellington), subject Avalyn Pharma Inc.
- `scripts/blog-qc.mjs` passes with 0 errors / 0 warnings.

## Violations / flags

1. **"No in-licensing anywhere in the stack"** (pipeline section) — minor, wording.
   The 424B4 discloses an exclusive license to PARI for the eRapid/eFlow delivery
   device ("our exclusive license to customize the delivery device"). The drug
   *molecules* are internally developed and there is no Roche/Genentech license, but
   the absolute "no in-licensing anywhere" is contradicted by the PARI device license,
   which the draft never mentions. Fix: qualify (e.g., "no in-licensed drug molecule")
   or name the PARI device license.

2. **"a multi-year open-label extension ([SAIL, NCT06951217]) extends the record past
   4.5 years"** — minor, imprecise linkage. The "4.5 years" figure is correct and
   traces to the 424B4 ("over four and a half years"), but that record belongs to the
   ATLAS OLE program begun ~2021; the SAIL registry entry (NCT06951217) itself shows
   a start date of 2025-04-17 (~1 year). Fix: attribute the 4.5-year record to the OLE
   program, not to the SAIL NCT's own duration.

3. **"lower GI and liver-enzyme toxicity than oral dosing"** (ATLAS sentence) — minor,
   interpretive. The 424B4 states "low rates of side effects, including GI toxicities
   and liver enzyme elevations, which have been commonly seen with oral products."
   "Lower ... than oral dosing" is a fair reading but slightly stronger than the
   source's "low rates ... commonly seen with oral products."

4. **Price-series provenance** — minor, sourcing completeness (not a factual error).
   The provenance footer cites "the Yahoo Finance daily series for AVLN" but no Yahoo
   URL appears in Sources. All cited closes were independently re-verified against
   Yahoo and are correct; only the link is missing.

VERDICT: needs-human
