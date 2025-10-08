<<<<<<< HEAD
# Global-Economic-Trends-Analysis

# 🌍 Global Economic Insights Dashboard

**Author:** Razan Widya Reswara  
**Tech Stack:** Python · Prefect · Pandas · SQLite · Power BI  
**Data Source:** World Bank API  
**Project Type:** End-to-End Data Analytics (ETL → Visualization → Insights)

---

## 🎯 Project Overview

The **Global Economic Insights Dashboard** is an end-to-end data analytics project designed to analyze key global economic indicators — **GDP Growth, Inflation, and Unemployment** — for major countries from 2000 to 2024.

This project automates data extraction from the **World Bank API**, performs transformation & cleaning in Python, and visualizes the results in **Power BI** to uncover meaningful macroeconomic trends.

💡 The goal:  
> To tell a clear story of how different economies grow, struggle, and stabilize over time — combining data engineering, analytics, and storytelling in one project.

---

## 🧱 Project Architecture

             ┌──────────────────────────────┐
             │  World Bank API              │
             │  (GDP, Inflation, Unemp.)    │
             └────────────┬─────────────────┘
                          │
                 [Extract with Prefect Flow]
                          │
                          ▼
           ┌──────────────────────────────┐
           │   Transform (Pandas)         │
           │   - Clean data               │
           │   - Normalize percentages    │
           │   - Handle missing values    │
           └────────────┬─────────────────┘
                          │
                 [Load to SQLite + CSV]
                          │
                          ▼
           ┌──────────────────────────────┐
           │ Power BI Visualization       │
           │ - KPI Cards                  │
           │ - Trend Lines                │
           │ - Phillips Curve Scatter     │
           │ - Stability Index Analysis   │
           └──────────────────────────────┘


---

## ⚙️ Pipeline Components

| Step | Tool | Description |
|------|------|-------------|
| **Extract** | `requests`, `Prefect` | Retrieve GDP, Inflation, and Unemployment data from the World Bank API for multiple countries |
| **Transform** | `Pandas` | Clean data, normalize scales (convert raw scientific notation to %), handle missing/unrealistic values |
| **Load** | `SQLite` & `.csv` | Store clean dataset for reproducible analysis |
| **Visualize** | `Power BI` | Create interactive dashboard and storytelling visualizations |

---

## 🔍 API Details

| Indicator | World Bank Code | Description |
|------------|------------------|--------------|
| GDP Growth | `NY.GDP.MKTP.KD.ZG` | Annual growth rate of GDP (constant local currency) |
| Inflation | `FP.CPI.TOTL.ZG` | Annual % change in consumer price index |
| Unemployment | `SL.UEM.TOTL.ZS` | % of total labor force unemployed |

---

## 🧩 ETL Challenges & Solutions

| Challenge | Description | Solution |
|------------|--------------|-----------|
| **Scientific Notation Values** | Data returned from the API was in very large exponential form (e.g., `3.9215E+14`) | Normalized using division by the correct scale factor (1e16) to restore true percentage values |
| **Inconsistent Units** | Inflation and Unemployment had different scales (one in %, one in basis points) | Applied standard transformation to unify into comparable percentage format |
| **Null and Negative Values** | Some countries had missing or negative growth data during recession years | Filled small gaps with rolling averages and retained negative values for economic realism |
| **Data Type Errors in Power BI** | Decimal values imported as text causing display issues | Fixed using Power Query → Change Type → Decimal Number |
| **Conditional Formatting for Gen Z Aesthetic** | Power BI default theme too flat | Applied custom gradient (teal–purple) and minimal neon highlights for contrast |

---

## 📊 Dashboard Highlights

### **Main Pages:**
1. **Global Trend Overview**  
   Line chart tracking GDP Growth, Inflation, and Unemployment from 2000–2024.

2. **Phillips Curve Analysis**  
   Scatter plot visualizing the trade-off between Inflation and Unemployment with country filter and year slicer.

3. **KPI Cards (Automated DAX Metrics)**  
   - 🏆 **Top GDP Growth:** Country with highest average GDP  
   - 💰 **Highest Inflation:** Country with highest inflation average  
   - 💼 **Lowest Unemployment:** Country with lowest unemployment rate  
   - 🌪️ **Most Volatile Inflation:** Highest inflation standard deviation  
   - ⚖️ **Economic Stability Index:** Composite score of growth vs. instability

4. **GDP Comparison Chart**  
   Horizontal bar chart ranking countries by GDP growth.

---

## 🧠 Data Storytelling & Key Insights

### **1️⃣ Global Recovery & Growth**
India and China maintained consistently high GDP growth (~5–6%), demonstrating resilience and rapid post-pandemic recovery.

### **2️⃣ Inflation Volatility**
Japan surprisingly exhibited the highest *inflation volatility*, driven by deflationary pressure pre-2010 and a rebound after 2020.

### **3️⃣ Employment Dynamics**
Developed economies (e.g., Japan, Germany) achieved the lowest unemployment rates (<5%), while emerging markets showed larger swings.

### **4️⃣ Economic Stability Index**
The stability score combined GDP growth, inflation, and unemployment — identifying nations with *balanced, sustainable growth* vs. those with high volatility.

---

## 🎨 Visual Identity (Gen Z Design Language)

- **Theme:** Modern Dark Mode with Neon Gradients  
- **Palette:**  
  - Teal `#00C9A7` → Growth  
  - Coral Red `#FF6B6B` → Inflation  
  - Yellow `#FFD93D` → Unemployment  
  - Indigo `#7B61FF` → Stability Metrics  
- **Fonts:** *Poppins*, *Inter*, *Segoe UI*  
- **Effects:** Rounded corners, shadows, glow on key metrics

---

## 📷 Dashboard Preview

<img width="957" height="531" alt="image" src="https://github.com/user-attachments/assets/32d63441-d9db-4c22-a182-0be6f552b846" />

---

## 🚀 Future Improvements

- Automate monthly refresh using Prefect scheduler  
- Deploy interactive dashboard to Power BI Service  
- Add machine learning model to forecast GDP and Inflation trends  

---

## 📚 References

- [World Bank Data API](https://data.worldbank.org)  
- [Prefect Documentation](https://docs.prefect.io)  
- [Power BI Design Guidelines](https://learn.microsoft.com/power-bi/create-reports/)

---

## 🧾 Summary

> This project represents a complete data analytics lifecycle — from API extraction, ETL, database management, and visualization, to insight communication.  
> It demonstrates both *technical skill* and *storytelling ability* — key aspects of a modern data analyst portfolio.

---
=======
# Global Economic Trends (World Bank API → Prefect → CSV/SQLite → Power BI)

This is a starter project to build an end-to-end data pipeline:
World Bank API → ETL with Python → Orchestrate with Prefect → Save to CSV/SQLite → Visualize in Power BI.

## Quickstart (Windows + VS Code)

1. Create & activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -U pip
   pip install -r requirements.txt
   ```

2. Run the pipeline:
   ```powershell
   python -m src.flow
   ```

3. Outputs:
   - `data/economic_metrics.csv`
   - `data/economic_trends.db` (SQLite with table `economic_metrics`)

4. Power BI:
   - Get Data → Text/CSV → pick `data/economic_metrics.csv`
   - Add slicers for Country/Year/Indicator; build Line/Scatter/Bar charts.
>>>>>>> c0589f4 (tools for ETL)
