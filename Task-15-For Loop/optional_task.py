num = int(input("Enter a number: "))

if num > 10:
    for i in range(num):
        print(f"{i+1}. {num}")

if num <= 10:
    print("Sorry, too small")
