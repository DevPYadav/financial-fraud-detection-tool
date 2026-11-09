# Indian Financial Fraud Detection Tool

## Consolidated Project Scope and Requirements

**Document status:** Requirements baseline approved for preparation\
**Market:** India\
**Engagement:** 8-week Proof of Concept (PoC)\
**Prepared for:** Project planning and solution design\
**Version:** 1.0\
**Date:** 9 November 2026

------------------------------------------------------------------------

## 1. Executive summary

The project will build an AWS-hosted proof of concept for a financial
fraud and corporate-governance red-flag detection tool focused on Indian
listed companies. The primary intended customer group is stock-market
regulators, with an initial use case of helping analysts identify
companies and disclosures that may warrant further investigation.

The PoC will analyse **10 NSE/BSE-listed companies**, selected to
include companies with publicly documented financial or governance red
flags as well as companies without known fraud allegations. It will use
freely accessible public information, prioritising quarterly and annual
financial results and reports, relevant NSE/BSE notices, and selected
Indian business and financial news sources.

The tool will combine configurable rules, selected machine-learning
models and generative-AI capabilities, with human review. It will
extract financial and governance information, identify selected
anomalies and changes over time, calculate company-level risk scores,
explain triggered indicators, and provide source URLs for findings. It
will not determine that fraud has legally occurred or replace an
investigator's judgement.

The engagement is limited to an **8-week PoC**, not a production
implementation. Given the breadth of the desired capability, the PoC
will prioritise core financial and corporate-governance features.
Remaining selected features may be deferred to a later phase. No
later-phase implementation is included in this engagement.

## 2. Objectives

1.  Demonstrate whether publicly available Indian company information
    can be collected and analysed consistently.
2.  Extract relevant financial and governance information from quarterly
    and annual reports, primarily in PDF format.
3.  Identify selected financial anomalies, governance red flags and
    significant five-year changes.
4.  Generate explainable company-level risk scores and risk categories.
5.  Help analysts review findings, supporting evidence and source URLs.
6.  Evaluate the prototype against publicly documented historical cases
    and disclosures.
7.  Estimate AWS and AI-service costs for the PoC and provide indicative
    scaling projections for 500 companies and the broader NSE/BSE-listed
    universe.

## 3. Target market and users

### 3.1 Target market

-   Primary target customer: Indian stock-market regulators, such as
    SEBI.
-   Initial company universe for future expansion: NIFTY 500, with an
    eventual ambition to cover all NSE/BSE-listed companies.
-   PoC coverage: 10 companies only.

The broader company universe is a future scalability consideration, not
a delivery commitment for this PoC.

### 3.2 PoC users

-   A single common user role.
-   No differentiated role-based access in the PoC.
-   Intended users are analysts who review company risk scores, red
    flags and evidence.

## 4. Engagement boundaries

### 4.1 Included

-   A working prototype with a Streamlit dashboard.
-   Company-level analysis and risk scores.
-   Financial and governance red-flag detection within the prioritised
    feature scope.
-   Natural-language analyst questions with evidence-backed answers.
-   Excel export of risk scores and summaries.
-   Quarterly risk-score history and trends.
-   Basic user guide.
-   PoC evaluation report.
-   AWS infrastructure and AI cost estimate, including indicative
    scaling projections.

### 4.2 Excluded

-   Production-grade implementation, operational rollout or
    service-level commitments.
-   Coverage of all listed companies during the PoC.
-   Legal determination that a company or individual has committed
    fraud.
-   Automated regulatory enforcement decisions.
-   Regulator-provided or confidential data.
-   Paid third-party data subscriptions or paid market-data feeds.
-   Social-media monitoring.
-   Standalone corporate announcements as a general analysis source; the
    company-report analysis is limited to quarterly and annual financial
    results/reports.
-   SEBI enforcement orders.
-   Detailed auditor-opinion or audit-quality analysis.
-   Peer benchmarking, cross-company ranking or comparative league
    tables.
