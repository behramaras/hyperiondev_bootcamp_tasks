num = int(input("Enter a number less than or equal to 100: "))

while num > 100:
    print("It's greater than 100.")
    num = int(input("Enter a number less than or equal to 100: "))

if num % 2 == 0:
    print(num*2)
    
else:
    print(num*3)
    
