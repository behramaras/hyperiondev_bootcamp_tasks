"""
The code reads every line in input.txt depending on whether it contains min, max, avg words.
Extracts the data from the line with min, max, avg words and assigns them to a list as an integer and
send it to the corresponding function. Writes the results to output.txt.

"""

#The code returns the minimum number of the list.

def num_min(file_list):

    return f"The min of {file_list} is {min(file_list)}"

#The code returns the maximum number of the list.
def num_max(file_list):

    return f"The max of {file_list} is {max(file_list)}"

#The code returns the average number of the list.

def avg(file_list):

    total = 0
    for i in file_list:
        total += i

    return f"The avg of {file_list} is {total/len(file_list)}"


input_file = open ("input.txt", "r", encoding="utf-8-sig")

for i in input_file:
    if i.startswith("min"):
        i = i.strip("min:")
        i = i.strip("\n")
        list_min = [eval(i) for i in i.split(",")]
    
    elif i.startswith("max"):
        i = i.strip("max:")
        i = i.strip("\n")
        list_max = [eval(i) for i in i.split(",")]
        
    else:
        i = i.strip("avg:")
        i = i.strip("\n")
        list_avg = [eval(i) for i in i.split(",")]
        

output_file = open ("output.txt", "w+", encoding="utf-8")

output_file.write(num_min(list_min) + "\n")
output_file.write(num_max(list_max) + "\n")
output_file.write(avg(list_avg) + "\n")

input_file.close()
output_file.close()