-   Automated alerts and notifications.
-   Automatic model retraining or automatic risk-weight adjustment based
    on analyst feedback.
-   Audit logging.
-   Formal knowledge-transfer or handover sessions.
-   A future implementation roadmap as a separate deliverable. The
    evaluation report will, however, include prioritised recommendations
    for possible subsequent improvements.
-   Formal production support, maintenance and ongoing operations.

## 5. Company sample and selection

-   Number of companies: **10**.
-   Sample composition: **7 companies with known public financial or
    governance red flags and 3 companies without known fraud
    allegations**.
-   The sample should cover a representative mix of sectors:
    -   Banking
    -   Financial services
    -   Information technology
    -   Pharmaceuticals
    -   Manufacturing
    -   Retail
    -   Infrastructure
-   TEKMentors will propose the 10 companies and obtain client approval.
-   Companies may be replaced if historical information is materially
    incomplete or unsuitable.
-   A formal data-quality assessment will be performed for each proposed
    company before analysis.
-   Companies with materially incomplete historical data or disclosures
    will be excluded and replaced.

## 6. Data sources and collection

### 6.1 Permitted sources

Use freely accessible public information only:

1.  NSE and BSE public filings, including quarterly and annual financial
    results/reports.
2.  Historical NSE/BSE notices, penalties and enforcement-related
    disclosures.
3.  Established Indian business and financial news publications.

No paid third-party data subscriptions, paid market feeds,
regulator-provided data or social-media sources will be used.

### 6.2 Company disclosures

-   Analyse quarterly and annual financial results and reports.
-   Analyse disclosures contained within those reports where relevant to
    the selected indicators.
-   Do not treat standalone corporate announcements as a general source
    for the PoC.
-   Historical coverage target: five years of financial information and
    relevant historical notices and news, subject to public availability
    and data quality.
-   Analysis cadence: quarterly, aligned with financial results.

### 6.3 News collection

-   Collect news weekly.
-   Start with established Indian business and financial publications.
-   Match news to companies using company names, subsidiaries, aliases,
    promoters and key directors.
-   News is contextual evidence; an article or allegation is not proof
    of fraud.

### 6.4 Collection and extraction

-   Automate collection from NSE/BSE and selected free public sources
    where technically and legally permitted.
-   Use AI/OCR-based extraction from PDF reports.
-   XBRL-based extraction is not part of the selected approach.
-   Validate extracted data for completeness, consistency and numerical
    accuracy.
-   Flag extraction failures for manual review.
-   Do not fabricate, infer or silently fill missing financial values.

### 6.5 Storage and retention

-   Store extracted data and source URLs.
-   Do not retain copies of the original PDF reports as a standard PoC
    data-store requirement.
-   Retain historical extracted company data between quarterly analyses.
-   Store quarterly company risk scores and historical risk-score
    trends.
-   Do not persist AI prompts or all detailed model outputs as a general
    data-retention feature.
-   Generate detailed explanations and evidence views from the stored
    extracted data and source references as required.

## 7. Functional scope

The overall desired capability is broad, but the 8-week PoC will
prioritise core financial and corporate-governance indicators. The
following list records the selected functional requirements.
Implementation depth will be agreed during solution design, with the
core indicators taking precedence.

