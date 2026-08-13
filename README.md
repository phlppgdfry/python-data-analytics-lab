# Python Data Analytics Lab

[![Tests](https://github.com/phlppgdfry/python-data-analytics-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/phlppgdfry/python-data-analytics-lab/actions/workflows/tests.yml)

Een end-to-end sales-analyticsproject dat tegelijk als leerlab en
portfolio-project dient. De repository toont hoe ruwe verkoopdata wordt
opgeschoond, geanalyseerd, gevisualiseerd en gepresenteerd in een dashboard.

## Wat dit project doet

\`\`\`text
CSV-data
    ↓
Pandas: cleaning en transformatie
    ↓
KPI's en zakelijke analyses
    ├── Matplotlib: statische PNG-rapporten
    ├── Plotly: interactieve HTML-grafieken
    └── Streamlit: filterbaar dashboard

PostgreSQL
    ↓ SQL-query
Pandas DataFrame
\`\`\`

De analyses beantwoorden onder meer:

- Wat is de totale omzet, het aantal orders en de gemiddelde orderwaarde?
- Hoe evolueert omzet per maand?
- Welk land en product levert de meeste omzet op?
- Hoe maken we rommelige brondata betrouwbaar?

## Dashboard starten

\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run dashboard/app.py
\`\`\`

Open daarna de URL die Streamlit toont, meestal
\`http://localhost:8501\`.

Het dashboard bevat:

- KPI-kaarten voor omzet, orders, landen en gemiddelde orderwaarde;
- een filter op land;
- interactieve omzettrend per maand;
- interactieve omzet per product;
- een tabel met de onderliggende orders.

## Analyses en grafieken uitvoeren

\`\`\`bash
# Reinig de bewust rommelige oefendata.
python src/19_clean_data.py

# Bereken KPI's en maandelijkse omzet.
python src/21_kpis.py
python src/23_analyze_multiple_months.py

# Maak statische PNG-grafieken.
python visualizations/matplotlib_monthly_revenue.py
python visualizations/matplotlib_revenue_by_product.py

# Maak interactieve HTML-grafieken.
python visualizations/plotly_monthly_revenue.py
python visualizations/plotly_revenue_by_product.py
\`\`\`

Gegenereerde grafieken komen in \`reports/charts/\`. Die staan bewust niet in
Git: de scripts kunnen ze altijd opnieuw maken.

## PostgreSQL-lab

Wanneer PostgreSQL lokaal draait, maak je de oefendatabase en laad je de
analyse-data in:

\`\`\`bash
createdb -h 127.0.0.1 analytics_lab
psql -h 127.0.0.1 -d analytics_lab -f sql/schema.sql
psql -h 127.0.0.1 -d analytics_lab -f sql/import_sales.sql
psql -h 127.0.0.1 -d analytics_lab -f sql/queries.sql
python src/24_read_postgres.py
\`\`\`

Dit demonstreert de bedrijfsflow:

\`\`\`text
CSV → PostgreSQL → SQL → Pandas → analyse
\`\`\`

## Tests

\`\`\`bash
pytest
\`\`\`

De test controleert dat de cleaning-pipeline ongeldige en dubbele orders
verwijdert en de verwachte omzet behoudt. GitHub Actions voert dezelfde test
automatisch uit bij elke push en pull request.

## Projectstructuur

\`\`\`text
python-data-analytics-lab/
├── data/raw/              # schone, rommelige en analyse-CSV's
├── dashboard/app.py       # Streamlit-dashboard
├── sql/                   # schema, import en zakelijke SQL-queries
├── src/                   # leerlessen, cleaning en analyses
├── tests/                 # pytest-controles
├── visualizations/        # Matplotlib- en Plotly-scripts
├── .github/workflows/     # automatische GitHub-testcontrole
├── requirements.txt
└── README.md
\`\`\`

## Vaardigheden die deze repo bewijst

- Python, functies, foutafhandeling en projectstructuur;
- NumPy en basisstatistiek;
- Pandas: CSV inlezen, filtering, \`groupby\`, cleaning en datums;
- zakelijke KPI-analyse;
- Matplotlib en Plotly;
- PostgreSQL, SQL en Pandas-databaseconnecties;
- Streamlit-dashboards;
- pytest, Git en GitHub Actions.

## Leerroute

De repository is stap voor stap opgebouwd:

\`\`\`text
concept → theorie → kleine oefening → toepassen → test → Git-commit
\`\`\`

De nummering in \`src/\` laat de volledige leergeschiedenis zien, van
\`01_python_basics.py\` tot en met de PostgreSQL-naar-Pandas-flow.
