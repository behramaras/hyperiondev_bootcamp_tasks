names = []
birthdays = []

with open("DOB.txt","r",encoding="utf-8") as file:

    for i in file:
        names.append(i.split()[:2])
        birthdays.append(i.split()[2:])

print("Name\n")       
for i in names:
    print(f"{i[0]} {i[1]}")

print("\nBirthdate\n")
for i in birthdays:
    print(f"{i[0]} {i[1]} {i[2]}")
    
