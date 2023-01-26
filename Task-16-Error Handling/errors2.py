# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.



# Runtime Error: Name 'Lion' has not been defined. Lion doesn't have quotation marks.
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16


# Logical Error: There was no 'f' for format.
# Fixed with f-string.
# Logical Error: {animal_type} and {number_of_teeth} swapped.

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"


# Syntax Error: There were no parentheses.
print(full_spec)

