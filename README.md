# Customer Shopping Behavior Analysis

An end-to-end data analytics project that analyzes customer shopping behavior using **Python, MySQL and Power BI**. The project covers data loading, exploratory data analysis, data cleaning, SQL-based business analysis, an interactive dashboard, and a written project report.

---

## Overview

This project analyzes transactional data from **3,900 purchases** across multiple product categories. The goal is to uncover insights into spending patterns, customer segments, product preferences, and subscription behavior to support business decisions.

**Workflow:**

```
Raw CSV -> Python (EDA, cleaning, feature engineering) -> Cleaned CSV -> MySQL -> SQL analysis -> Power BI dashboard -> Project report
```

---

## Dataset

- **Rows:** 3,900
- **Columns:** 18
- **Customer demographics:** Age, Gender, Location, Subscription Status
- **Purchase details:** Item Purchased, Category, Purchase Amount, Season, Size, Color
- **Shopping behavior:** Discount Applied, Promo Code Used, Previous Purchases, Frequency of Purchases, Review Rating, Shipping Type
- **Missing data:** 37 values in the `Review Rating` column

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Data loading, EDA, cleaning, feature engineering |
| Pandas | Data manipulation and analysis |
| SQLAlchemy + PyMySQL | Connecting Python to MySQL and loading data |
| MySQL | Storing data and running business queries |
| Power BI | Interactive dashboard |
| Microsoft Word | Project report |

---

## Project Steps

### 1. Exploratory Data Analysis (Python)
- Loaded the dataset with Pandas
- Checked structure and data types with `df.info()`
- Generated summary statistics with `df.describe()`

### 2. Data Cleaning & Preprocessing
- **Missing values:** Filled missing `Review Rating` values with the median rating of each product category
- **Column names:** Converted to lowercase snake_case and renamed `purchase_amount_(usd)` to `purchase_amount`
- **Consistency check:** Found `discount_applied` and `promo_code_used` to be identical and dropped `promo_code_used`

### 3. Feature Engineering
- **`age_group`:** Customer ages split into four groups using `pd.qcut`
- **`purchase_frequency_days`:** Text purchase frequencies (for example Weekly, Monthly) mapped to numeric days

### 4. Database Integration
- Loaded the cleaned DataFrame into a MySQL database (`customer_shopping_db`, table `customer_shopping`) using SQLAlchemy

### 5. SQL Analysis (MySQL)
Ten business questions were answered with SQL:

1. Revenue by gender
2. Discount users spending at or above the average purchase amount
3. Top 5 products by average review rating
4. Average purchase amount: Standard vs Express shipping
5. Subscribers vs non-subscribers (customers, average spend, revenue)
6. Top 5 products by percentage of discounted purchases
7. Customer segmentation: New, Returning, Loyal
8. Top 3 most purchased products per category
9. Subscription status of repeat buyers (more than 5 previous purchases)
10. Revenue by age group

### 6. Dashboard (Power BI)
- Built an interactive dashboard to present the findings visually

### 7. Project Report
- Documented the full process, queries, results, and recommendations in a Word report

---

## Dashboard

![Customer Shopping Behavior Dashboard](images/dashboard.png)

**Dashboard features:**
- KPI cards: Total Customers, Total Revenue, Average Purchase Amount, Average Review Rating
- Filters: subscription, gender, category, shipping type, payment method
- Charts: customers by subscription status, revenue by gender, revenue by category, revenue by age group, top 10 products by revenue

---

## Results

Key findings from the SQL analysis:

- **Revenue by gender:** Male customers generated 157,890 and female customers 75,191 (about 67.7% vs 32.3% of total revenue)
- **Subscription:** 1,053 subscribers and 2,847 non-subscribers; average spend is similar (59.49 vs 59.87)
- **Shipping:** Express shipping has a slightly higher average purchase amount (60.48) than Standard (58.46)
- **Top rated products:** Gloves (3.86), Sandals (3.84), Boots (3.82), Hat (3.80), Skirt (3.78)
- **Most discounted products:** Hat (50.00%), Sneakers (49.66%), Coat (49.07%), Sweater (48.17%), Pants (47.37%)
- **Customer segments:** Loyal 3,116, Returning 701, New 83
- **Revenue by age group:** Young_Adult 62,143, Middle_Ageg 59,197, Adult 55,978, Senior 55,763

---

## Business Recommendations

- **Grow subscriptions:** Test clear member benefits such as exclusive offers or early access, and track subscription rate, repeat purchases, and revenue per customer
- **Strengthen customer loyalty:** Use the New, Returning, and Loyal segments to tailor follow-ups and rewards
- **Optimize discount strategy:** Identify products frequently bought with discounts, then compare sales and profit to avoid unnecessary markdowns
- **Improve product positioning:** Promote products that combine strong sales with high ratings, and investigate lower-rated products before increasing promotion
- **Refine targeted marketing:** Use age-group, category, and gender views to design campaign tests before shifting budget

---

## Skills Demonstrated

- Data cleaning and preprocessing with Python and Pandas
- Exploratory data analysis
- Feature engineering
- SQL: aggregations, filtering, subqueries, CTEs, `CASE` statements, window functions
- Python to MySQL integration with SQLAlchemy
- Dashboard design and data visualization in Power BI
- Business insight generation and technical documentation

---

## Author

**Parth jadwani**
