# This code determines whether or not a string is a palindrome.

string = input("Enter a string:\n")

if string == string[::-1]:
    print("Your word is a palindrome.") 
 
else:
    print("Your word is not a palindrome.")
