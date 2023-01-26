'''
The code takes a string, counts character frequency
with the help of a for loop and prints out the frequency as a dictionary.
'''

count = {}
string = input("Enter a string: ")
letters = list(string)

for letter in set(letters):
    count[letter] = int(letters.count(letter))
    
print(count)
