"""
The code takes 2 numbers from the user and returns the result according to the selected operation.

"""

# The code returns the sum of num1 and num2.

def add_num(num1, num2):

    return num1 + num2

# The code subtracts a from b and returns the result.

def subtract_num(num1, num2):

    return num1 - num2

# The code returns a times b.

def multiply_num(num1, num2):

    return num1 * num2

# The code returns the the division of a to b.

def divide_num(num1, num2):

    return num1 / num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("""
        Menu:

        Option 1 - add
        Option 2 - subtract
        Option 3 - multiply
        Option 4 - divide
""")

choise = input("Enter the option number: ")

if choise == "1":
    print(add_num(num1, num2))

elif choise == "2":
    print(subtract_num(num1, num2))

elif choise == "3":
    print(multiply_num(num1, num2))

elif choise == "4":
    print(divide_num(num1, num2))

else:
    print("Invalid option number!")
