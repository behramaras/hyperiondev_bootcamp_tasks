"""This code makes each alternate character an uppercase character
and each other alternate character a lowercase character."""

string = "Hello World"
new_string = [] 

for i in range(len(string)):
    if not i%2:
        new_string.append(string[i].upper())
    else:
        new_string.append(string[i].lower())

print("".join(new_string))
              
        
#This code makes each alternate word lower and upper case.

string = "I am learning to code"
pieces = string.split(" ")
new_string = []

for i in range(len(pieces)):
    if i%2:
        new_string.append(pieces[i].upper())
    else:
        new_string.append(pieces[i].lower())

print(" ".join(new_string))
              
        
    
    
