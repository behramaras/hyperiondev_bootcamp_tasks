name = input("Enter your full name: ")

if len(name) == 0:
    print("You haven’t entered anything. Please enter your full name.")

if 0 < len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
    
if len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

if 4 <= len(name) <= 25:
    print("Thank you for entering your name.")
