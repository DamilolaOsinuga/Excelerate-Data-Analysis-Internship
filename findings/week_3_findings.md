# Week 3 Findings — Advanced Analysis & Predictive Modelling

**Programme:** Excelerate AI & Data Analytics Internship (Supported by Rochester Institute of Technology)  
**Week Focus:** Advanced pattern analysis, applicant churn modelling, and predictive insights using Python  
**Analyst:** Damilola Osinuga — Team 4

---

## Overview

Week 3 moved from descriptive Excel analysis into Python-driven deeper analysis. Two core analytical workstreams were executed:
1. **Churn analysis** — identifying applicant drop-off patterns and incomplete application behaviours
2. **Predictive modelling** — building a model to forecast application outcomes based on applicant characteristics

---

## 1. Applicant Churn Analysis (`week3_churn.py`)

### Definition
For this project, "churn" refers to applicants who initiated but did not complete the application process, or whose applications remained in Pending / Under Review status beyond expected processing windows.

### Key Findings

| Metric | Finding |
|--------|--------|
| Overall churn rate | Applications with non-final status (Pending/Under Review) |
| Highest churn segment | Identified by age group and opportunity category |
| Lowest churn segment | Segments with highest Accepted rate |
| Seasonal churn pattern | Churn varies by application quarter — aligned with Week 2 seasonality findings |

### Churn by Age Group
- The **21-29** cohort showed the highest absolute volume but not the highest churn rate percentage
- Younger applicants (16-20) showed higher rates of incomplete applications — likely due to eligibility mismatches
- The 30-35 segment showed the strongest completion-to-acceptance ratio

### Churn by Programme Category
- Programmes with longer selection processes had higher in-process (Pending) rates
- High-demand programmes showed faster resolution times (accepted or rejected sooner)
- Niche or newer programmes had disproportionate Pending backlogs

---

## 2. Predictive Model (`week3_model.py`)

### Objective
Build a model to predict application outcome (Accepted / Rejected) based on available applicant features.

### Features Used
| Feature | Type | Rationale |
|---------|------|----------|
| Age_Group | Categorical | Demographic predictor |
| Opportunity_Category | Categorical | Programme-specific acceptance rates differ |
| Apply_Date (quarter) | Derived | Seasonal effect established in Week 2 |
| Country | Categorical | Geographic pattern identified in Week 2 |

### Model Approach
- **Algorithm:** Classification model (Logistic Regression / Decision Tree)
- **Target variable:** Application Status (binary: Accepted vs Not Accepted)
- **Train/test split:** 80/20
- **Evaluation:** Accuracy, precision, recall on test set

### Results
- Model performance metrics recorded in `analysis/week3_model.py`
- Key predictors identified: Opportunity_Category and Apply Quarter emerged as strongest signals
- Geographic features added marginal predictive value beyond category and timing

---

## 3. Strategic Insights from Week 3

1. **Application timing is the strongest predictor** — Q1 applications have significantly better acceptance outcomes than Q4 applications
2. **Programme category drives acceptance rates** — not all programmes accept at the same rate; some are significantly more selective
3. **Age group 21-29 is the core market** — highest volume AND competitive acceptance rates
4. **Churn intervention opportunity** — a targeted follow-up campaign for Pending applications older than 30 days could recover meaningful conversion
5. **Predictive model use case** — a simple scoring tool could help Excelerate prioritise outreach to high-probability applicants

---

## 4. Tools & Techniques Used

- **Python (pandas)** — data manipulation and feature engineering
- **Python (scikit-learn)** — classification modelling and evaluation
- **Python (matplotlib / seaborn)** — visualisation of churn patterns
- **Excel** — cross-validation of findings against pivot table outputs

---

## 5. Files from Week 3

| File | Description |
|------|-------------|
| `analysis/week3_churn.py` | Churn analysis script — drop-off patterns by segment |
| `analysis/week3_model.py` | Predictive model — applicant outcome classification |

---

## 6. What Week 4 Will Deliver

- Final Power BI dashboard consolidating all four weeks of findings
- Executive presentation with strategic recommendations for Excelerate
- Live evaluation presentation to programme assessors
