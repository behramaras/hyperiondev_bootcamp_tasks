"""
This code provides the user with a simple calculator. This calculator can add, subtract, divide and multiply.
The user enters two numbers and operations to perform the calculation.
Calculations made according to the entered values are printed to a file and also displayed as output.
These values are also printed in another file whose name is taken from the user.
If the user wants, he can read the processes from this file, which he has chosen the file's name himself.
OOP is used in every step in the code that requires selection and in the file name received from the user.
And a suitable text is shown.

"""

# 'time' module has been added to make the program more realistic.
# When outputting with time.sleep(1), the program runs every 1 second.

import time
print("*********************************\n\tWelcome to The Calculator")

while True:

    option = input("""
1- Enter two numbers and an operator
2- Read all of the equations from a new txt file 
Enter 1 or 2 or 0 to quit: """)

    if option == "0":
        break

    elif option == "1":

        with open("calculator.txt", "a") as file:
            pass

        try:
            num_1 = float(input("Enter a number: "))
            num_2 = float(input("Enter a number: "))
            operation = input("Enter the operation(+, -, x, /) or O to quit: ")

            if operation == "0":
                break

            elif operation == "+":
                result = num_1 + num_2
                with open("calculator.txt", "a") as file:
                    file.write(f"{num_1} {operation} {num_2} = {result}\n")
                print(f"Result: {result}")

            elif operation == "-":
                result = num_1 - num_2
                with open("calculator.txt", "a") as file:
                    file.write(f"{num_1} {operation} {num_2} = {result}\n")
                print(f"Result: {result}")

            elif operation == "x":
                result = num_1 * num_2
                with open("calculator.txt", "a") as file:
                    file.write(f"{num_1} {operation} {num_2} = {result}\n")
                print(f"Result: {result}")

            elif operation == "/":
                result = num_1 / num_2
                with open("calculator.txt", "a") as file:
                    file.write(f"{num_1} {operation} {num_2} = {result}\n")
                print(f"Result: {result}")

            else:
                print(f"\nPlease enter an invalid operation. The operation was: {operation}")

        except ZeroDivisionError:
            print("\nA number cannot be divided by zero!")

        except ValueError:
            print("\nPlease enter a number!")

    elif option == "2":
        while True:
            try:
                file_name = input("\nEnter a file name: ")
                first_file = open("calculator.txt", "r")
                second_file = open(f"{file_name}", "w+")
                print(f"{file_name}.txt file created.\nContent:")

                for line in first_file:
                    line = line[:-1]
                    second_file.write(line + "\n")

                second_file.seek(0)

                for new_line in second_file:
                    time.sleep(1)
                    print(new_line)

                first_file.close()
                second_file.close()

            except FileNotFoundError:
                print("Invalid file name entered!")

    else:
        print("Invalid option. Please choose 1 or 2!")
