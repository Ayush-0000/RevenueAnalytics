Retail Sales & Customer Insights Dashboard

An end-to-end retail analytics project using Python, SQL (SQLite), and Power BI to analyse sales performance, customer activity, product sales, and returns.
Tech Stack
- Python: pandas, openpyxl
- SQL: SQLite
- Visualisation: Microsoft Power BI Desktop (DAX measures)
Workflow
1. Clean data — 01_clean_data.py
   Combines the two sheets in online_retail_II.xlsx, removes missing rows and duplicates, creates date attributes, and saves the cleaned data to online_retail_clean.db.
2. Analyse data — 02_sql_analysis.py
   Runs SQL queries against the SQLite database and exports CSV tables for Power BI.
3. Build dashboard — Power BI
   Imports the CSV outputs and presents key metrics and interactive charts.


   <img width="1349" height="776" alt="image" src="https://github.com/user-attachments/assets/d0be068e-e296-45c3-a353-c8b43b40aa0a" />

Dashboard Features
- KPI cards for revenue, quantity sold, revenue per customer, return percentage, return count, and return value
- Monthly revenue and returns trends
- Customer table with activity months and customer type
- Returns by country treemap
- Product revenue versus return-line count
- Customer activity by active months
- Average order value and average price over time
- Slicers for customer type, year, and country

  
Dataset
The project uses the Online Retail II dataset from the UCI Machine Learning Repository. Place online_retail_II.xlsx in the project folder alongside the Python scripts. The workbook should contain the sheets Year 2009-2010 and Year 2010-2011.
Run Locally
From the online+retail+ii project directory, install dependencies and run the scripts:
python -m pip install pandas openpyxl
python 01_clean_data.py
python 02_sql_analysis.py
The scripts create online_retail_clean.db and these CSV files:
- sales_summary.csv
- products_by_quantity.csv
- customer_activity.csv
- returns_summary.csv
- product_summary.csv
Import the CSV files into Power BI Desktop and open the saved .pbix report to explore the dashboard. The .xlsx, .db, and generated CSV files are produced or supplied locally and may be excluded from version control if they are too large.
