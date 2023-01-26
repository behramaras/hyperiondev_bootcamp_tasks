"""
The code creates a dictionary including abbreviations and meanings.
Then two more abbreviations and meanings are added. Then an abbreviation is taken from user.
If is exists in the abbreviations dictionary it prints out the abbreviation and its meaning.
If not prints a 'not found' message.
"""
abbreviations = {
    "API": "Application Programming Interface",
    "IDE": "Integrated Development Environment",
    "SDK": "Software Development Kit",
    "SSH": "Secure Shell",
}

abbreviations["UX"] = "User Experience"
abbreviations["UI"] = "User Interface"

given = input("Enter an abbreviation: ").replace(".","").upper()

if given not in abbreviations:
    print("Abbreviation not found!")

else:
    print(f"{given}: {abbreviations[given]}")
