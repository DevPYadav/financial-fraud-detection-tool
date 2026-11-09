# Indian Financial Fraud Detection PoC --- Backlog

**Backlog basis:** Approved Indian Financial Fraud Detection PoC scope,
version 1.0\
**Delivery window:** 8 weeks\
**PoC sample:** 10 NSE/BSE-listed companies (7 with publicly documented
red flags and 3 without known fraud allegations)\
**Implementation priority:** Core financial indicators,
corporate-governance indicators, risk scoring, evidence, dashboard and
evaluation. Lower-priority market-activity features are deferred unless
time and permitted free public data allow.

Tasks are intentionally small and independently assignable. Each task
contains its own context so it can be handed to a contributor who has
not read the other tasks. This document defines work only; it does not
contain implementation code.

## 1. Create an empty project with a passing test

Goal: Establish a clean, reproducible project skeleton with at least one
passing automated test. Description: Create the repository structure for
the Indian financial fraud detection PoC, including application, tests,
configuration and documentation directories. Add the minimum test-runner
configuration and one trivial test that passes on a clean checkout; do
not implement business functionality.

## 2. Document local development setup

Goal: Make it possible for a new contributor to prepare and verify a
local development environment. Description: Document supported
Python/runtime versions, environment creation, dependency installation,
configuration setup and test commands for the PoC. Include
troubleshooting guidance for common setup failures and avoid placing
credentials in the repository.

## 3. Define environment and configuration conventions

Goal: Establish a consistent, secure approach for application
configuration. Description: Document the configuration values required
for local, test and AWS environments, including database, storage, model
and source settings. Define how secrets are supplied through environment
variables or a secrets service, and provide safe example configuration
with no real credentials.

## 4. Define the PoC data dictionary

Goal: Create a shared definition of the company, filing, financial
metric, disclosure, finding and risk-score data used by the PoC.
Description: Document field names, meanings, units, periods, source
references and null-handling rules for the core data entities. Include
conventions that distinguish extracted facts, detected anomalies and
AI-generated interpretations.

## 5. Define company sample selection criteria

Goal: Establish transparent criteria for choosing the 10 companies used
in the PoC. Description: Define how TEKMentors will propose 7 companies
with publicly documented financial or governance red flags and 3
companies without known fraud allegations, across the selected
representative sectors. Record the evidence needed to support sample
classification and the requirement for client approval.

## 6. Prepare the proposed 10-company sample

Goal: Produce a client-reviewable list of 10 eligible NSE/BSE-listed
companies. Description: Research candidate companies using permitted
free public sources and check whether five years of quarterly and annual
financial information can reasonably be obtained. Record sector,
identifiers, red-flag/control-sample rationale, source links and any
data gaps, then submit the proposed list for client approval.

## 7. Define company replacement procedure

Goal: Ensure an unsuitable company can be replaced without compromising
the evaluation sample. Description: Document the criteria for excluding
a company with materially incomplete or unsuitable historical
disclosures and the steps for selecting a replacement. Preserve the
intended 7-to-3 sample composition and record the reason for every
replacement.

## 8. Inventory permitted public data sources

Goal: Identify the free public sources that may be used by the PoC.
Description: Create a source register for NSE and BSE quarterly/annual
financial results and reports, historical exchange notices and
penalties, and selected established Indian business/financial news
publications. Record access method, available history, terms or usage
constraints, update frequency and source URL; exclude paid feeds,
regulator-provided data and social media.

## 9. Define news source and collection policy

Goal: Establish a compliant and repeatable approach for weekly
collection of relevant Indian business and financial news. Description:
Propose the initial publication list and document permitted access
methods, collection limits, attribution and source-link retention.
Define how company names, subsidiaries, aliases, promoters and key
directors will be used for entity matching, while treating news
allegations as context rather than proof.

## 10. Design the source-document and filing metadata model

