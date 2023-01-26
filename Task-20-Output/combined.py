'''
In the first 2 blocks of codes, numbers1.txt (contains odd numbers from 1 to 100) and

numbers2.txt (contains even numbers from 1 to 100) files are created.

Then these numbers are read, united and wrote in a new all_numbers.txt file, sequentially.

'''


with open("numbers1.txt","w+") as num1: 
    for i in range(1,101):
        if i % 2 != 0:
            num1.write(f"{i}\n")

with open("numbers2.txt","w+") as num2:
    for i in range(1,101):
        if not i % 2:
            num2.write(f"{i}\n")


all_list = []

num1 = open("numbers1.txt","r")
for i in num1.readlines():
    all_list.append(int(i.replace('\n','')))
        
num2 = open("numbers2.txt","r")
for i in num2.readlines():
    all_list.append(int(i.replace('\n','')))

all_num = open("all_numbers.txt","w+")

for i in sorted(all_list):
    all_num.write(str(i) + '\n')



num1.close()
num2.close()
all_num.close()

