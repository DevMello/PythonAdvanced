products = [('iphone', 999),
            ('laptop', 1500),
            ('car', 25000),
            ('shoes', 120),
            ('PS5', 499),
            ('books', 35.95),
            ('shoes', 199.99),
            ('table', 150.45),
            ('tv', 899.99),
            ('lamp', 50.00),
            ('gun', 345.00)]

price = float(input("Enter a numeric price value: "))

affordable_products = [product[0] for product in products if product[1] <= price]

print("You can afford to buy the following products:")
for product in affordable_products:
    print(product)