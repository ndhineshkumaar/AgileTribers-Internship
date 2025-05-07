items = [
    ("Apples", 1.50),
    ("Bananas", 0.99),
    ("Cherries", 3.75),
    ("Dates", 2.50),
    ("Eggplant", 1.25)
]

itemwidth = 15
pricewidth = 10

print("Item".ljust(itemwidth) + "Price".rjust(pricewidth))
print("-" * (itemwidth + pricewidth))

for item, price in items:
    itemstr = item.ljust(itemwidth)
    pricestr = f"${price:.2f}".rjust(pricewidth)
    print(itemstr + pricestr)