Goal: Record enough filing metadata to identify, retrieve and trace
every extracted result. Description: Define the metadata fields for
exchange, company, filing type, reporting period, publication date,
retrieval date and source URL. Include duplicate detection and a way to
distinguish quarterly results, annual reports, exchange notices and news
items.

## 11. Build the public filing discovery workflow

Goal: Discover relevant quarterly and annual financial reports for the
approved PoC companies. Description: Implement or configure a repeatable
workflow to locate permitted NSE/BSE filings for the 10 approved
companies and the required historical period. Capture filing metadata
and source URLs, and do not collect standalone corporate announcements
as a general analysis source.

## 12. Build weekly public news discovery

Goal: Collect eligible news references for the approved companies on a
weekly cadence. Description: Implement or configure the weekly discovery
workflow against the approved free publications and permitted access
methods. Store article metadata and URLs, match likely company
references using the agreed aliases and related entity names, and retain
the original publication attribution.

## 13. Create the filing ingestion register

Goal: Track which expected reports have been found, retrieved and
processed for each company. Description: Provide a register that records
company, financial period, filing type, source URL, processing status
and failure reason. Make missing periods visible so the data-quality
assessment can identify gaps rather than silently treating absent
reports as zero values.

## 14. Extract text and tables from PDF reports

Goal: Convert public quarterly and annual PDF reports into
machine-processable content. Description: Use Amazon Textract or the
selected OCR/document extraction approach to extract text and tabular
content from eligible reports. Preserve the association between
extracted content, company, reporting period and source URL, and flag
unreadable or failed documents for manual review.

## 15. Define financial table normalization rules

Goal: Normalize extracted financial values so that they can be compared
consistently across reports and periods. Description: Document and
implement conventions for units, currencies, signs, parentheses, decimal
formats, consolidated versus standalone statements and reporting
periods. Preserve the original extracted value and its normalized value
so that corrections and validation remain traceable.

## 16. Validate extracted financial values

Goal: Detect incomplete, inconsistent or numerically implausible
extracted financial data before analysis. Description: Implement checks
for required fields, missing periods, duplicate rows, unit mismatches
and basic arithmetic or cross-statement consistency where applicable.
Record validation outcomes and route extraction or numerical issues to
manual review without inventing missing values.

## 17. Perform company-level data-quality assessment

Goal: Decide whether each proposed company has sufficient historical
data for reliable PoC analysis. Description: Assess completeness,
consistency, numerical accuracy and availability of the five-year
financial and disclosure history for each company. Exclude companies
with material gaps and recommend replacements, documenting the evidence
and client approval where needed.

## 18. Store extracted data and source references

Goal: Persist validated extracted information without retaining original
PDF copies as a standard data-store requirement. Description: Store
normalized extracted facts, reporting periods, validation status and
source URLs in the selected data store. Retain historical extracted
company data between quarterly runs, and document that original report
PDFs are not retained in the PoC data store.

## 19. Configure PostgreSQL and pgvector data services

Goal: Provide the relational and vector data foundation selected for the
PoC. Description: Provision or configure PostgreSQL in the approved AWS
environment and verify compatibility for the planned pgvector extension.
Document connection settings, schema migration approach, backup
assumptions and access restrictions without embedding credentials in
source control.

## 20. Configure S3 for permitted PoC artifacts

Goal: Provide controlled object storage for application artifacts that
need S3. Description: Create the required S3 storage structure for
non-original-PDF artifacts such as approved exports or processing
artifacts, with encryption and access controls. Ensure the storage
design does not contradict the requirement not to retain original report
PDFs as a standard data-store feature.

## 21. Define core financial indicator formulas

Goal: Agree on precise, testable calculations for the highest-priority
financial red flags. Description: Specify formulas, required inputs,
units, reporting-period comparisons and missing-data behaviour for
revenue growth, profit margins, profit versus operating cash flow, debt,
current ratio, operating expenses, total assets and fixed assets.
Document the definitions of unusual movement and materiality before
implementing the rules.

