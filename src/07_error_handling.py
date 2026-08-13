"""Fase 0.4c — een verwachte fout begrijpelijk afhandelen.

Voer uit met: python src/07_error_handling.py
"""

file_path = "data/raw/missing_products.txt"

try:
    with open(file_path, encoding="utf-8") as file:
        products = file.read().splitlines()

    print(products)

except FileNotFoundError:
    print(f"Bestand niet gevonden: {file_path}")
