string = input("Enter a string:\n")
disappear = input("Which characters you would like to make disappear:\n")

for i in disappear.split(","):
    string = string.replace(i,"")
    
print(string)
