#The code stores all entered strings until string can be 'John'. Then, print outs the list of incorrect names.

name = input("Enter your name:\n")
name_list = []

while name.lower() != "john":
    name_list.append(name.title())
    name = input("Enter your name:\n")

print(f"Incorrect names: {name_list}")
