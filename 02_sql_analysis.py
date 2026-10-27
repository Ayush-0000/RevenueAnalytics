
import sqlite3
from pathlib import Path
import pandas as pd

# Connect to the database created by our first script
db_path = Path("online_retail_clean.db")

if not db_path.exists():
    raise FileNotFoundError(
        "Database not found. Run 01_clean_data.py first."
    )

with sqlite3.connect(db_path) as conn:

    # 1. SALES SUMMARY
    query1 = """
        SELECT customer_id,
               invoice,
               description,
               country,
               year,
               month,
               week,
               price,
               quantity AS total_quantity,
               quantity * price AS total_revenue,
               invoicedate
        FROM retail_data
        WHERE quantity > 0
    """
    sales_summary = pd.read_sql_query(query1, conn)

    # 2. PRODUCTS BY QUANTITY
    query2 = """
        SELECT invoice,
               stockcode,
               description,
               quantity AS total_quantity
        FROM retail_data
        WHERE quantity > 0
        ORDER BY total_quantity DESC
    """
    products_by_quantity = pd.read_sql_query(query2, conn)

    # 3. CUSTOMER ACTIVITY
    query3 = """
        SELECT customer_id,
               MAX(country) AS country,
               SUM(quantity * price) AS total_spent,
               MAX(invoicedate) AS last_purchase_date,
               COUNT(DISTINCT year || '-' || month) AS active_months
        FROM retail_data
        WHERE quantity > 0
        GROUP BY customer_id
        ORDER BY total_spent DESC
    """
    customer_activity = pd.read_sql_query(query3, conn)

    # 4. RETURNS SUMMARY
    query4 = """
        SELECT customer_id,
               invoice,
               country,
               year,
               month,
               week,
               stockcode,
               description,
               price,
               ABS(quantity) AS total_returns_quantity,
               ABS(quantity * price) AS total_returns_value,
               invoicedate
        FROM retail_data
        WHERE quantity < 0
    """
    returns_summary = pd.read_sql_query(query4, conn)

    # 5. PRODUCT SALES AND RETURNS
    query5 = """
        SELECT stockcode,
               MAX(description) AS description,
               SUM(
                   CASE WHEN quantity > 0
                   THEN quantity * price ELSE 0 END
               ) AS total_revenue,
               SUM(
                   CASE WHEN quantity < 0
                   THEN 1 ELSE 0 END
               ) AS return_count
        FROM retail_data
        GROUP BY stockcode
    """
    product_summary = pd.read_sql_query(query5, conn)

# Export all four query results to CSV files
sales_summary.to_csv("sales_summary.csv", index=False)
products_by_quantity.to_csv("products_by_quantity.csv", index=False)
customer_activity.to_csv("customer_activity.csv", index=False)
returns_summary.to_csv("returns_summary.csv", index=False)
product_summary.to_csv("product_summary.csv", index=False)

print("SQL analysis completed successfully!")
print("Sales rows:", len(sales_summary))
print("Product rows:", len(products_by_quantity))
print("Customer rows:", len(customer_activity))
print("Return rows:", len(returns_summary))
