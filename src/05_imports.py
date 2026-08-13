"""Fase 0.4a — functies uit een ander bestand importeren.

Voer uit met: python src/05_imports.py
"""

from sales_helpers import calculate_revenue


order = {
    "product": "Shoes",
    "price": 89.99,
    "quantity": 2,
}

revenue = calculate_revenue(order["price"], order["quantity"])

print(f"Product: {order['product']}")
print(f"Omzet: €{revenue:.2f}")
