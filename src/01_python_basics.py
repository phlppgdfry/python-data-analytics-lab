"""Fase 0.1 — variabelen, getallen en functies.

Voer uit met: python src/01_python_basics.py
"""


def calculate_revenue(price, quantity):
    """Bereken omzet: prijs per stuk × aantal stuks."""
    return price * quantity


# Een variabele geeft een waarde een duidelijke naam.
shoe_price = 89.99
shoe_quantity = 2

# We roepen de functie aan met de prijs en hoeveelheid.
shoe_revenue = calculate_revenue(shoe_price, shoe_quantity)

print(f"Omzet schoenen: €{shoe_revenue:.2f}")


# Mini-oefening 0.1
#
# 1. Maak twee variabelen voor de prijs en hoeveelheid van een jas.
# 2. Gebruik calculate_revenue om de omzet te berekenen.
# 3. Print het resultaat op dezelfde manier als hierboven.
#
# Tip: begin bijvoorbeeld met jacket_price = 129.99.


jacket_price = 129.99
jacket_quantity = 3
jacket_revenue = calculate_revenue(jacket_price, jacket_quantity)

print(f"Omzet jas: €{jacket_revenue:.2f}")