### 7.1 Core financial indicators

  -----------------------------------------------------------------------
  Area                                PoC requirement
  ----------------------------------- -----------------------------------
  Revenue and profitability           Identify unusual revenue growth,
                                      unusual profit margins and
                                      inconsistencies between reported
                                      profits and operating cash flows.

  Operating cash flow                 Identify unusual differences
                                      between reported profits and
                                      operating cash flows.

  Debt and liquidity                  Identify unusual changes in debt
                                      levels and current ratios.

  Operating expenses                  Identify unusual increases or
                                      decreases in total operating
                                      expenses. No detailed
                                      expense-category analysis.

  Assets                              Identify unusual changes in total
                                      assets and fixed assets. No
                                      detailed receivables, inventory or
                                      impairment analysis under this
                                      asset indicator.

  Inventory                           Extract inventory values and flag
                                      unusual changes relative to
                                      revenue.

  Trade receivables                   Extract trade receivables and flag
                                      unusual growth relative to revenue.
                                      No ageing or collection-pattern
                                      analysis.

  Loans and advances                  Extract and highlight disclosed
                                      loans and advances.

  Contingent liabilities and legal    Extract and highlight disclosed
  cases                               contingent liabilities and pending
                                      legal cases. No trend or
                                      financial-impact assessment under
                                      this specific requirement.

  Exceptional/extraordinary items     Extract and highlight these items
                                      and identify significant changes
                                      over five years.

  Foreign exchange                    Extract disclosed foreign-currency
                                      transactions and exposure and
                                      identify significant changes over
                                      five years. No assessment of FX
                                      gains/losses relative to profits.

  Accounting policies                 Identify accounting-policy changes
                                      over five years and extract their
                                      stated financial impact. No
                                      independent assessment of whether a
                                      change is misleading.

  Restatements                        Identify restated or revised
                                      financial results and compare
                                      original and revised figures. No
                                      independent materiality or
                                      fraud-impact assessment.

  Standalone vs consolidated          Extract both sets of results and
                                      identify significant differences.
                                      No subsidiary-level performance
                                      analysis.

  NSE vs BSE figures                  Compare corresponding financial
                                      figures reported to NSE and BSE and
                                      flag differences exceeding
                                      configurable thresholds.
  -----------------------------------------------------------------------

### 7.2 Corporate-governance and ownership indicators

  -----------------------------------------------------------------------
  Area                                PoC requirement
  ----------------------------------- -----------------------------------
  Related-party transactions          Extract and highlight disclosed
                                      related-party transactions and flag
                                      significant increases or decreases
                                      over five years.

  Related-party sales and purchases   Extract separately and flag
                                      significant increases or decreases
                                      over five years.

  Outstanding related-party balances  Extract year-end balances and flag
                                      significant increases or decreases
                                      over five years.

  Loans/advances to related parties   Separately extract loans and
                                      advances to promoters, directors
                                      and related parties and flag
                                      significant increases or decreases
                                      over five years.

  Subsidiary/associate transactions   Extract transactions with
                                      subsidiaries and associate
                                      companies and flag significant
                                      increases or decreases over five
                                      years.

  Guarantees and commitments          Extract disclosed guarantees and
                                      commitments and flag significant
                                      increases or decreases over five
                                      years. No financial-exposure
                                      assessment.

  Promoter shareholding               Extract and highlight promoter
                                      shareholding percentages only. No
                                      five-year ownership trend or
                                      ownership-network analysis.

  Promoter share pledging             Extract current promoter pledging
                                      and identify significant increases
                                      or decreases over five years. Do
                                      not correlate pledging with other
                                      red flags.

  Share capital                       Extract and highlight changes in
                                      issued and paid-up share capital
                                      only.

  Dividend                            Excluded.

  Auditor changes                     Extract auditor appointments and
                                      resignations and identify frequent
                                      changes over five years. Detailed
                                      auditor opinions and audit-quality
                                      analysis are excluded.

  Key managerial personnel            Extract CEO, CFO and Company
                                      Secretary appointments/resignations
                                      and identify frequent changes over
                                      five years. Do not analyse
                                      resignation reasons.

  Independent directors/board         Extract independent-director
                                      appointments and resignations and
                                      identify frequent changes in board
                                      composition over five years. No
                                      relationship or board-position
                                      concentration analysis.

  Governance compliance               Extract compliance status and
                                      exceptions and flag repeated or
                                      significant exceptions over five
                                      years.

  Filing delays                       Identify delayed quarterly and
                                      annual financial-result filings
                                      only. No recurrence-pattern
                                      analysis or correlation with other
                                      indicators.
  -----------------------------------------------------------------------

### 7.3 Market activity indicators

