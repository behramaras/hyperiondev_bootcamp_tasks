# This function returns all the days of the week.

def days():
    return "Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday"


"""
This function takes a sentence from the user as a data.

Splits the data and adds it to a list.

Changes the index 1 in the list with "Hello".

Reunites the elements of the list as a new sentence and returns it.
"""

def second_word():

    data = input("\nPlease enter a sentence with at least 2 words: ")

    new_data = data.split(" ")

    new_data[1] = "Hello"

    changed_data = " ".join(new_data)
    
    return changed_data

print(days())
print(second_word())
    


