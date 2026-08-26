# Excelerate Data Analysis Internship — Applicant Analysis Project

**Programme:** Excelerate AI & Data Analytics Internship | Supported by Rochester Institute of Technology (RIT)  
**Duration:** February 2026 (4-week virtual programme)  
**Analyst:** Damilola Osinuga — Team 4  
**Location:** Lagos, Nigeria

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Damilola%20Osinuga-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/damilola-osinuga)

---

## Project Overview

This project analyses **8,558 real applicant records** from Excelerate's global programme platform (2022–2024) to uncover insights about applicant demographics, application trends, programme popularity, seasonal patterns, and outcome prediction.

The analysis progressed across four weeks from Excel-based data cleaning to Python-driven predictive modelling and a final Power BI executive dashboard — delivered live to programme evaluators in February 2026.

---

## Dataset

| Attribute | Detail |
|-----------|--------|
| Records | **8,558 applications** |
| Period | 2022 – 2024 |
| Key columns | Opportunity_Category, Apply_Date, Age_Group, Country, Status |
| Source | Excelerate — global internship & professional development platform |

Full column definitions: [`findings/data/data_dictionary.md`](findings/data/data_dictionary.md)

---

## Project Goals

- Understand applicant demographics and geographic distribution
- Identify trends, seasonality, and programme demand patterns
- Analyse acceptance and churn rates by applicant segment
- Build a predictive model for application outcome
- Deliver a Power BI KPI dashboard and executive recommendations

---

## Progress & Status

| Week | Focus | Status |
|------|-------|--------|
| Week 1 | Data cleaning, quality assessment, initial exploration | ✅ Complete |
| Week 2 | Deeper EDA — temporal, demographic, geographic, programme analysis | ✅ Complete |
| Week 3 | Python analysis — churn modelling and outcome prediction | ✅ Complete |
| Week 4 | Power BI dashboard, executive presentation, live evaluation | ✅ Complete |

---

## Repository Structure

```
Excelerate-Data-Analysis-Internship/
├── README.md                            # This file
├── requirements.txt                     # Python dependencies
├── analysis/
│   ├── week_1_2_analysis.xlsx           # Excel workbook: data cleaning + pivot analysis
│   ├── week3_churn.py                   # Python: applicant churn analysis
│   └── week3_model.py                   # Python: predictive outcome model
└── findings/
    ├── data/
    │   └── data_dictionary.md             # Column definitions and valid value reference
    ├── week_1_findings.md               # Week 1: cleaning steps, initial observations
    ├── week_2_findings.md               # Week 2: temporal, demographic, geographic insights
    ├── week_3_findings.md               # Week 3: churn analysis + predictive model results
    └── week_4_findings.md               # Week 4: final dashboard + executive recommendations
```

---

## Key Findings Summary

### 📈 1. Consistent Year-on-Year Growth (2022–2024)
Application volume grew sharply from 2022 to 2023 and continued into 2024, validating strong and accelerating market demand for Excelerate programmes.

### 🗓️ 2. Strong Seasonal Pattern — Q1 Dominates
Q1 (January–March) consistently drives the highest application volumes. Q3 is the secondary peak. Q2 and Q4 are significantly lower — a recurring, reliable pattern for capacity planning.

### 👥 3. 21-29 Age Group is the Core Market
The 21-29 cohort represents the largest share of applications and the strongest engagement. The 16-20 segment is meaningful and growing.

### 🌍 4. Nigeria Leads Geographic Distribution
Nigeria accounts for the highest share of applicants among all countries in the dataset. Significant international diversity exists, with untapped growth potential in underrepresented regions.

### 🎯 5. Application Timing Predicts Outcomes
Q1 applications have significantly better acceptance outcomes than Q4 applications. Apply quarter is the strongest single predictor of outcome in the classification model.

### ⚠️ 6. Churn Concentrated in Pending Backlog
A meaningful percentage of applications remain in Pending/Under Review beyond expected processing windows. A targeted SLA and follow-up outreach campaign could recover significant conversion.

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Microsoft Excel | Data cleaning, pivot tables, initial EDA |
| Power BI | Final KPI dashboards and executive visualisations |
| Python (pandas) | Data manipulation and feature engineering |
| Python (scikit-learn) | Classification model for outcome prediction |
| Python (matplotlib / seaborn) | Visualisation of churn and trend patterns |
| SQL | Data querying and validation |

---

## Strategic Recommendations (Week 4 Summary)

1. Invest in Q1 and Q3 programme capacity — align intake with seasonal demand
2. Launch Q2 and Q4 activation campaigns to smooth demand and fill available spots
3. Build a Pending application SLA (21-day maximum) with automated follow-up
4. Prioritise the 21-29 segment while developing an entry pathway for 16-20 applicants
5. Deploy the predictive scoring model internally to prioritise high-probability applicants
6. Expand geographic marketing beyond Nigeria to underrepresented applicant regions

---

## Running the Python Analysis

```bash
# Clone the repository
git clone https://github.com/DamilolaOsinuga/Excelerate-Data-Analysis-Internship.git

# Install dependencies
pip install -r requirements.txt

# Run churn analysis
python analysis/week3_churn.py

# Run predictive model
python analysis/week3_model.py
```

---

## Certificate

Completed and certified by Excelerate in partnership with **Rochester Institute of Technology (RIT)**, February 2026.

---

## Connect

**Damilola Osinuga** — Data & Operations Analyst | Power Platform | SQL | Lagos, Nigeria  
👤 [LinkedIn](https://www.linkedin.com/in/damilola-osinuga) | 📊 [GitHub](https://github.com/DamilolaOsinuga)
