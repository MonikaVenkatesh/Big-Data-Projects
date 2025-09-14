# Finance Investment Analysis using PySpark (Databricks)

## 📌 Overview
This project analyzes investment preferences (Mutual Funds, Bonds, Gold, etc.)
by Age Group and Gender using PySpark on Databricks.  

It demonstrates:
- Data cleaning and feature engineering
- Normalization of investment values
- Group-wise aggregations
- Ranking top 3 investors using Window functions

## 📊 Sample Output
Top 3 investors by Total Investment Score per Age Group:

| age | GenderGroup | gender | Total_Investment_Score | Rank_in_AgeGroup |
|-----|-------------|--------|-------------------------|------------------|
| 22  | Young       | Male   | 30                      | 1                |
| 24  | Young       | Female | 29                      | 2                |
| 23  | Young       | Male   | 27                      | 3                |

## 🛠️ Tech Stack
- Databricks (PySpark)
- Python 3
- GitHub for version control
