orders = [
    {"product": "Shoes", "price": 89.99, "quantity": 2},
    {"product": "Shirt", "price": 49.99, "quantity": 1},
    {"product": "Jacket", "price": 129.99, "quantity": 3},
]

total_revenue = 0

for order in orders:
    revenue = order["price"] * order["quantity"]
    total_revenue += revenue

    print(f"{order['product']}: €{revenue:.2f}")

print(f"Totaal omzet: €{total_revenue:.2f}")