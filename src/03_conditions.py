order = {
    "product": "Jacket",
    "country": "Belgium",
    "price": 129.99,
    "quantity": 1,
}

revenue = order["price"] * order["quantity"]

if revenue >= 300:
    order_size = "groot"
else:
    order_size = "standaard"

print(f"Product: {order['product']}")
print(f"Omzet: €{revenue:.2f}")
print(f"Bestellingstype: {order_size}")