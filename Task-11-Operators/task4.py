num = int(input("Enter a whole number: "))

if (num % 2 == 0) and (num % 5 == 0):
    print(f"{num} can divisible by 2 and 5.")
elif (num % 2 == 0) or (num % 5 == 0):
    print(f"{num} can divisible by 2 or 5.")
else:
    print(f"{num} can not divisble by 2 or 5.")