## 22. Implement revenue and profitability checks

Goal: Identify unusual revenue growth and profit-margin movements in
company financial results. Description: Calculate the agreed revenue
growth and profit-margin measures over available reporting periods and
flag values that cross the approved thresholds. Include the company,
period, calculation inputs, explanation and source URL for each finding.

## 23. Implement profit-to-cash-flow checks

Goal: Identify unusual differences between reported profit and operating
cash flow. Description: Compare the agreed profit measure with operating
cash flow for corresponding periods and calculate the approved
difference or ratio. Flag unusual divergence with the underlying
figures, reporting period, rationale and source URL.

## 24. Implement debt and liquidity checks

Goal: Identify unusual changes in company debt levels and current
ratios. Description: Calculate debt measures and current ratios from
validated financial statement values using the agreed definitions. Flag
material changes over time and retain the input values, calculation,
period and source URL supporting each finding.

## 25. Implement operating expense checks

Goal: Identify unusual increases or decreases in total operating
expenses. Description: Compare total operating expenses across
comparable reporting periods using the agreed thresholds and period
alignment. Do not introduce expense-category analysis; show the values,
movement, reason for the flag and source URL.

## 26. Implement asset movement checks

Goal: Identify unusual changes in total assets and fixed assets.
Description: Compare total assets and fixed assets across available
historical periods using approved calculations and thresholds. Keep this
task limited to total and fixed assets; inventory and receivables have
their own separately defined indicators.

## 27. Implement inventory-to-revenue checks

Goal: Identify unusual inventory changes relative to revenue.
Description: Extract inventory values and compare their movement with
revenue over comparable periods. Flag unusual divergence using agreed
thresholds and provide the underlying values, reporting period and
source URL.

## 28. Implement receivables-to-revenue checks

Goal: Identify unusual growth in trade receivables relative to revenue.
Description: Extract trade receivables and compare their growth with
revenue over comparable periods. Do not add receivables ageing or
collection-pattern analysis; include the calculation, finding
explanation and source URL.

## 29. Extract loans, advances and contingent liabilities

Goal: Make disclosed loans and advances, contingent liabilities and
pending legal cases available to analysts. Description: Extract and
highlight these disclosures from eligible financial reports, preserving
amounts, parties where disclosed, reporting periods and source URLs.
This task is extraction and presentation only; do not add trend or
financial-impact scoring beyond separately approved related-party loan
trend rules.

## 30. Implement related-party transaction trend checks

Goal: Identify significant five-year increases or decreases in disclosed
related-party transactions. Description: Extract related-party
transaction disclosures and compare comparable categories across the
five-year history. Show the reported values, direction and magnitude of
change, reporting periods and source URLs without inferring undisclosed
relationships.

## 31. Implement related-party sales and purchase trends

Goal: Identify significant five-year changes in related-party sales and
purchases. Description: Extract related-party sales and purchases as
separate measures and compare them over available historical periods.
Flag significant increases or decreases using agreed thresholds and show
the supporting disclosures and source URLs.

## 32. Implement outstanding related-party balance trends

Goal: Identify significant five-year changes in year-end outstanding
related-party balances. Description: Extract year-end balances and
compare corresponding categories across reporting years. Flag
significant increases or decreases without assessing the balances
relative to revenue or total assets.

## 33. Implement related-party loans and advances trends

Goal: Identify significant five-year changes in loans and advances to
promoters, directors and related parties. Description: Extract these
disclosed balances separately from general loans and advances and
compare them over time. Flag significant increases or decreases,
preserving the disclosed party/category, amount, period and source URL
without adding company-size materiality analysis.

## 34. Implement subsidiary and associate transaction trends

Goal: Identify significant five-year changes in transactions with
subsidiaries and associate companies. Description: Extract the disclosed
transactions with subsidiaries and associates and compare like-for-like
categories over time. Flag significant increases or decreases and show
the source disclosure, reporting period and URL.

## 35. Implement guarantees and commitments trends

