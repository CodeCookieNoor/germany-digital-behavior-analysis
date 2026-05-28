# Dataset Issues & Methodology Questions

Project:

Digital Engagement & E-commerce Behavior in Germany (2020–2025)

Status:

Cleaning phase completed

Before starting EDA, the following methodology and data issues require validation.

---

# Priority Questions

## Q1 — Missing Ecommerce Frequency Years (HIGH PRIORITY)

Issue:

E-commerce purchase-frequency indicators are unavailable for some years.

Available:

2020
2021
2023
2025

Missing:

2022
2024

Affected indicators:

I_BF_3-5

I_BF_6-10

I_BF_GT10

Question:

Should analysis:

1. Continue using only available years?

2. Remove yearly evolution claims?

3. Replace missing indicators?

Risk:

Temporal analysis may become inconsistent.

---

## Q2 — Aggregated Data vs Correlation Analysis

Issue:

Eurostat provides aggregated demographic percentages rather than individual observations.

Current data:

Percentage of population groups

NOT:

Individual consumer behavior data

Question:

Is correlation analysis methodologically acceptable using aggregated demographic percentages?

Alternative:

Trend analysis only

Comparative demographic analysis

Risk:

Potential ecological fallacy.

---

## Q3 — Merge Validity

Planned merge keys:

year

demo_code

education_level

Question:

Is merging social-media and e-commerce tables using demographic dimensions valid?

Risk:

Potential mismatch between aggregated datasets.

---

## Q4 — Education Structure

Education download produced:

Y16_24HI

Y16_24LO

Y25_54ME

etc.

Meaning:

Age + Education combined

NOT:

Independent education variable

Question:

Should analysis:

A)

Use education inside age groups

OR

B)

Separate age and education analyses?

Risk:

Interpretation complexity.

---

## Q5 — Gender Coverage Difference

Available:

F_Y16_74

M_Y16_74

Education groups:

No gender split

Question:

Should gender remain exploratory only?

Risk:

Unequal demographic granularity.

---

## Q6 — Temporal Framing

Current project framing:

Pandemic (2020–2021)

Post-pandemic

AI emergence (2023–2025)

Issue:

Dataset contains:

Internet behavior

Shopping behavior

NOT:

AI adoption indicators

Question:

Can AI-emergence framing remain contextual only?

Risk:

Overinterpretation.

---

## Q7 — Correlation Method Choice

Planned:

Pearson correlation

Question:

Should Pearson correlation be used?

Alternatives:

Spearman

Descriptive comparison

Cluster analysis

Segment analysis

Risk:

Small aggregated groups.

---

## Q8 — Removed Variables

Removed:

Y25_64_SALSELFFAM

Y25_64_UNE

Reason:

Outside project scope.

Question:

Should employment remain excluded?

Risk:

Potential loss of segmentation dimension.

---

# Dataset Observations

## Social Media Dataset

Status:

Clean

Education available for all years.

Age:

Y16_24

Y25_54

Y55_74

Gender:

F_Y16_74

M_Y16_74

Education:

HI

ME

LO

---

## Ecommerce Dataset

Issue:

Partial yearly availability.

Frequency indicators missing for:

2022

2024

Potential impact:

Trend continuity.

---

# Methodology Validation Needed

Need coach confirmation for:

[ ] Correlation validity

[ ] Merge strategy

[ ] Education interpretation

[ ] Missing-year handling

[ ] Dashboard scope

[ ] Final methodology

---

# Goal After Discussion

Start:

EDA

↓

Merge

↓

Correlation

↓

Dashboard

↓

Report