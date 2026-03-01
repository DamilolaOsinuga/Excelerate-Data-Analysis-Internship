# Excelerate Data Analysis Internship - Application Analysis Project

## Project Overview

This is my real-world data analysis project from a **4-week global data analytics internship** with Excelerate. The project involves analyzing **applicant data** for various programs offered by Excelerate to uncover insights about applicant demographics, application trends, program popularity, and applicant characteristics.

---

## 📊 Project Goals

- Understand applicant demographics and characteristics
- Identify trends in program applications over time
- Analyze application seasonality and patterns
- Explore geographic distribution of applicants
- Provide insights to support decision-making and strategy
- Practice data cleaning, exploration, and analysis with Excel

---

## 📅 Timeline & Progress

- **Week 1-2:** Data cleaning, exploration, and initial analysis ✅ **COMPLETE**
  - Data quality assessment and cleaning
  - Exploratory analysis with pivot tables and formulas
  - Key findings on applications, demographics, and trends
  
- **Week 3:** Deeper analysis and advanced insights ✅ **COMPLETE**
  - Advanced trend analysis
  - Comparative analysis across programs and demographics
  - Forecasting and predictive insights
  
- **Week 4:** Python implementation, visualizations, and final report 📋 **PLANNED**
  - Advanced Python analysis and automation
  - Interactive data visualizations
  - Executive summary and strategic recommendations

---

## 🛠️ Tools & Technologies Used

- **Excel** - Data cleaning, formulas (COUNTIF, SUMIF, AVERAGEIF, VLOOKUP), pivot tables, analysis
- **Python** (coming in Week 3-4) - Advanced analysis, forecasting, and visualization
- **Pivot Tables** - Data aggregation and summarization
- **Excel Formulas** - Data transformation and calculations

---

## 📁 Project Structure

```
Excelerate-Data-Analysis-Internship/
├── README.md                          # This file
├── data/
│   ├── raw_data/
│   │   └── applicant_data.xlsx        # Original dataset
│   ├── cleaned_data/
│   │   └── cleaned_applicant_data.xlsx # Cleaned version
│   └── data_dictionary.md              # Explanation of all columns
├── analysis/
│   ├── week_1_2_analysis.xlsx         # Week 1-2 pivot tables & analysis
│   ├── week_3_analysis.xlsx           # Week 3 analysis (TBD)
│   └── week_4_analysis.xlsx           # Week 4 analysis (TBD)
├── findings/
│   ├── week_1_findings.md             # Week 1 key findings
│   ├── week_2_findings.md             # Week 2 key findings
│   ├── week_3_findings.md             # Week 3 findings (TBD)
│   └── week_4_findings.md             # Week 4 final report (TBD)
├── visualizations/
│   ├── charts/                        # Charts and graphs (PNG/JPG)
│   └── pivot_tables/                  # Screenshots of pivot tables
└── documentation/
    └── analysis_methodology.md        # How we approached the analysis
```

---

## 📋 Key Findings (Week 1-2)

### Data Overview
- **Total Applications:** 8,558
- **Number of Programs/Opportunities:** Multiple (Internships, Courses, Events, Competitions, Engagement)
- **Geographic Reach:** Global (USA, India, Nigeria, and others)
- **Date Range:** 2022-2024
- **Data Quality:** Cleaned and validated

---

## 📈 Major Insights from Week 2 Analysis

### 1. Application Growth Over Time (2022–2024)
**Key Finding:** Applications show a **strong upward trend**, rising sharply from 2022 to 2023 and continuing to increase in 2024.

**Implications:**
- Rapid platform growth and increasing interest in Excelerate opportunities
- Application demand is likely to remain high in the future
- The low volume in 2022 likely reflects early-stage platform activity or partial-year data
- Greater emphasis should be placed on recent years (2023-2024) when analyzing trends

**Strategic Value:** Application year is an important time-based predictor for forecasting and strategic planning.

---

### 2. Application Seasonality Pattern (Quarterly Analysis)
**Key Finding:** Clear seasonality across quarters with distinct patterns:
- **Q1 (Jan-Mar):** HIGHEST volume - Peak period
- **Q3 (Jul-Sep):** SECOND HIGHEST - Secondary peak
- **Q2 (Apr-Jun):** Lower volume
- **Q4 (Oct-Dec):** Lowest volume

**Implications:**
- Applicant interest peaks at the beginning of the year and mid-year
- Likely aligns with academic calendars and program intake cycles
- Significant imbalance between Q1 and other quarters presents optimization opportunity
- Patterns are recurring and predictable

**Strategic Opportunity:** Targeted outreach and marketing efforts during slower periods (Q2 and Q4) could help stabilize application flow throughout the year.

**Forecasting Value:** Apply Quarter demonstrates strong predictive potential for demand forecasting.

---

