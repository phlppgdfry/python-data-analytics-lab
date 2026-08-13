# Python Data Analytics Lab

[![Tests](https://github.com/phlppgdfry/python-data-analytics-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/phlppgdfry/python-data-analytics-lab/actions/workflows/tests.yml)
[![Status](https://img.shields.io/badge/status-learning%20companion-2563eb)](https://github.com/phlppgdfry/python-data-analytics-lab)
[![Python](https://img.shields.io/badge/Python-learning%20path-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-SQL%20practice-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)

> **Learning companion repository.** For the finished, deployed portfolio application, see [Sales Analytics Project](https://github.com/phlppgdfry/python-data-analytics-project) and its [live dashboard](https://sales-analytics-phlppgdfry.streamlit.app/).

This repository is the hands-on learning path behind the larger portfolio app. It progresses from small Python exercises to NumPy, Pandas, data cleaning, business analysis, visualisation, SQL and PostgreSQL. Each numbered script is intentionally small enough to study and run independently.

```text
Concept → explanation → small exercise → apply it to sales data → test → Git commit
```

## What you learn

```text
CSV data
    ↓
Pandas: loading, filtering, groupby, cleaning and dates
    ↓
Business KPIs and statistics
    ├── Matplotlib: static PNG reports
    ├── Plotly: interactive HTML charts
    └── Streamlit: filterable dashboard

PostgreSQL
    ↓ SQL query
Pandas DataFrame → analysis
```

| Area | Lessons | Evidence in this repo |
| --- | --- | --- |
| Python foundations | 01–07 | variables, collections, conditions, loops, functions, files and errors |
| NumPy and statistics | 08–10 | arrays, statistics and filtering |
| Pandas basics | 11–16 | DataFrames, CSV, calculated columns, filters and `groupby` |
| Data quality | 17–20 | inspecting dirty data, normalising text, cleaning and dates |
| Business analysis | 21–23 | KPIs and monthly revenue analysis |
| SQL and PostgreSQL | 24 | SQL schema, import, queries and reading results in Pandas |

## Quick start

```bash
git clone https://github.com/phlppgdfry/python-data-analytics-lab.git
cd python-data-analytics-lab

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python src/01_python_basics.py
python src/19_clean_data.py
python src/21_kpis.py
streamlit run dashboard/app.py
```

Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## Visualisation exercises

```bash
# Static Matplotlib charts
python visualizations/matplotlib_monthly_revenue.py
python visualizations/matplotlib_revenue_by_product.py

# Interactive Plotly charts
python visualizations/plotly_monthly_revenue.py
python visualizations/plotly_revenue_by_product.py
```

Generated reports appear in `reports/charts/` and are intentionally excluded from Git because the scripts reproduce them at any time.

## PostgreSQL lab

When PostgreSQL is installed locally, this lab demonstrates the company-style flow `CSV → PostgreSQL → SQL → Pandas → analysis`.

```bash
createdb -h 127.0.0.1 analytics_lab
psql -h 127.0.0.1 -d analytics_lab -f sql/schema.sql
psql -h 127.0.0.1 -d analytics_lab -f sql/import_sales.sql
psql -h 127.0.0.1 -d analytics_lab -f sql/queries.sql
python src/24_read_postgres.py
```

## Tests and project structure

```bash
pytest
```

GitHub Actions runs the cleaning test on every push and pull request. The repository includes raw and intentionally messy CSV files, a Streamlit dashboard, SQL scripts, numbered exercises, visualisation scripts and pytest checks.

```text
python-data-analytics-lab/
├── data/raw/              # clean, dirty and analysis CSV files
├── dashboard/app.py       # local Streamlit dashboard
├── sql/                   # schema, import and business SQL queries
├── src/                   # 24 numbered lessons plus shared helpers
├── tests/                 # pytest checks
├── visualizations/        # Matplotlib and Plotly scripts
└── .github/workflows/     # automated test workflow
```

## Skills demonstrated

`Python` · `NumPy` · `Pandas` · `data cleaning` · `business KPIs` · `Matplotlib` · `Plotly` · `Streamlit` · `PostgreSQL` · `SQL` · `pytest` · `GitHub Actions`
