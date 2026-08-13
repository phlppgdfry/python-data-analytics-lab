products = ["Shoes", "Shirt", "Jacket"]

order = {
      "product": "Jacket",
      "price": 129.99,
      "quantity": 3,
      "country": "Belgium",
  }

revenue = order["price"] * order["quantity"]

print(f"Product: {order['product']}")
print(f"Omzet: €{revenue:.2f}")
print(f"Eerste product in de lijst: {products[0]}")
print(f"Land: {order['country']}")