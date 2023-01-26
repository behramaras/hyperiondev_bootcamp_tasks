prod_1 = input("Enter a product name: ")
prod_2 = input("Enter a product name: ")
prod_3 = input("Enter a product name: ")

price_1 = float(input(f"How much is the price of the {prod_1}?: "))
price_2 = float(input(f"How much is the price of the {prod_2}?: "))
price_3 = float(input(f"How much is the price of the {prod_3}?: "))

price_1 = float("{:.2f}".format(price_1))
price_2 = float("{:.2f}".format(price_2))
price_3 = float("{:.2f}".format(price_3))

total = price_1+price_2+price_3

average = round(total/3,2)

print(f"The Total of {prod_1}, {prod_2}, {prod_3} is {total} and the average price of the items is {average}.")