These are selected requirements but are lower priority than core
financial and governance capabilities within the 8-week PoC.

  -----------------------------------------------------------------------
  Area                                PoC requirement
  ----------------------------------- -----------------------------------
  Share-price movement                Extract historical share prices and
                                      identify unusual movements around
                                      quarterly and annual
                                      financial-result announcements. No
                                      correlation with news or other
                                      financial red flags.

  Trading volume                      Extract historical trading volumes
                                      and flag unusual volume spikes
                                      around financial-result
                                      announcements.

  Short selling                       Extract publicly available
                                      short-selling data and flag unusual
                                      increases. No correlation with
                                      price movements or financial red
                                      flags.

  Insider-trading disclosures         Extract disclosed insider trades by
                                      promoters and directors and flag
                                      unusual trading patterns around
                                      financial-result announcements. No
                                      correlation with subsequent price
                                      movements.

  Bulk/block deals                    Extract publicly disclosed bulk and
                                      block deals and flag unusually
                                      large transactions and repeated
                                      activity. No buyer/seller
                                      relationship analysis.

  Credit ratings                      Extract credit-rating changes and
                                      rating actions, identify downgrades
                                      and flag repeated rating changes
                                      over five years. Do not analyse
                                      rating-agency explanations.
  -----------------------------------------------------------------------

Availability of free, sufficiently complete and historically consistent
data for these market indicators must be validated. If data cannot be
obtained from permitted public sources, the feature will be documented
as unavailable rather than populated using an unapproved paid source.

## 8. Detection approach and AI capabilities

### 8.1 Combined detection approach

Use a combination of: - Configurable, predefined rules and thresholds. -
Selected machine-learning models. - Pre-trained foundation models. -
Generative AI for document understanding and analyst assistance. - Human
review and validation.

The PoC is not a fully autonomous fraud-decision system.

### 8.2 Rules and configuration

-   Provide predefined indicators and configurable rules.
-   Allow users to enable/disable predefined indicators and adjust their
    parameters.
-   Allow analysts to adjust risk weights and thresholds.
-   Do not include a user interface for creating entirely new detection
    rules.
-   Keep the configuration suitable for a single common PoC user role.

### 8.3 Generative-AI functionality

-   Provide natural-language questions and answers for analysts.
-   Answers must be grounded in extracted company data and available
    evidence.
-   Show supporting evidence and source URLs.
-   Clearly distinguish:
    1.  Extracted facts.
    2.  Detected anomalies.
    3.  AI-generated interpretations.
-   Human validation is required before treating an interpretation as an
    investigative conclusion.

Automated investigation reports and autonomous case decisions are not
core PoC deliverables.

## 9. Risk scoring and explainability

### 9.1 Score design

-   Overall company risk score: 0--100.
-   Category-level risk scores.
-   Risk categories and explanations.
-   Individual red-flag scores may be considered later; they are not a
    required first-release scoring output.
-   Companies are analysed independently. No cross-company ranking or
    peer comparison.

### 9.2 Fixed risk categories

      Score Category
  --------- ----------
      0--30 Low
     31--60 Medium
     61--80 High
    81--100 Critical

These are the initial fixed PoC thresholds.

### 9.3 Finding-level information

For each finding, where applicable, show: - What indicator was
triggered. - Why it was triggered. - Its impact on the company/category
risk score. - Confidence: High, Medium or Low. - Source URL.

Analyst feedback options: - Relevant. - Not Relevant. - Needs Further
Review.

Feedback will be used to measure relevance and inform evaluation. It
will not automatically retrain models or change risk weights.

## 10. User interface and reports

### 10.1 Dashboard

Use Streamlit. Start with: - A dashboard showing company-level risk
scores and categories. - Company-level analysis pages. - Financial and
governance red flags. - Supporting evidence and source URLs. -
Historical quarterly risk-score trends.

### 10.2 Analyst assistant

Provide natural-language questions with evidence-backed answers, using
the extracted data and available source references.

