# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.



# Syntax Error: There were no parentheses.
print("Welcome to the error program")


# Syntax Error: There were no parentheses.
# Syntax Errors: There were incorrect indentations.

print("\n")


# Runtime Error: Name 'ageStr' which has not been defined.
# Deleted the "=" to fix the definition.
# Runtime Error: Performing an operation on incompatible types. Deleted "years old" to fix conversion.

ageStr = "24" #I'm 24 years old.
age = int(ageStr)

# Runtime Error: Performing an operation on incompatible types.
# Name age is an integer, the age and ageStr swapped. 

print("I'm " + ageStr + " years old.")


# Syntax Error: There were quotation marks.
three = 3

answerYears = age + three


# Syntax Error: There were no parentheses.
# Logical Error: Even if there is no error, user observing the variable name rather than number.
# Fixed with f-string.

print(f"The total number of years: {answerYears}")

# Runtime Error: Using an identifier (answer) which has not been defined.
# Used answerYears instead.
answerMonths = answerYears * 12


# Syntax Error: There were no parentheses.
# Runtime Error: Performing an operation on incompatible types. The name answerMonths is an integer.
# Fixed with f-string.
# Logical Error: The answer was missing 6 months.
print(f"In 3 years and 6 months, I'll be {answerMonths + 6} months old")



#HINT, 330 months is the correct answer

