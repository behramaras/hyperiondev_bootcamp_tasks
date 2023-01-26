# In task 1, the code counts the number of characters in the file.
# In task 2, the code counts the number of words in the file.
# In task 3, the code counts the number of lines in the file.
# In task 4, the code counts the total number of vowels (a, e, i, o and u) in the file.


with open("input.txt","r",encoding="utf-8") as file:
    
    print("******************Task 1******************\n")
    all_file = file.read()
    characters = 0
    
    for i in all_file:
        characters +=1
    print(f"The number of characters: {characters}")
    
    print("\n******************Task 2******************\n")
    
    words = all_file.split()

    print(f"The number of words: {len(words)}")
        
    print("\n******************Task 3******************\n")
    file.seek(0)
    line = file.readlines()
    lines = 0
    
    for i in line:
        lines += 1
    print(f"The number of lines: {lines}")

    print("\n******************Task 4******************\n")
    total = all_file.count("a")+all_file.count("e")+all_file.count("i")+all_file.count("0")+all_file.count("u")
    print(f"The total number of vowels (a, e, i, o and u): {total}")