### 10.3 Export

Provide Excel export for risk scores and summaries.

### 10.4 Alerts

No automated alerts or notifications. Analysts will manually review the
dashboard.

### 10.5 User guide

Provide a basic user guide covering dashboard navigation, company
analysis, risk scores and interpretation.

## 11. Technical architecture

### 11.1 Hosting and deployment

-   AWS cloud.
-   Host in TEKMentors' own AWS account for the PoC.
-   Design with the possibility of future migration, without committing
    to a production migration in this engagement.

### 11.2 Selected AWS and data technologies

  Capability                             Selected technology
  -------------------------------------- ---------------------------
  Generative AI / foundation models      Amazon Bedrock
  PDF OCR and document extraction        Amazon Textract
  Selected custom ML model development   Amazon SageMaker
  Relational data                        Amazon RDS for PostgreSQL
  Vector search                          PostgreSQL with pgvector
  Object storage                         Amazon S3
  User interface                         Streamlit

The detailed architecture, service configuration and pgvector deployment
compatibility must be confirmed during technical design.

### 11.3 Security

Basic PoC security: - Username/password authentication. - Encryption in
transit. - Encryption at rest. - Basic access controls. - One common
user role.

Audit logging is excluded. This is not a full enterprise cybersecurity
assessment or production security certification.

## 12. Evaluation and acceptance approach

### 12.1 Evaluation sample

Use the approved 10-company sample: - 7 companies with known public red
flags. - 3 companies without known fraud allegations.

### 12.2 Validation

-   Compare detected red flags with publicly documented historical cases
    and disclosures.
-   The provisional target is detection of at least 80% of known red
    flags in the agreed evaluation dataset.
-   This target is subject to dataset quality, the definition of a known
    red flag, availability of evidence and the agreed evaluation method.
-   Establish a false-positive baseline first; no numerical
    false-positive target has been fixed.
-   Evaluate detection accuracy, explainability and analyst
    productivity.
-   Analyst feedback will be captured as Relevant, Not Relevant or Needs
    Further Review and used to measure relevance.

The 80% target is a PoC evaluation target, not a guarantee of detecting
all fraud or a claim of legal fraud-detection accuracy.

### 12.3 Evaluation report

Include: - Evaluation dataset and methodology. - Detected results
against known public red flags. - Detection performance and accuracy
observations. - False-positive baseline. - Explainability and evidence
traceability observations. - Analyst productivity observations. -
Data-quality limitations and unavailable data. - Technical and
functional limitations. - Prioritised recommendations for a subsequent
phase.

## 13. Delivery plan and timeline

**Total duration: 8 weeks.**

A proposed high-level sequencing is:

  -----------------------------------------------------------------------
  Period                  Focus                   Indicative outputs
  ----------------------- ----------------------- -----------------------
  Week 1                  Mobilisation, company   Approved company
                          selection, data-source  sample, source
                          validation and          inventory, data-quality
                          data-quality assessment findings

  Weeks 2--3              Data collection, PDF    Ingestion/extraction
                          extraction, validation  pipeline and validated
                          and storage foundation  historical data for
                                                  priority indicators

  Weeks 3--5              Core financial and      Priority detection
                          governance rules,       indicators, scoring
                          anomaly detection and   logic and
                          risk scoring            explainability

  Weeks 5--6              Dashboard, company      Working Streamlit
                          analysis and analyst    prototype
                          Q&A                     

  Week 7                  Testing,                Test results and
                          historical-case         initial evaluation
                          validation and tuning   

  Week 8                  Final evaluation, cost  PoC evaluation report,
                          estimate and            AWS cost estimate and
                          documentation           user guide
  -----------------------------------------------------------------------

This is an indicative plan. Detailed sequencing will depend on
public-data availability, PDF quality, source access constraints and the
final prioritisation of indicators.

## 14. Deliverables

1.  Working AWS-hosted PoC prototype.
2.  Streamlit dashboard with company-level risk scores and analysis.
3.  Data collection, PDF extraction and validation capability for agreed
    sources and priority indicators.
