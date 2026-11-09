# Company Sample Selection Criteria

These rules for choosing the 10 PoC companies are fixed before any company is picked, so the client can approve the method as well as the list. Source: [PoC scope](../../indian_financial_fraud_detection_poc_scope.md) §5, §6.1 and §12.1.

## Sample composition

- **10 companies** listed on NSE and/or BSE.
- **7 red-flag companies:** companies with publicly documented financial or governance red flags.
- **3 control companies:** companies without known fraud allegations.
- Companies are analysed independently. The sample is not used for ranking or peer comparison.

## Sectors

The sample should cover this mix of sectors:

1. Banking
2. Financial services
3. Information technology
4. Pharmaceuticals
5. Manufacturing
6. Retail
7. Infrastructure

Rules:

- Every sector should have at least one company, red-flag or control.
- No sector should have more than two companies, unless that is the only way to meet the 7-to-3 balance.
- If 10 companies cannot cover all 7 sectors (for example, no eligible red-flag or control company exists in a sector), fill the gap in this order:
  1. Keep the 7-to-3 balance. It always takes priority over sector coverage.
  2. Prefer a company in a missing sector over a second company in a covered sector.
  3. If a sector still cannot be covered, record it under "Sector coverage gaps" in `company-sample.md` with the reason (for example "no listed retail company with five years of results and qualifying evidence"). Sectors are never silently dropped.

## What qualifies as a red-flag company

A company is "red flag" when at least one of the following is publicly documented, with a dated public source, during the five-year analysis window or up to the evidence cut-off date:

- An exchange (NSE/BSE) notice, penalty, suspension or enforcement-related disclosure about financial reporting, governance or disclosure failures.
- A restatement or revision of published financial results because of errors or irregularities.
- A statutory auditor resignation, qualified opinion or disclaimer that cites financial-reporting or governance concerns, as disclosed in the company's filings.
- A forensic audit, fund-diversion finding or accounting irregularity disclosed by the company or reported to the exchanges.
- A regulatory action on financial reporting or governance, reported by at least one established Indian business publication from the news policy (#9).

Evidence rules:

- Evidence must come from free public sources (scope §6.1): NSE/BSE filings and notices, the company's own filings, or established Indian business and financial news publications.
- Each red-flag company needs **at least one public evidence link that opens**. If the only evidence is news, it needs **at least two independent publications**.
- Allegations are recorded as allegations. Selection does not claim that fraud occurred.
- The red flags used to select a company also become that company's known red flags for evaluation (#66, #68). They are listed in `company-sample.md`.

## What qualifies as "no known allegations" (control)

A company qualifies as a control company when a documented search finds none of the following, from the start of the five-year window to the cut-off date:

- Any of the red-flag evidence types listed above.
- A fraud or fund-diversion allegation reported by an established Indian business publication.

Routine procedural matters, such as a small exchange fine for a late filing that was later fixed, do not disqualify a control company. They must be listed in `company-sample.md`.

The search is documented in `company-sample.md` with the sources checked, the search terms and the date of the search.

## Data availability

- Five years of quarterly and annual results must be publicly available for each company.
- The **five-year window** is the five most recent complete Indian financial years before the evidence cut-off date. For a cut-off in FY2027, that is FY2022 to FY2026 (Q1 FY2022 to Q4 FY2026).
- "Available" means that, for each year in the window, the four quarterly results and the annual report can be opened from NSE, BSE or the company's investor-relations page.
- A company missing **any annual report**, or **more than two quarterly results**, in the window is not eligible. Up to two missing quarters are allowed, but they must be listed in `company-sample.md`.
- A full data-quality assessment is a separate step (#17) and may still lead to a company being replaced (#7).

## Delisted, merged or renamed companies

- **Renamed:** eligible. Record former names in `company-sample.md`. Use them when searching filings and news.
- **Merged or amalgamated into another company during the window:** not eligible, because the five-year series is broken. Exception: if the listed entity is the surviving company and its own results cover the full window, it is eligible, with the merger recorded.
- **Delisted, or suspended from trading, during the window:** eligible only if all filings for the full window can still be opened from NSE, BSE or the company's site. Otherwise not eligible. Record the listing status and its date.
- **Listed during the window (recent IPO):** not eligible unless five years of results are available.

## Evidence cut-off date

Evidence used for selection and evaluation is limited to what was public on or before the cut-off date recorded in `company-sample.md`. Later events are not used to reclassify companies during the PoC.

## Client approval

- TEKMentors proposes the 10 companies, using these criteria, in `company-sample.md` (#6).
- **The client must approve the final list before analysis starts.** The client may also be asked to approve this method first.
- The approval decision, approver name and date are recorded in the "Client approval" section of `Code/docs/company-sample.md`. A link to the written approval (e-mail or meeting note reference) is added as a comment on issue #6.
- Any later change to the list follows the replacement procedure (#7) and needs its own approval.
