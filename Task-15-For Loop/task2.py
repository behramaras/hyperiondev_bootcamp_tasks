year = int(input("What year do you want to start with?: ") )
num = int(input("How many years do you want to check?: "))

for i in range(num):
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} isn't a leap year.")

    year += 1
