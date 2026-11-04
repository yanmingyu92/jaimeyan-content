# Critique review — `content/posts/ipo-eikon-2026.md`

Mode: no data pack / no evidence cards. Evidence base = the linked sources in the
draft's Sources section, fetched directly. Report violations only (per instruction —
no rewrite applied).

Sources actually fetched: pricing release, BioPharma Dive, Fierce Biotech, The Pharma
Letter (paywalled — lede only), S-1/A, 424B4, Q2 2026 10-Q, Q2 results release (ex99.1),
8-K (board resignations), ClinicalTrials.gov NCT06697301 / NCT07365319 / NCT06246110,
Yahoo Finance daily series for EIKN and MANE. **Smartkarma returned HTTP 403** — not
verifiable (noted below).

## Violations

1. **"the largest biotech IPO since Acelyrin's 2023 offering" (line 35) — misattributed and contradicted.**
   The sentence attributes this to BioPharma Dive, but the linked BioPharma Dive article
   makes no mention of Acelyrin or 2023; it calls Eikon's pricing week "the busiest week
   for biotech IPO activity since early last year." The linked Fierce Biotech article
   states the opposite framing: "largest biotech IPO since 2024, overtaking Aktis
   Oncology's $318 million offering last month." So "Acelyrin's 2023 offering" has no
   provenance in any linked source and conflicts with the Fierce source ("since 2024").
   The trailing editorial aside ("has not aged well for either name") also imports an
   unsourced implication about Acelyrin.

2. **"the post-IPO high is $16.26, set February 18" (line 41) — $16.26 is a close, not the intraday high.**
   Yahoo Finance EIKN daily series: the post-IPO intraday high is **$17.40 on Feb 5** (the
   debut day), and the Feb 18 intraday high was **$16.39**. **$16.26 is the Feb 18 closing
   price** (the highest close). Labeled as a "high," the number is wrong; the true
   post-IPO intraday peak is $17.40, not $16.26.

3. **"The June 10 low was $8.36" / "bottomed at $8.36 on June 10" (line 41; repeated in Key takeaways) — $8.36 is a close, not the low.**
   Yahoo Finance EIKN: the post-IPO intraday low is **$7.90 on Apr 28**, and the Jun 10
   intraday low was **$8.32**. **$8.36 is the Jun 10 closing price** (the lowest close).
   The draft's "bottom" understates the true drawdown (the stock printed $7.90, ~$0.46
   below the stated low). The three single-day drop figures (10.6% Mar 12, 9.7%/9.5%
   Apr 24/27) and the cited closes ($17.05 open / $15.00 close Feb 5, $15.72 Feb 17,
   $8.56 Apr 28, $9.15 Aug 3, $10.98 Aug 28, $10.86 Sep 4) all reconcile to Yahoo; the
   error is specifically that "high"/"low" labels are applied to closing values.

4. **Net-proceeds breakdown: "$6.4M of expenses" is not a disclosed figure (Table 1 caption).**
   The 10-Q states: "net proceeds from the initial public offering were $348.1 million,
   after deducting underwriting discounts and commissions and other offering costs of
   $33.1 million." The 424B4 states underwriting of $1.26/share (≈$26.7M) and *estimated*
   offering expenses of "approximately $5.5 million" (estimated net ≈$349.0M). "$6.4M
   expenses" appears in neither source; it is the residual $33.1M − $26.7M. $348.1M and
   $26.7M are fine; the $6.4M expense figure is an inferred split (and diverges from the
   424B4's stated $5.5M) with no verbatim provenance.

5. **Veradermics "+479%" (One Take) — unsourced and inconsistent with the cited class piece.**
   The only Veradermics return figure cited in this article is the linked class piece's
   "+476.1%" (marked Aug 28). "+479%" is a different (Sep 4) mark with no source in this
   article and is not reconciled to the cited +476.1%.

6. **Post-IPO 8-K enumeration "earnings, two company-update decks, one director
   appointment" (line 47) — no provenance.**
   The only 8-K linked is the resignation filing. The specific enumeration of the other
   post-IPO 8-Ks — and the blanket conclusion "every 8-K since the IPO is routine … with
   no trial failure, delay, or safety disclosure" — rests on an unlinked 8-K sweep. The
   conclusion itself is unverifiable from the linked sources.

## Verified clean (no violation)

- Deal terms: 21,177,600 shares @ $18.00; 3,176,640-share (15%) option; 17,648,000-share
  $16–18 range ($282–318M); ~20% upsize; $381M gross — verified against pricing release,
  S-1/A, 10-Q.
- Pipeline: EIK1001 in-licensed from Seven and Eight Biotherapeutics Corp. (prior name
  BDB001), TLR7/8, first-line advanced-melanoma Phase 2/3 + pembro with first interim
  guided H2 2026 (~740 pts, recruiting); NSCLC Phase 2/3 (NCT07365319, 750 pts, now
  recruiting, site selection at IPO); TeLuRide-005 Phase 2 (NCT06246110, 70 pts,
  active-not-recruiting, primary completion Dec 2026); EIK1003/EIK1004 selective PARP1
  from Impact Therapeutics (Shanghai) Inc.; EIK1005 WRN helicase, MSI-high, first internal
  program — all confirmed in S-1/A + ClinicalTrials.gov.
- Licensing obligations $630M development/regulatory + $1.1B sales + high-single-digit to
  low-teen royalties; >$1.1B private raise; backers Column Group / Lux / Catalyst4;
  platform (Betzig Nobel super-resolution, Tjian co-founder, Perlmutter CEO) — confirmed
  in S-1/A.
- Cash $531.2M, Q2 net loss $88.4M, R&D $75.5M, runway into H2 2027 — confirmed in 10-Q /
  ex99.1.
- Lockup: 32,924,231 shares (≈32.9M) unlocked Aug 3; 180-day term — confirmed.
- Greenshoe not exercised — supported by 10-Q (21,177,600 shares sold; offering terminated
  after sale of all registered securities).
- Board resignations: Leon Chen (partner, The Column Group) and Joshua Wolfe (Lux Capital)
  effective Jul 31, 8-K filed Aug 3 — confirmed (S-1/A confirms both affiliations).

## Sources not verifiable

- **Smartkarma** — HTTP 403; the "Six Months Later" piece could not be fetched.
- **The Pharma Letter** — paywalled; only the visible lede retrieved ("largest biotech IPO
  of the year so far", "fell nearly 17%", "closed at $15", "21.2M shares at $18, top of
  range"), which is consistent with the draft.

VERDICT: needs-human
