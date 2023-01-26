'''
The code takes 'keys' from the menu list, with a for loop.
And calculates the total stock worth in a cafe with the related
values from stocks and prices dictionaries.
'''

menu = ["tea", "coffee", "sugar", "milk"]
stocks = {"tea": 100, "coffee": 50, "sugar": 60, "milk": 70}
prices = {"tea": 3, "coffee": 4, "sugar": 1, "milk": 1}

stocks_worth = 0

for i in menu:
    stocks_worth += stocks[i] * prices[i]

print(f"Total stock worth: {stocks_worth} £")
