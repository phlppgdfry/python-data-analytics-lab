# Python Data Analytics Lab

Een groeiend end-to-end data-analyseproject. We leren telkens één concept,
oefenen het klein, passen het toe in deze repository en leggen het vast met Git.

## Huidige fase: 0 — Python-basis

We beginnen met precies de Python die je voor data-analyse nodig hebt:

- variabelen en basistypes
- strings, lists en dictionaries
- voorwaarden en lussen
- functies, imports en bestanden
- virtual environments en packages

Daarna voegen we stap voor stap NumPy, Pandas, data cleaning, analyses,
visualisaties, SQL en een dashboard toe.

## Zo werken we

```text
CONCEPT → theorie → mini-oefening → toepassen in het lab → Git-commit
```

Je hoeft niets vooraf uit het hoofd te leren. Bij elke stap leggen we eerst uit
wat het is, waarom het bestaat en wanneer je het gebruikt.

## Lokaal starten

```bash
python3 -m venv .venv
source .venv/bin/activate
python src/01_python_basics.py
```

Op Windows activeer je de omgeving met:

```powershell
.venv\Scripts\Activate.ps1
```

## Eerste les — 0.1: variabelen, getallen en functies

Open `src/01_python_basics.py` en voer het bestand uit. Het laat zien hoe je
waarden in variabelen bewaart en omzet berekent met een functie.

De mini-oefening is: voeg zelf een product toe door een prijs, hoeveelheid en
berekende omzet te maken.

## Projectstructuur (vandaag)

```text
python-data-analytics-lab/
├── data/       # toekomstige ruwe en verwerkte gegevens
├── src/        # Python-code en kleine lessen
├── tests/      # automatische controles, later toegevoegd
├── README.md
└── requirements.txt
```

## Leerlog

| Stap | Onderwerp | Status |
| --- | --- | --- |
| 0.1 | Variabelen, getallen en functies | Klaar |
| 0.2 | Strings, lists en dictionaries | Klaar |
| 0.3a | Voorwaarden (`if` / `else`) | Klaar |
| 0.3b | Lussen (`for`) | Klaar |
| 0.4a | Imports en herbruikbare functies | Klaar |
| 0.4b | Bestanden lezen en schrijven | Klaar |
| 0.4c | Fouten afhandelen | Klaar |
| 1.1 | NumPy-arrays en vectorization | Klaar |
| 1.2 | NumPy-basisstatistiek | Klaar |
| 1.3 | Indexing, slicing en filtering | Klaar |
| 2.1 | Pandas en DataFrames | Klaar |
| 2.2 | CSV-bestanden inlezen | Klaar |
| 2.3 | Kolommen berekenen en selecteren | Klaar |
| 2.4 | Rijen filteren | Klaar |
| 2.5 | Groeperen en samenvatten met `groupby` | Klaar |
| 2 | Pandas en CSV | Gepland |
| 3 | Data cleaning | Gepland |
| 4 | Zakelijke analyse en KPI's | Gepland |
| 5 | Matplotlib | Gepland |
| 6 | Plotly | Gepland |
| 7 | PostgreSQL en SQL | Gepland |
| 8 | Streamlit-dashboard | Gepland |
