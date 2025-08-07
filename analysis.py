import pandas as pd

# Load Excel files
df_financials = pd.read_excel('financials.xlsx')
df_skus = pd.read_excel('sku_data.xlsx')
df_suppliers = pd.read_excel('supplier_costs.xlsx')
df_logistics = pd.read_excel('logistics.xlsx')

print("✅ Excel files loaded successfully.")

import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("profitability_analysis.db")

# Save each DataFrame into SQL tables
df_financials.to_sql("financials", conn, if_exists="replace", index=False)
df_skus.to_sql("sku_data", conn, if_exists="replace", index=False)
df_suppliers.to_sql("supplier_costs", conn, if_exists="replace", index=False)
df_logistics.to_sql("logistics", conn, if_exists="replace", index=False)

print("✅ Data loaded into SQLite database.")


# SQL: Calculate profit and margin
query = """
SELECT 
    "Year", 
    "Business Unit",
    "Revenue",
    "COGS_Fixed" + "COGS_Variable" + "Operating_Expense" AS Total_Cost,
    ("Revenue" - ("COGS_Fixed" + "COGS_Variable" + "Operating_Expense")) AS Profit,
    ROUND((("Revenue" - ("COGS_Fixed" + "COGS_Variable" + "Operating_Expense")) * 100.0) / "Revenue", 2) AS Profit_Margin
FROM financials
ORDER BY "Year", "Business Unit";
"""

# Run the query
df_sql_profit = pd.read_sql(query, conn)

# Print result
print("\n📊 Profit Margin Report:")
print(df_sql_profit)


df_sql_profit.to_excel("profit_margin_report.xlsx", index=False)
print("✅ Report saved as 'profit_margin_report.xlsx'")


query_low_margin = """
SELECT 
    "SKU_ID",
    "Business Unit",
    "Units Sold",
    "Unit Cost",
    "Unit Price",
    ROUND(("Unit Price" - "Unit Cost") * 100.0 / "Unit Price", 2) AS SKU_Margin_Percent
FROM sku_data
ORDER BY SKU_Margin_Percent ASC
LIMIT 10;
"""

df_low_margin_skus = pd.read_sql(query_low_margin, conn)

print("\n❗ Lowest-Margin SKUs:")
print(df_low_margin_skus)

import seaborn as sns
import matplotlib.pyplot as plt

# Create heatmap from logistics table
df_logistics_pivot = df_logistics.pivot(index='Region', columns='Business Unit', values='Logistics Cost')

plt.figure(figsize=(8, 6))
sns.heatmap(df_logistics_pivot, annot=True, fmt=".0f", cmap='coolwarm')
plt.title("🚚 Logistics Cost by Region and Business Unit")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_sql_profit, x='Year', y='Profit_Margin', hue='Business Unit', marker='o')
plt.title("📉 Profit Margin Trend by Business Unit")
plt.ylabel("Profit Margin (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

with pd.ExcelWriter("Profitability_Analysis_Final_Report.xlsx") as writer:
    df_sql_profit.to_excel(writer, index=False, sheet_name='Profit Margins')
    df_low_margin_skus.to_excel(writer, index=False, sheet_name='Low Margin SKUs')
    df_financials.to_excel(writer, index=False, sheet_name='Raw Financials')
    df_logistics.to_excel(writer, index=False, sheet_name='Logistics')
    df_suppliers.to_excel(writer, index=False, sheet_name='Suppliers')

print("✅ Final Excel Report saved as 'Profitability_Analysis_Final_Report.xlsx'")


