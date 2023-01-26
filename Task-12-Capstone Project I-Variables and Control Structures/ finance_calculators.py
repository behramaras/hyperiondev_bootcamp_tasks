"""
This program allows the user to calculate their interest on an investment or
calculate the amount that should be repaid on a home loan each month.

"""
# The invesment depends on type of interest which it can be simple or compound.
# If the user enters "q", program will stop.

import math

while True:

    choose = input("""Choose either 'investment' or 'bond' from the menu below to proceed or 'q' to quit:

investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
""")

    choose = choose.lower()
    
    if choose == "q":
        break

    elif (choose != "investment") and (choose != "bond"):
        print("Invalid input!\n")

    elif choose == "investment":
        deposite = int(input("Enter the amount of money that you are depositing: "))
        rate = int(input("Enter the interest rate: ").strip("%"))
        year = int(input("Enter the number of years you plan on investing: "))
        interest = input("Do you want a 'simple' or a 'compound' interest: ").lower()

        if (interest != "simple") and (interest != "compound"):
            print("Invalid input!\n")

        elif interest == "simple":
            total = deposite * (1+((rate/100) * year))
            print(f"Total amount: {total:.2f}\n")
    
        else:
            total = deposite * math.pow((1+rate/100),year)
            print(f"Total amount: {total:.2f}\n")

    else:
        house_value = int(input("Enter the present value of the house: "))
        rate = int(input("Enter the interest rate: ").strip("%"))
        months = int(input("Enter the number of months you plan to take to repay the bond: "))

        repayment = ((rate/12) * house_value) / (1- math.pow(1+(rate/12),(-months)))

        print(f"Total repayment: {repayment:.2f}\n")
    
