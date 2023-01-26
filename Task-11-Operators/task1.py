num1 = 119
num2 = 14
num3 = 370
largest = 0
middle = 0
smallest = 0

#This code compares num1 and num2 and display the larger value.

if (num1 > num2):
    print(f"{num1} and {num2} are comparing...\nThe larger value is {num1}")
else:
    print(f"{num1} and {num2} are comparing...\nThe larger value is {num2}")

#This code displays that num1 is odd or even.
    
if (num1 % 2 == 0):
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

#This code finds the smallest number:   
if (num1 < num2 and num1 < num3):
    smallest = num1
elif (num2 < num1 and num2 < num3):
    smallest = num2
elif (num3 < num1 and num3 < num2): 
    smallest = num3

#This code finds the largest number:   
if (num1 > num2 and num1 > num3):
    largest = num1
elif (num2 > num1 and num2 > num3):
    largest = num2
elif (num3 > num1 and num3 > num2): 
    largest = num3

#This code finds the middle number:   
if (num1 < num2 and num1 > num3) or (num1 > num2 and num1 < num3):
    middle = num1
elif (num2 < num1 and num2 > num3) or (num2 > num1 and num2 < num3):
    middle = num2
else:
    middle = num3

#Sort numbers:
print(largest,middle,smallest)
