# Sales-Performance-Dashboard-Data-Cleaning-Power-BI-Analysis

This project focuses on cleaning, validating, and transforming retail sales data using Python (pandas & NumPy) and delivering a fully interactive Sales Performance dashboard in Power BI.
The goal was to simulate a real-world data analytics workflow, starting from raw, inconsistent transactional data and ending with a business-ready dashboard that enables decision-making.

🛠️ Tools & Technologies
Python (pandas, NumPy)
Power BI
CSV data source
Data cleaning, feature engineering, and validation techniques

🔍 Data Cleaning & Preparation (Python)
The raw dataset contained missing values, inconsistent totals, and unstructured date information. The following steps were applied:
Missing value imputation:
 Filled missing Item values using their corresponding Category
 Filled missing Price Per Unit using historical item-level prices
Date feature engineering:
 Extracted transaction year, month (text & numeric), and day
Data validation:
 Recalculated total transaction values (Price Per Unit × Quantity)
 Corrected inconsistent Total Spent values using numeric tolerance
Data quality control:
 Removed unrecoverable records with critical missing values
Export:
 Cleaned and structured dataset exported for Power BI consumption

📈 Power BI Dashboard
The Power BI report visualizes sales performance through:
Key KPIs:
 Total Sales
 Total Customers
 Quantity Sold
 Average Price per Unit
Sales trends:
 Monthly sales evolution
Category analysis:
 Sales distribution by product category
Payment method breakdown:
 Cash, Credit Card, Digital Wallet
Sales channel comparison:
 Online vs In-store

The dashboard is designed to be interactive, allowing users to filter by year, month, and product category.
<img width="1273" height="716" alt="Captura de pantalla 2026-01-09 234540" src="https://github.com/user-attachments/assets/533bb0c1-98dc-47ce-be58-492c7c3158ea" />



