"""Fase 0.4b — een tekstbestand veilig lezen.

Voer uit met: python src/06_read_file.py
"""

file_path = "data/raw/products.txt"

# with sluit het bestand automatisch nadat we klaar zijn.
with open(file_path, encoding="utf-8") as file:
    products = file.read().splitlines()

for product in products:
    print(f"- {product}")

print(f"Aantal producten: {len(products)}")