Goal: Identify significant five-year changes in disclosed guarantees and
commitments. Description: Extract guarantees and commitments made on
behalf of subsidiaries, promoters or related parties where disclosed.
Compare values over time and flag significant increases or decreases
without estimating financial exposure relative to company size.

## 36. Extract promoter ownership and share pledging

Goal: Present promoter shareholding percentages and promoter
share-pledging disclosures. Description: Extract and highlight promoter
shareholding percentages without calculating five-year ownership trends
or ownership networks. Separately extract current promoter pledging and
identify significant increases or decreases over five years, without
correlating pledging changes with other red flags.

## 37. Extract share-capital changes

Goal: Highlight changes in issued and paid-up share capital.
Description: Extract issued and paid-up share-capital values from
eligible financial reports and identify reported changes across periods.
Do not expand this task to authorised capital, preferential allotments,
rights issues or bonus issues as separate event analysis.

## 38. Implement auditor and leadership change indicators

Goal: Identify frequent changes in auditors and key managerial personnel
over five years. Description: Extract auditor appointments and
resignations, and appointments/resignations of CEOs, CFOs and Company
Secretaries. Flag frequent changes using agreed definitions; do not
analyse auditor opinions, audit quality or reasons for individual
resignations.

## 39. Implement independent-director and board-change indicators

Goal: Identify frequent changes in independent directors and board
composition over five years. Description: Extract independent-director
appointments and resignations and build a period-based board-composition
history from available disclosures. Flag frequent changes without
inferring personal relationships or concentration of board positions.

## 40. Implement governance-compliance exception indicators

Goal: Highlight repeated or significant corporate-governance compliance
exceptions. Description: Extract disclosed compliance status and
exceptions from eligible reports and compare exceptions over the
five-year history where available. Flag repeated or significant
exceptions using agreed definitions and retain the supporting disclosure
URL.

## 41. Identify delayed quarterly and annual result filings

Goal: Highlight delayed quarterly and annual financial-result filings.
Description: Compare filing dates with the applicable expected filing
deadlines using a documented source for the deadline. Present the
company, filing period, actual filing date, expected deadline and source
references; do not add recurrence scoring or correlation with other red
flags.

## 42. Identify NSE/BSE financial figure discrepancies

Goal: Flag differences between corresponding financial figures reported
to NSE and BSE. Description: Match equivalent figures for the same
company and reporting period and compare normalized values. Flag
differences that exceed configurable thresholds and show both source
URLs, values and the calculated difference.

## 43. Extract accounting-policy changes and restatements

Goal: Surface accounting-policy changes and revised financial results
with their disclosed context. Description: Extract accounting-policy
changes over five years and capture their stated financial impact.
Identify restated or revised results and compare original with revised
figures, without independently declaring a change misleading or
assigning fraud intent.

## 44. Compare standalone and consolidated results

Goal: Identify significant differences between standalone and
consolidated financial results. Description: Extract both sets of
financial results for the same company and reporting period and compare
the agreed financial measures. Flag significant differences with both
sets of values and source URLs; do not perform subsidiary-level
performance analysis.

## 45. Extract exceptional items and foreign-exchange disclosures

Goal: Highlight exceptional/extraordinary items and historical
foreign-currency exposure. Description: Extract exceptional and
extraordinary items and identify significant changes over five years.
Also extract foreign-currency transactions and exposure and identify
significant changes over five years, without assessing FX gains or
losses relative to profits.

## 46. Define finding and evidence representation

Goal: Standardize how every detected red flag is represented and traced
to public evidence. Description: Define a finding structure containing
company, indicator, reporting period, extracted facts, calculation or
rule result, confidence, explanation and source URL. Ensure extracted
facts, detected anomalies and AI-generated interpretations are
explicitly labelled as different information types.

## 47. Implement finding confidence labels