4.  Configurable predefined detection indicators and scoring parameters.
5.  Natural-language analyst Q&A with evidence-backed answers.
6.  Excel export of risk scores and summaries.
7.  Basic user guide.
8.  PoC evaluation report, including limitations and prioritised
    recommendations.
9.  AWS infrastructure and AI cost estimate for the PoC, with indicative
    projections for 500 companies and all NSE/BSE-listed companies.

No formal knowledge-transfer or handover session is included.

## 15. Cost estimation

Prepare an estimate covering: - AWS infrastructure costs for the
10-company PoC. - Amazon Bedrock usage. - Amazon Textract usage. -
Amazon SageMaker usage, where applicable. - RDS PostgreSQL, S3,
networking and supporting services. - Indicative scale projections for
500 companies and the broader NSE/BSE-listed universe.

The estimate must document assumptions such as report volume, page
count, extraction frequency, model usage, storage retention, query
volume and compute sizing. Scale projections are indicative and are not
a commitment to deliver or operate at that scale.

## 16. Intellectual property and licensing

Source-code ownership and licensing are open for commercial negotiation
and must be agreed separately before contract execution or delivery.

## 17. Assumptions, dependencies and constraints

1.  Public data is accessible without paid subscriptions and can be
    collected in accordance with applicable website terms, access
    policies and law.
2.  The client will review and approve the proposed 10-company sample in
    a timely manner.
3.  The client will provide timely clarification or feedback where
    needed.
4.  Historical data availability and document quality may vary by
    company and year.
5.  Companies with materially incomplete data will be replaced, subject
    to approval where required.
6.  The prototype will not infer missing values or present unverified AI
    interpretations as facts.
7.  Market-activity and other lower-priority data may not be available
    free of charge or in a consistent historical format. Such features
    may be deferred.
8.  The 8-week duration requires prioritisation; it does not imply that
    every item in the broad functional inventory will be fully
    implemented.
9.  The PoC is intended to identify potential red flags for human
    investigation, not to establish fraud, culpability or regulatory
    liability.
10. No production-grade resilience, scale, security certification,
    operational support or service levels are included.

## 18. Decisions requiring confirmation during solution design

These are implementation details not yet fully specified by the
requirements choices and should be resolved during project
initiation/design:

-   Exact company names and the public evidence used to classify the 7
    red-flag and 3 comparison companies.
-   Exact list of news publications and permitted collection method.
-   Precise definition of a "known red flag" for evaluation and the
    evidence cut-off date.
-   Financial indicator formulas, anomaly thresholds, materiality rules
    and risk-weight defaults.
-   Mapping of individual indicators into risk-score categories and
    aggregation logic.
-   The operational definition of "unusual", "significant" and
    "frequent" for each five-year trend.
-   Exact historical periods and reporting dates available for each
    company.
-   Handling of restated data in historical evaluation.
-   Availability and licensing/terms for public market-price,
    trading-volume, short-selling, insider-trading, bulk/block-deal and
    credit-rating information.
-   Analyst productivity measurement method.
-   AWS region, sizing assumptions, access/network configuration and
    final service architecture.
-   Whether any additional user-facing configuration controls are
    required beyond the selected rules and weight/threshold settings.

## 19. Scope interpretation and priority rule

Where the broad functional inventory exceeds the available 8-week PoC
capacity, implementation priority is:

1.  Core financial indicators and financial-statement consistency
    checks.
2.  Core corporate-governance and related-party indicators.
3.  Company-level risk scoring, evidence traceability and
    explainability.
4.  Dashboard and analyst natural-language Q&A.
5.  Historical-case validation and evaluation.
6.  Lower-priority market-activity indicators and other extended
    features, only where time and free public data availability permit.

Items not implemented during the PoC may be documented as deferred
recommendations. Their implementation is not included in the current
engagement.

------------------------------------------------------------------------

**End of scope document**
