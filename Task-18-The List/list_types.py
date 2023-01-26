friends_names = ["Mehmet Kaya","Ali Yilmaz","Selman Ozturk"]

# This code writes the name of the first friend.
print("\n***********Task 1***********\n")
print(friends_names[0])

# This code writes the name of the last friend.
print("\n***********Task 2***********\n")
print(friends_names[-1])

# This code writes the length of the list.
print("\n***********Task 3***********\n")
print(len(friends_names))

# This code writes the age of friends.
print("\n***********Task 4***********\n")
friends_ages = [25,27,32]

for i in range(len(friends_names)):
    print(f"{friends_names[i]} is {friends_ages[i]} years old.")
