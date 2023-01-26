# This code displays count down from 20 to 0.

print("***********Task 1***********")
i = 20

while i >= 0:
    print(f"i: {i}")
    i -= 1


# This code displays all the even numbers between 1 and 20.

print("***********Task 2***********")
for i in range(1,21):
    if i % 2 == 0:
        print(i)

# This code creates a loop that use "*".

print("***********Task 3***********")

show = "*"
for i in range(1,6):
    print(i*"*")


# This code computes the greatest common divisor of two positive integers.

print("***********Task 4***********")

num_1 = int(input("Enter a positive number: "))
num_2 = int(input("Enter a positive number: "))

num1_list = list()
common = list()

for i in range(1,num_1+1):
    if num_1 % i == 0:
        num1_list.append(i)

for i in num1_list:
    if num_2 % i == 0:
        common.append(i)

print(sorted(common)[-1])
