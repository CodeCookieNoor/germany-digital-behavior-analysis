# Digital Engagement & E-commerce Behavior in Germany (2020–2025)

## Project Overview

This project analyzes the relationship between digital engagement and online shopping behavior among German consumers using Eurostat data.

The study investigates how social media participation and e-commerce purchasing patterns vary across demographic groups and evolve over time.

Focus areas:

- Social media usage
- Online purchasing behavior
- Age segmentation
- Gender segmentation
- Education segmentation
- Germany (2020–2025)

---

## Research Question

**How does social media engagement relate to online shopping behavior among German consumers across demographic groups?**

### Sub-questions

1. Which age groups show the strongest social-media engagement?

2. Do highly engaged demographics exhibit stronger e-commerce participation?

3. How do purchasing patterns differ across education segments?

4. How did digital behavior evolve during:

- Pandemic years (2020–2021)
- Post-pandemic normalization
- Recent digital transition period (2023–2025)

---

## Data Source

Source:

Eurostat Databrowser

Country:

Germany (DE)

---

### Dataset 1 — Social Media Usage

Table:

`isoc_ci_ac_i`

Indicators:

| Code | Meaning |
|-------|----------|
| I_IUSNET | Social Media Participation |
| I_IUIF | Product Information Search |
| I_IUEM | Email Usage |
| I_IUNW1 | Online News Reading |

---

### Dataset 2 — E-commerce

Table:

`isoc_ec_ib20`

Indicators:

| Code | Meaning |
|-------|----------|
| I_BF_1_2 | Low Purchase Frequency (1–2 purchases) |
| I_BF_3-5 | Moderate Purchase Frequency (3–5 purchases) |
| I_BF_6-10 | High Purchase Frequency (6–10 purchases) |
| I_BF_GT10 | Very High Purchase Frequency (10+ purchases) |
| I_BUX | Never Purchased Online |

---

## Demographic Dimensions

### Age

- Y16_24
- Y25_54
- Y55_74

### Gender

- F_Y16_74
- M_Y16_74

### Education

Low:

- Y16_24LO
- Y25_54LO
- Y55_74LO

Medium:

- Y16_24ME
- Y25_54ME
- Y55_74ME

High:

- Y16_24HI
- Y25_54HI
- Y55_74HI

---

## Project Workflow

Raw Eurostat Data

↓

Cleaning & Validation

↓

EDA

↓

Dataset Integration

↓

Trend Analysis

↓

Correlation Analysis

↓

Dashboard Development

↓

Business Insights

---

## Cleaning Pipeline

Completed tasks:

✔ Missing value handling

✔ Column standardization

✔ Indicator renaming

✔ Demographic classification

✔ Education integration

✔ Employment-group removal

✔ Metadata cleanup

✔ Dataset export

Output files:

```text
germany_social_clean.csv

germany_ecommerce_clean.csv
```

---

## Technology Stack

| Tool | Purpose |
|-------|----------|
| Python | Data analysis |
| pandas | Cleaning & transformation |
| scipy | Correlation analysis |
| matplotlib | Visualization |
| seaborn | EDA |
| Jupyter Notebook | Development |
| Tableau Public | Dashboard |
| GitHub | Portfolio |

---

## Repository Structure

```text
project/

│── data/

│   ├── germany_social_clean.csv

│   ├── germany_ecommerce_clean.csv

│

│── notebooks/

│   ├── data_cleaning.ipynb

│   ├── analysis.ipynb

│

│── dashboard/

│   └── tableau_dashboard.twb

│

│── README.md
```

---

## Current Limitations

### Aggregated Data

Eurostat provides population-level percentages rather than individual observations.

Findings indicate associations only.

---

### Temporal Availability

Some e-commerce frequency indicators were unavailable for specific years.

Interpretation therefore focuses on observed behavioral patterns rather than continuous yearly measurements.

---

### Germany Scope

The study focuses only on Germany and may not generalize to other EU countries.

---

## Deliverables

- analysis.ipynb

- germany_social_clean.csv

- germany_ecommerce_clean.csv

- Tableau Dashboard

- Executive Summary

- GitHub Repository

---

## Future Improvements

Potential extensions:

- Cross-country EU comparison

- Employment segmentation

- Additional digital indicators

- Advanced statistical modeling

---

## Author

Noorulain Faheem

Project Type:

Portfolio / Data Analytics Project

Topic:

Digital Engagement & E-commerce Analysis