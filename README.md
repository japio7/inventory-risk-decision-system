# Inventory Risk Decision System

## Overview

This project analyzes inventory data to identify parts at risk of
stockout.\
The dataset contains \~500 parts but only **7 stockout events (1.4%)**,
making predictive machine learning unreliable due to extreme class
imbalance.

Instead of relying solely on ML models, this project develops a **risk
scoring framework** to prioritize high‑risk inventory items.

---
## Key Insights

-   Stockout events are extremely rare (1.4%)
-   Machine learning models can produce misleading results when event
    frequency is too low
-   A rule‑based risk scoring system can be more effective in these
    scenarios

---
## Dataset Features

  Feature           Description
  ---  inventory_value   Total value of inventory
  days_of_supply    Estimated remaining inventory duration
  lead_time_days    Supplier lead time
  daily_usage       Average daily usage
  unit_cost         Cost per unit
  stockout_flag     Indicates stockout event

---

## 📊 Risk Model Evaluation

- Top 20% highest-risk items capture 71% of stockouts
- Top 10% capture 52% of stockouts

This demonstrates the model effectively prioritizes critical inventory.

___


## Risk Scoring Model

Risk Score Calculation:

    +3 if days_of_supply < lead_time_days
    +2 if lead_time_days > 20
    +1 if daily_usage > median usage

Items are ranked by risk score to identify parts most likely to cause
operational disruption.

---

## 🚦 Action Strategy

| Risk Score | Action |
|----------|--------|
| 4+ | Immediate reorder |
| 3 | Monitor closely |
| ≤2 | Low priority |

---

## 💰 Estimated Impact

- Avg stockout cost: $1,000
- Preventing 5 stockouts/year → $5,000 savings

This system provides measurable operational value.

---

## Example Visualizations

-   Stockout Risk vs Inventory Value
-   Top High‑Risk Inventory Items
-   Inventory Distribution Analysis

---
## Project Structure

```
inventory-risk-analysis
│
├── README.md
├── Inventory Risk Analysis Report.pdf
│
├── data_generator.py
│
├── data
│   ├── inventory_master.csv
│   └── transactions.csv
│
├── notebooks
│   └── inventory_risk_analysis.ipynb
│
└── outputs
    └── figures
```

---
## Tools Used

-   Python
-   Pandas
-   Numpy
-   Scikit‑learn
-   Matplotlib

---
## Author

**Jared Pino**\
MS Data Science

GitHub: https://github.com/japio7