### 3. Opportunity Category Distribution
**Key Finding:** Applications are heavily concentrated in specific program types:
- **Internships:** Dominant category (majority of applications)
- **Courses:** Second largest category
- **Events:** Much smaller volume
- **Competitions:** Much smaller volume
- **Engagement Opportunities:** Smallest volume

**Implications:**
- Users primarily associate Excelerate with internship opportunities
- Internships are the major driver of overall application demand
- Heavy imbalance across categories creates risk (over-reliance on one program type)
- Underrepresented categories have untapped potential

**Strategic Opportunity:** Increase awareness and visibility of underrepresented categories (Events, Competitions, Engagement) to diversify user interest and reduce reliance on internships alone.

**Forecasting Value:** Opportunity Category has strong predictive potential for overall application volume.

---

### 4. Age Group Distribution
**Key Finding:** Age distribution is heavily concentrated in one segment:
- **21–29 age group:** Vast majority of applicants (PRIMARY DEMOGRAPHIC)
- **16–20 age group:** Smaller proportion
- **30–35 age group:** Much smaller proportion
- **36–59 age group:** Very small proportion

**Implications:**
- Excelerate primarily attracts early-career individuals (current students and recent graduates)
- This aligns well with the platform's internship-focused offerings
- Limited diversity in age demographics
- Strong skew toward a single age segment

**Strategic Opportunity:** Explore targeted outreach strategies for older or non-traditional learners (30+) if diversification of the applicant base becomes a business goal.

**Forecasting Value:** Age Group shows meaningful predictive potential—shifts in this core demographic could directly influence overall application volume.

---

### 5. Geographic Concentration & Distribution
**Key Finding:** Strong geographic concentration with global reach but uneven distribution:
- **United States:** Largest applicant base (majority)
- **India:** Second largest (significant volume)
- **Nigeria:** Notable presence but smaller than US/India
- **Other countries:** Long tail of applications (relatively low volumes)

**Implications:**
- Excelerate currently has strong traction in a few key geographies
- Significant concentration risk (reliance on 2 main countries)
- Engagement in other regions remains relatively limited
- Global expansion opportunity exists

**Strategic Opportunity:** Expand visibility and marketing in underrepresented countries to support more balanced global growth and reduce geographic concentration risk.

**Forecasting Value:** Country demonstrates solid predictive potential—changes in outreach, partnerships, or marketing efforts within high-volume countries will significantly impact application numbers.

---

## 🔍 Analysis Methods

### Data Cleaning
- Removed duplicates and errors
- Handled missing values
- Standardized formatting (dates, text, categories)
- Validated data accuracy
- Flagged and resolved inconsistencies

### Exploratory Data Analysis (EDA)
- Descriptive statistics across all dimensions
- Pivot tables for aggregation by:
  - Application year/quarter
  - Opportunity category
  - Age group
  - Country/geographic location
- Excel formulas for calculations (COUNTIF, SUMIF, AVERAGEIF)
- Trend identification and pattern recognition

### Key Pivot Tables Created
- Applications by Year (2022, 2023, 2024)
- Applications by Quarter (Q1, Q2, Q3, Q4)
- Applications by Opportunity Category
- Applications by Age Group
- Applications by Country/Geography
- Cross-tabulations (e.g., Category × Year, Age × Year)

### Excel Formulas Used
- `COUNTIF()` - Count applications by category
- `SUMIF()` - Sum applications by condition
- `AVERAGEIF()` - Average metrics by group
- `VLOOKUP()` / `INDEX-MATCH()` - Data lookup and matching
- `IF()` statements - Conditional calculations
- Year/Quarter extraction formulas

---

## 📊 Visualizations (Week 2)

The following visualizations have been created to illustrate key findings:
- 📈 **Application Growth Over Time** - Line chart showing 2022-2024 trend
- 📊 **Quarterly Seasonality Pattern** - Bar chart showing Q1-Q4 distribution
- 🎯 **Opportunity Category Distribution** - Pie/Bar chart showing program breakdown
- 👥 **Age Group Distribution** - Bar chart showing demographic concentration
- 🌍 **Geographic Distribution** - Bar chart showing country-level volume

---

## 🎯 Key Insights & Strategic Recommendations

### Insight 1: Strong Growth Trajectory
The platform is experiencing robust growth with applications increasing year-over-year. This validates the market demand for Excelerate's offerings.

**Recommendation:** Maintain and accelerate investment in infrastructure to support continued growth.

---

### Insight 2: Predictable Seasonality
Quarterly patterns are consistent and predictable, indicating that seasonal planning can be optimized.

**Recommendation:** Plan marketing campaigns to boost applications in Q2 and Q4 to balance the quarterly distribution and maximize annual volume.

---

### Insight 3: Internship Dominance
Internships drive the vast majority of applications, but other program types show potential.

**Recommendation:** While maintaining internship leadership, develop strategic initiatives to grow Courses, Events, and Competitions to diversify revenue and user value.

---

### Insight 4: Concentrated Demographics
The 21-29 age group represents the core user base, with limited diversity.

