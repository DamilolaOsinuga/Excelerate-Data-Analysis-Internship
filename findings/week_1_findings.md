# Week 1 Findings — Excelerate Applicant Data Analysis

**Programme:** Excelerate AI & Data Analytics Internship (Supported by Rochester Institute of Technology)  
**Week Focus:** Data cleaning, quality assessment, and initial exploratory analysis  
**Analyst:** Damilola Osinuga — Team 4

---

## Dataset Overview

| Attribute | Detail |
|-----------|--------|
| Source | Excelerate — global internship & programme platform |
| Total records | **8,558 applications** |
| Columns | First_Name, Opportunity_Category, Apply_Date, Age_Group, Country, Status |
| Date range | 2022 – 2024 |
| Format | Microsoft Excel (.xlsx) |

---

## 1. Data Quality Assessment

### Issues Identified
- **Missing values:** Reviewed all 6 columns for null or blank entries
- **Date formatting:** Apply_Date column had inconsistent date formats across entries — standardised to YYYY-MM-DD
- **Duplicate check:** Scanned for duplicate application records by name + date + program combination
- **Status values:** Confirmed valid categories — Accepted, Rejected, Pending, Under Review
- **Age group values:** Confirmed valid brackets — 16-20, 21-29, 30-35, 36-59

### Data Quality Summary
| Column | Issue Found | Resolution |
|--------|------------|------------|
| Apply_Date | Mixed date formats | Standardised to YYYY-MM-DD |
| Opportunity_Category | Inconsistent spacing | Trimmed whitespace |
| Country | Variant spellings | Standardised country names |
| Status | No issues | — |
| Age_Group | No issues | — |
| First_Name | No issues | — |

---

## 2. Initial Exploration — Key Observations

### Application Volume
- **Total applications analysed:** 8,558
- Dataset spans 3 years (2022–2024), showing clear growth trajectory
- 2024 data suggests continued year-on-year growth

### Geographic Distribution (Initial)
- Applications received from multiple countries
- Nigeria accounts for a significant share of applicants — consistent with Excelerate's African market presence
- Significant international diversity in applicant pool

### Age Group Distribution (Initial)
- **21-29** age group dominates — consistent with target demographic for internship programmes
- 16-20 group represents a meaningful secondary segment (pre-university / undergraduate)
- 30-35 and 36-59 segments present — indicates broader professional interest in upskilling

### Opportunity Category Spread
- Multiple programme types attracting applications
- Data Analytics, Business, and Technology programmes among top categories
- Clear concentration in a subset of high-demand programme categories

---

## 3. Tools & Techniques Used

- **Microsoft Excel** — data inspection, cleaning, formula-based transformations
- **COUNTIF / COUNTBLANK** — null value detection
- **TEXT functions** — date standardisation
- **Pivot Tables** — initial category and country distributions
- **Conditional Formatting** — outlier and anomaly flagging

---

## 4. Outputs from Week 1

| Deliverable | Description |
|------------|-------------|
| `analysis/week_1_2_analysis.xlsx` | Cleaned dataset + initial pivot tables |
| `findings/data/data_dictionary.md` | Column definitions and valid value reference |

---

## 5. What Week 2 Will Explore

Building on the cleaned dataset, Week 2 will go deeper into:
- Temporal trends (year-over-year and quarterly seasonality)
- Program-level application breakdown
- Demographic and geographic pattern analysis
- Status conversion rates (Accepted vs Rejected vs Pending)
