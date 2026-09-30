# Daniela Hotz

**Data Analyst | Economist | Healthcare Analytics & Business Intelligence**  
Montréal, Québec, Canada

I connect healthcare data, statistical analysis and business context to support strategic decisions. My experience includes more than six years in strategic information and healthcare analytics, progressing from assistant to senior analyst.

My work focuses on healthcare expenditure, population patterns, forecasting and analytical methodology. I translate complex business questions into structured analyses and findings for management and executive audiences.

**[Explore my portfolio →](https://dhotz8.github.io/)**

## Areas of expertise

- **Healthcare cost analytics:** expenditure trends, claims ratios, utilization patterns and cost drivers.
- **Statistical modeling and forecasting:** membership forecasting with SARIMAX, intervention modeling, financial model comparison using ARIMA, SARIMA, ETS and Prophet, temporal validation and residual diagnostics.
- **Clinical text processing:** normalization of unstructured descriptions, reference dictionaries, ICD-10 mapping and rule-based classification of chronic conditions.
- **Analytics methodology and governance:** indicator definitions, eligibility rules, classification dictionaries, reconciliation, traceability and documentation of analytical limitations.
- **Business intelligence and decision support:** data exploration, KPI monitoring and communication of analytical findings using Qlik, Python and Excel.

## Selected projects

### [Healthcare Cost Drivers](https://dhotz8.github.io/cases/healthcare-cost-drivers.html)

**Objective:** investigate healthcare expenditure growth in the context of membership, cost per member and other drivers.  
**My contribution:** structured comparative analyses across time and population dimensions and translated findings into management-oriented reporting.  
**Analytical finding:** the selected historical periods show nominal expenditure growing substantially faster than membership, motivating further investigation of prices, utilization and case mix.

### [Chronic Population Analytics](https://dhotz8.github.io/cases/chronic-population.html)

**Objective:** turn inconsistent clinical descriptions into structured categories for population analysis.  
**My contribution:** developed Python processing with text normalization, regular expressions and reference dictionaries, supporting disease-category mapping and analytical reporting.  
**Analytical finding:** the study identified the largest mapped condition categories and reported concentration of healthcare costs in the chronic population. Categories may overlap; observation windows are documented in the case.

### [Healthcare Forecasting](https://dhotz8.github.io/cases/healthcare-forecasting.html)

**Objective:** support membership and financial planning through forecasts and scenarios.  
**My contribution:** developed membership forecasting and scenario scripts, compared financial forecasting models and implemented temporal evaluation and statistical diagnostics.  
**Analytical output:** forecasts, planning scenarios and estimated revenue-loss comparisons. The displayed financial estimates come from the original 2025 study; the updated 2026 SARIMAX intervention approach is described separately. Estimates are not realized losses or evidence of forecast accuracy.

## Tools

**Python:** pandas, NumPy, statsmodels, SciPy, scikit-learn, Prophet, Matplotlib and regular expressions.  
**Analytics & BI:** Qlik, SQL and Excel.  
**Methods:** time-series analysis, segmentation, model comparison, hypothesis testing and methodological documentation.

## Education

- **AEC in International Business Management** — Greystone College, Montréal · in progress
- **MBA in Data Science & Big Data** — PUC Minas
- **MBA in Project Management** — USP/ESALQ
- **Bachelor’s degree in Economics** — UNIOESTE · first in class

## Contact

[LinkedIn](https://www.linkedin.com/in/danielahotz/) · [GitHub](https://github.com/DHOTZ8/)  
Email: [danielahotz08@gmail.com](mailto:danielahotz08@gmail.com)

---

## About this repository

This repository hosts my responsive portfolio through GitHub Pages. It uses HTML, CSS and SVG, with no build step or external font dependency.

Case charts reconstruct selected aggregate values from the original studies with organization names anonymized. No original internal PDFs or individual patient records are published. Sources, periods and interpretation notes are documented in each case and in [data/README.md](data/README.md). The homepage hero is illustrative.

The two Python examples in [code/](code/) are separate demonstrations using synthetic data. They do not replace the original internal project scripts, which have not been published in this repository.

For a local preview, open `index.html` or run `python -m http.server 8000` in the repository folder.

- `index.html`: homepage
- `cases/`: case studies
- `assets/`: styling and figures
- `data/`: transcribed aggregate data and provenance
- `code/`: synthetic-data demonstrations