Goal: Assign a High, Medium or Low confidence label to each finding.
Description: Define a consistent confidence approach based on source
quality, extraction validation and data completeness. Apply the label to
findings and ensure missing or weak source data lowers confidence rather
than causing the system to fabricate certainty.

## 48. Implement explainable risk contribution

Goal: Explain why an indicator was triggered and how it affects the
company risk score. Description: For each scored finding, show the rule
or model reason, relevant input values and contribution to the
applicable category and overall score. Include a source URL and avoid
presenting an AI interpretation as an extracted fact.

## 49. Define risk categories and score aggregation

Goal: Establish the PoC's 0--100 company risk score and fixed risk
categories. Description: Document how indicator results and category
scores combine into an overall score, including treatment of missing
indicators and duplicate findings. Apply the agreed fixed categories:
Low 0--30, Medium 31--60, High 61--80 and Critical 81--100.

## 50. Implement configurable predefined detection rules

Goal: Allow the PoC user to enable, disable and adjust predefined
detection indicators. Description: Provide configuration for the
predefined rules and their thresholds without allowing users to create
entirely new rule types. Keep the configuration consistent with the
single common PoC user role and record the effective configuration used
for a scoring run.

## 51. Implement analyst-adjustable weights and thresholds

Goal: Allow analysts to adjust risk weights and thresholds used by the
PoC. Description: Provide a controlled configuration interface for
changing the approved indicator weights and thresholds. Validate inputs
and make the resulting score calculation reproducible; changes must not
silently rewrite previously stored quarterly scores.

## 52. Implement quarterly risk-score history

Goal: Retain and display company risk scores across quarterly analysis
runs. Description: Store each company's overall score, category scores,
risk category, analysis period and run timestamp for each completed
quarterly analysis. Support historical trend display without retaining
all AI prompts or every detailed model output.

## 53. Build the company risk dashboard

Goal: Give analysts a clear overview of risk scores for the 10 PoC
companies. Description: Build a Streamlit dashboard that displays
company-level overall scores, risk categories and available quarterly
score trends. Do not add peer rankings, cross-company comparisons or
automated alerts.

## 54. Build the company analysis view

Goal: Let an analyst inspect a selected company's risk indicators and
supporting evidence. Description: Provide a company-level view of
category scores, triggered findings, confidence labels, explanations and
source URLs. Make it clear that findings are potential red flags for
human investigation and not legal conclusions of fraud.

## 55. Add natural-language analyst Q&A

Goal: Let analysts ask questions about a company and receive
evidence-backed answers. Description: Use Amazon Bedrock or the selected
foundation model to answer natural-language questions using validated
extracted company data and available source references. Answers must
cite supporting source URLs, distinguish facts from interpretations and
state when the available data cannot answer a question.

## 56. Add analyst finding feedback

Goal: Capture an analyst's assessment of each finding. Description:
Allow the user to mark a finding as Relevant, Not Relevant or Needs
Further Review and retain the feedback for evaluation. Do not
automatically retrain models or change rules, weights or thresholds
based on this feedback.

## 57. Add Excel export for scores and summaries

Goal: Allow analysts to export company risk scores and summary
information. Description: Provide an Excel export containing company
identifiers, analysis period, overall score, category scores and risk
category, with relevant summary fields. Ensure exported values match the
dashboard and do not include unsupported claims or untraceable findings.

## 58. Implement basic username/password authentication

Goal: Restrict access to the PoC dashboard using basic authentication.
Description: Provide a basic sign-in mechanism suitable for a limited
PoC with one common user role. Store or verify credentials securely and
do not implement differentiated role permissions or audit logging.

## 59. Apply encryption and basic access controls

Goal: Protect PoC data and application traffic using baseline security
controls. Description: Configure encryption in transit and at rest for
the selected AWS services and restrict access to the application,
database and storage resources to the minimum required. Document the
controls and explicitly note that this is not a production security
certification or full cybersecurity assessment.

## 60. Integrate Amazon Bedrock for approved AI tasks

