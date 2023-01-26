num = int(input("Enter a number or '-1' to stop: "))
counter = 0
total = 0

while num != -1:
    
    counter += 1
    total += num
    num = int(input("Enter a number or '-1' to stop: "))

print(f"The average of the numbers is {total/counter}")

