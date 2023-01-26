print("Welcome to the monthly wage program")

position = input("Are you a salesperson or a manager?: ")

if (position == "salesperson"):
    gross_sales = int(input("How much is your gross sales for the month?: "))
    print(f"Total monthly wage: {2000+((gross_sales*8)/100)}")

else:
    hours = int(input("What is your the number of hours worked for the month?: "))
    print(f"Total monthly wage: {hours*40}")
