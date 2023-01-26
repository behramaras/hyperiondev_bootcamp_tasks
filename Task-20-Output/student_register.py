"""
The code takes the student number information
as much as the number given as input from the user
and saves this information to the file within a for loop.
This file also contains a signature field for each student.
"""

num = int(input("How many students are registering?: "))

file = open("reg_form.txt","w")

for i in range(0,num):
    id_num = input("Enter your ID number: ")

    file.write(f"{id_num}\t=\t................\n\n")

file.close()