Goal: Establish a controlled foundation-model integration for document
interpretation and analyst Q&A. Description: Configure the selected
Amazon Bedrock model access and a small integration boundary for
approved PoC use cases. Define prompt/input handling, response
validation, error handling and cost visibility, and do not treat model
output as verified fact without evidence.

## 61. Integrate Amazon Textract document processing

Goal: Make OCR and document extraction available through the selected
AWS service. Description: Configure Amazon Textract for eligible public
PDF report processing and capture extraction status, output and
failures. Verify representative report layouts and ensure original PDFs
are not retained in the standard application data store.

## 62. Establish SageMaker model experimentation boundary

Goal: Provide a controlled path for selected custom ML experiments
within the PoC. Description: Document and configure the minimum
SageMaker capability needed for approved model experiments, including
data inputs, experiment tracking assumptions and output evaluation. Keep
custom modelling limited to the agreed indicators and avoid making model
development a dependency for every rule-based finding.

## 63. Create representative automated tests for data and indicators

Goal: Verify that core extraction, normalization and red-flag
calculations behave as specified. Description: Prepare synthetic or
appropriately de-identified test cases covering valid values, missing
periods, unit differences, restatements and threshold boundaries. Test
the key financial and governance calculations and verify that every
finding includes the expected period and source reference.

## 64. Test end-to-end analysis for one company

Goal: Demonstrate a complete data-to-risk-score workflow for a single
approved company. Description: Process available quarterly and annual
reports for one company through discovery, extraction, validation,
storage, priority indicators and risk scoring. Verify that the dashboard
can show findings and source URLs and record defects before expanding
the run to the remaining sample.

## 65. Run the PoC analysis for all 10 companies

Goal: Produce the agreed prototype analysis for the approved 10-company
sample. Description: Run the validated workflow for all 10 companies,
subject to the approved data-quality gate and replacement process.
Record coverage, missing periods, extraction failures, findings and
score outputs for each company.

## 66. Validate findings against public historical cases

Goal: Compare the PoC's detected red flags with publicly documented
historical cases and disclosures. Description: Create an evaluation set
of known public red flags with company, period, indicator, evidence URL
and evidence cut-off date. Compare system findings against this set and
report detection coverage, including cases that could not be evaluated
because data was unavailable.

## 67. Establish false-positive baseline

Goal: Measure and document the initial level of findings that are not
supported by the evaluation evidence. Description: Review findings from
the 10-company sample against the documented public evidence and record
unsupported or irrelevant findings using the available classifications.
Report a baseline rather than assuming a numerical false-positive target
that has not been agreed.

## 68. Evaluate the provisional 80% known-red-flag target

Goal: Determine whether the PoC detects at least 80% of the agreed known
red flags in the evaluation dataset. Description: Calculate detection
coverage using the documented evaluation denominator and evidence rules.
Explain dataset limitations, unavailable periods and the distinction
between detecting a public red flag and proving fraud.

## 69. Evaluate explainability and analyst productivity

Goal: Assess whether the prototype helps analysts understand and review
potential red flags. Description: Evaluate the clarity of explanations,
confidence labels, source traceability and natural-language answers
using representative company-analysis scenarios. Document the method and
observations for analyst productivity without claiming a quantified
improvement unless it is measured.

## 70. Prepare the PoC evaluation report

Goal: Deliver a concise evidence-based assessment of prototype
performance and limitations. Description: Report the evaluation dataset
and method, detection results, accuracy observations, false-positive
baseline, explainability, analyst productivity, data-quality constraints
and technical limitations. Include prioritised recommendations for a
subsequent phase without committing that phase to the current
engagement.

## 71. Estimate AWS and AI service costs

Goal: Estimate the cost of operating the 10-company PoC in the
TEKMentors AWS account. Description: Estimate infrastructure and usage
costs for Bedrock, Textract, SageMaker where used, RDS PostgreSQL, S3,
networking and supporting services. State assumptions for report/page
volumes, extraction frequency, model calls, storage, query volume,
compute sizing and AWS region.

