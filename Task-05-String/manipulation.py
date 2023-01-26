#This code takes a sentence from the user.

str_manip = input("Enter a sentence:")

#This code calculates and displays the length of "str_manip".

length = len(str_manip)

print(f"The length of str_manip is {length}.")

#This code finds the last letter in str_manip. 
#And replaces every occurrence of this letter in "str_manip" with '@'.

the_letter = str_manip[-1]

rep_str = str_manip.replace(the_letter,"@")

print(rep_str)

#This code prints the last 3 characters in "str_manip" backwards.

last3 = str_manip[-1:-4:-1]

print(last3)

#This code creates a five-letter wordt
#That is made up of the first three characters and the last two characters in "str_manip".

part1 = str_manip[0:3]

part2 = str_manip[-2:]

new_word = (f"{part1}{part2}") 

print(new_word)
