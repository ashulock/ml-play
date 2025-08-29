prices = {"laptop": 55000, "phone": 25000, "tablet": 18000}
product = max(prices, key=prices.get)
print(product)