## 72. Prepare indicative scale cost projections

Goal: Show how AWS and AI costs may change at 500 companies and the
wider NSE/BSE-listed universe. Description: Extend the PoC cost
assumptions into indicative 500-company and all-listed-company
scenarios, identifying volume, frequency, storage and compute
assumptions. Clearly label the figures as projections rather than a
commitment to build or operate at those scales.

## 73. Prepare the basic user guide

Goal: Help an analyst navigate the PoC and interpret its outputs.
Description: Document sign-in, dashboard navigation, company analysis,
risk scores, category scores, confidence labels, evidence links,
natural-language Q&A, feedback and Excel export. Explain that the tool
identifies potential red flags and does not make legal fraud
determinations.

## 74. Prepare the PoC architecture and deployment notes

Goal: Document how the PoC is deployed and configured in the AWS
environment. Description: Record the selected AWS services, application
components, data flows, environment configuration, access controls and
deployment assumptions. Include operational limitations and the steps
required to reproduce the PoC deployment without exposing secrets.

## 75. Review deferred features and scope completion

Goal: Confirm which agreed capabilities were delivered in the 8-week PoC
and which were deferred. Description: Compare completed work against the
approved priority order, documenting acceptance evidence, known defects,
unavailable public data and deferred lower-priority market-activity
features. Do not expand the current engagement into implementation of a
later phase.

## 76. Confirm source-code and licensing terms

Goal: Record the commercial agreement governing PoC source code and
licensing. Description: Prepare the source-code ownership and licensing
points for commercial negotiation and obtain the required agreement
before contract execution or delivery. Do not assume that ownership or
licensing rights have been granted by the technical scope alone.

------------------------------------------------------------------------

## Deferred / conditional market-activity backlog

The following tasks are independently described but are **not core PoC
commitments**. They may be selected only if the core financial and
governance priorities are complete, time remains within the 8-week
window, and suitable free public data is available and permitted.

## 77. Extract historical share-price movements

Goal: Highlight unusual share-price movements around quarterly and
annual financial-result announcements. Description: Obtain permitted
free public historical price data for the approved companies and align
price movements with financial-result announcement dates. Flag unusual
movements using an agreed definition; do not correlate them with news or
other financial red flags.

## 78. Extract unusual trading-volume spikes

Goal: Flag unusual trading-volume spikes around financial-result
announcements. Description: Obtain permitted free public trading-volume
data and identify spikes around the relevant result announcement dates
using an agreed baseline. Present the underlying volume, comparison
period and source reference without correlating the spike with other
financial red flags.

## 79. Extract and flag short-selling activity

Goal: Identify unusual increases in publicly available short-selling
activity. Description: Identify a permitted free public source for
short-selling data and extract the available company/time-period
information. Flag unusual increases using an agreed definition; if
adequate public data is unavailable, record the limitation and do not
substitute a paid feed.

## 80. Extract insider-trading disclosures

Goal: Identify unusual disclosed insider-trading patterns around
financial-result announcements. Description: Extract publicly disclosed
insider trades by promoters and directors and align their dates with
quarterly and annual result announcements. Flag unusual patterns using
agreed criteria without correlating trades with subsequent share-price
movements.

## 81. Extract bulk and block deals

Goal: Highlight unusually large or repeated publicly disclosed bulk and
block deals. Description: Obtain permitted free public bulk/block deal
disclosures for the approved companies and extract transaction date,
quantity and disclosed values where available. Flag unusually large
transactions and repeated activity without analysing buyer/seller
relationships.

## 82. Extract credit-rating changes

Goal: Highlight credit-rating downgrades and repeated rating changes
over five years. Description: Extract publicly available rating actions
and changes for the approved companies, including dates and rating
levels. Flag downgrades and repeated changes; do not analyse
rating-agency explanations, and defer the feature if suitable free
public data is unavailable.