**Recommendation:** Create targeted outreach programs for underrepresented age groups (16-20 and 30+) to broaden the addressable market.

---

### Insight 5: Geographic Concentration Risk
US and India represent a significant portion of applications, creating geographic concentration risk.

**Recommendation:** Develop localized marketing strategies and partnerships in emerging regions (Africa, Southeast Asia, Latin America) to diversify the geographic base and tap new markets.

---

## 📈 What I Learned (Week 1-2)

- Data cleaning and validation is crucial—quality input determines output quality
- Pivot tables are incredibly powerful for rapid insights and pattern recognition
- Seasonality and trend analysis provide actionable business insights
- Clear visualization of data helps communicate findings to stakeholders
- Asking strategic questions (Why Q1? Why US/India?) leads to better insights
- Documentation of methodology is essential for reproducibility and stakeholder trust

---

## 🤖 Week 3 — Predictive Modeling Results

### Models Built
| Script | Model | Purpose |
|--------|-------|---------|
| `analysis/week3_forecast.py` | Linear Regression (Trend + Seasonality) | Forecast monthly application volume |
| `analysis/week3_churn.py` | Logistic Regression (Balanced) | Predict participant dropout/churn |

### Key Results
- **Best Forecast Model:** Linear Regression with Trend + Seasonality — R² = 0.431
- **6-Month Forecast (Jan–Jun 2025):** 1,037 → 801 → 455 → 426 → 486 → 540 applications
- **Churn Model Accuracy:** 74.7% | Churn Recall: **95%**
- **Top churn driver:** Internship opportunity category (coefficient +3.20)
- **Dataset:** 34 monthly points for forecasting | 4,730 accepted applicants for churn model

### How to Run
```bash
pip install -r requirements.txt
python analysis/week3_forecast.py
python analysis/week3_churn.py
```

### Python Version
Python 3.10+

---


## 🔄 Next Steps (Week 4)

- [ ] Deep-dive analysis on underperforming categories and demographics
- [ ] Build predictive models for application forecasting (Python)
- [ ] Create interactive visualizations and dashboards
- [ ] Analyze conversion rates and applicant progression
- [ ] Develop strategic recommendations with financial impact estimates
- [ ] Prepare executive summary and final presentation
- [ ] Implement Python automation for ongoing analysis

---

## 📂 Files & Data Structure

| File/Folder | Purpose | Status |
|-------------|---------|--------|
| `applicant_data.xlsx` | Original dataset | ✅ Complete |
| `cleaned_applicant_data.xlsx` | Cleaned dataset | ✅ Complete |
| `week_1_2_analysis.xlsx` | Pivot tables and formulas | ✅ Complete |
| `findings/` | Detailed findings documentation | ✅ Complete |
| `visualizations/` | Charts and graphs | ✅ Complete |
| `week_3_analysis.xlsx` | Advanced analysis | 🔄 In Progress |
| `week_4_analysis.xlsx` | Final analysis and models | 📋 Planned |

---

## 📝 Key Metrics & Statistics

**Application Volume:**
- 2022: Low (early-stage)
- 2023: Strong growth
- 2024: Continued increase

**Quarterly Breakdown:**
- Q1: Highest volume (seasonal peak)
- Q2: Lower volume
- Q3: Secondary peak
- Q4: Lowest volume

**Program Distribution:**
- Internships: Dominant (majority)
- Courses: Secondary
- Events: Minimal
- Competitions: Minimal
- Engagement: Minimal

**Age Demographics:**
- 21-29: 70%+ of applications (primary demographic)
- Other ages: Remaining applicants

**Geographic:**
- United States: Largest market
- India: Second largest market
- Nigeria: Notable presence
- Other: Distributed globally

---

## 🛠️ How to Use This Analysis

1. **Review the findings** documented in `/findings/week_1_findings.md` and `/findings/week_2_findings.md`
2. **Examine the raw data** in `/data/raw_data/applicant_data.xlsx`
3. **Study the analysis** in `/analysis/week_1_2_analysis.xlsx` (pivot tables and formulas)
4. **Review visualizations** in `/visualizations/` folder
5. **Understand the methodology** in `/documentation/analysis_methodology.md`

---

## 📬 Questions or Feedback?

Feel free to reach out if you have questions about this analysis or want to discuss the findings:

- **LinkedIn:** https://www.linkedin.com/in/damilola-osinuga
- **Email:** osinugadamilola4@gmail.com

---

## 📅 Project Timeline

| Week | Focus | Status |
|------|-------|--------|
| Week 1-2 | Data exploration & initial analysis | ✅ COMPLETE |
| Week 3 | Advanced analysis & forecasting | 🔄 IN PROGRESS |
| Week 4 | Python, visualizations, final report | 📋 PLANNED |

---

*This project is part of the Excelerate Global Data Analytics Internship Program*

**Last Updated:** Week 2 - [Current Date: February 2026]
