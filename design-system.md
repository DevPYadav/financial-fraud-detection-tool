# Design System

The UI is a Streamlit app for analysts reviewing potential financial and governance red flags. Keep it simple, consistent and evidence-first.

## Principles

- **Evidence first:** every score or finding links to its supporting evidence and source URL.
- **Explainable:** show why something was flagged and how it affects the score.
- **Not a verdict:** the tool shows potential red flags, not fraud determinations. Show this disclaimer on the dashboard and in Q&A answers.
- **Per company:** companies are analysed independently. No cross-company rankings or peer comparisons.

## Components

- Use built-in Streamlit components and the default theme. Do not add UI libraries or custom CSS without asking.
- Pages: Dashboard, Company Analysis, Analyst Q&A. Navigate from the sidebar.
- Use `st.dataframe` for tables, Streamlit charts for trends and `st.download_button` for the Excel export.

## Risk categories

| Score  | Category | Colour |
| ------ | -------- | ------ |
| 0-30   | Low      | Green  |
| 31-60  | Medium   | Amber  |
| 61-80  | High     | Orange |
| 81-100 | Critical | Red    |

Always show the score and the category name together. Never rely on colour alone.

## Findings

Show each finding in this order:

1. Indicator triggered
2. Why it was triggered
3. Impact on the company/category score
4. Confidence: High, Medium or Low (as text)
5. Source URL (opens in a new tab)
6. Feedback buttons: Relevant, Not Relevant, Needs Further Review

## Information types

Label content consistently so analysts can tell them apart:

- **Extracted fact** - a value taken from a source document
- **Detected anomaly** - a rule or model result
- **AI interpretation** - generated text that needs human validation

## Formatting

- Currency: Indian rupees, shown with the unit (for example `₹ 1,234.5 crore`).
- Periods: Indian financial year labels (for example `Q2 FY2025`, `FY2024`), with standalone or consolidated stated.
- Dates: `DD MMM YYYY` (for example `09 Nov 2026`).
- Show missing data as "Not available" with the reason when known. Never show it as zero.

## Out of scope

No alerts or notifications, no rule-builder UI and no per-user roles (one common role).
