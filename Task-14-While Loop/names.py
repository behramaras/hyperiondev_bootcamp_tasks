name = input("Enter the names of all pupils in a class, write  'Stop' to exit: ")
counter = 0

while name.lower() != "stop":
    counter += 1
    name = input("Enter the names of all pupils in a class, then 'Stop' to stop: ")

print(f"Total number of students is {counter}.")
