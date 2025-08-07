# 📊 Profitability Analysis & Cost Optimization

This project models the profitability of a multi-unit business and identifies cost optimization opportunities using Python, SQL (SQLite), and Excel. It involves financial analytics, SKU-level profitability analysis, supplier and logistics cost evaluation, and scenario-based recommendation modeling.

## 🚀 Project Overview

- **Objective**: Identify areas of cost inefficiency and propose data-backed strategies to optimize margins.
- **Tools Used**: Python (Pandas, SQLite3), SQL, Excel, PowerPoint
- **Business Scope**:
  - 3 years of financial data across 4 business units
  - SKU-level and supplier-level performance evaluation
  - Transportation/logistics cost analysis

## 🗂️ Data Sources

| File Name           | Description                                |
|---------------------|--------------------------------------------|
| `financials.xlsx`   | BU-level Revenue, COGS, Margin              |
| `sku_data.xlsx`     | SKU-wise Revenue, Cost, Units Sold         |
| `supplier_costs.xlsx` | Supplier cost, delivery fees               |
| `logistics.xlsx`    | Transport mode, distance, cost              |

## ⚙️ Project Pipeline

### 1. Data Preparation

- Loaded Excel files using `pandas` and `openpyxl`
- Cleaned and standardized column names
- Created calculated columns for profitability and margin analysis

### 2. SQL-based Analytics

- Converted dataframes to SQLite tables
- Ran SQL queries for key insights:
  - Unprofitable SKUs
  - Supplier cost benchmarking
  - Logistics cost by transport mode
  - Margin trends by business unit

### 3. Key Insights

- **20% of SKUs** were loss-making
- **Supplier X** was 12% above cost benchmark
- **BU-2 & BU-4** had >15% margin decline over 3 years
- **Road logistics** dominated 40% of total spend

### 4. Recommendations

- Rationalize low-performing SKUs
- Renegotiate supplier contracts
- Optimize transportation mix (introduce multimodal options)

### 5. Scenario Modeling

- **Base Case**: Partial SKU and logistics improvement → ~$2.6M savings
- **Aggressive Case**: Full-scale optimization → ~$4.2M savings

### 6. Final Deliverables

- 🐍 Python scripts / Jupyter notebook
- 🗃️ SQLite database: `profitability.db`
- 📊 Excel input files
- 📽️ PowerPoint Presentation

