"""
The code adds math, time and median moduls.

Then it takes 10 numbers from the user with a for loop and adds them to a list.

And it prints the code's results 1 second apart thanks to the added time module.
"""

from statistics import median
import math
import time

num_list = []

for i in range(1, 11):
    value = float(input(f"Enter {i}. number: "))
    num_list.append(value)

# The sum of all values taken ​​from the user is calculated with math module and printed out.
    
total = math.fsum(num_list)
print(f"\nThe total of all the numbers: {total}\n")
time.sleep(1)

# The maximum number ​in the list is found using max() built-in function and printed out.

max_num = max(num_list)
max_index = num_list.index(max_num)

print(f"The maximum number: {max_num} at index {max_index} in the list.\n")
time.sleep(1)

# The minimum number ​in the list is found using min() built-in function and printed out.

min_num = min(num_list)
min_index = num_list.index(min_num)

print(f"The minimum number: {min_num} at index {min_index} in the list.\n")
time.sleep(1)

# The average of the numbers calculated and printed as a rounded off to 2 decimal places using round() built-in function.

avarage = total/len(num_list)
round_2 = round(avarage,2)

print(f"The average of the numbers: {round_2}\n")
time.sleep(1)

# The median number ​in the list is found using median() function from statistics modul and printed out.

median_num = median(num_list)
print(f"The median number: {median_num}\n")
time.sleep(1)
