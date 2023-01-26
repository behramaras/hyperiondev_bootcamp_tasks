# 'k' which is in the print changed as 'key'.

def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Added "\" in 'd'oh'.

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd\'oh', "maggie": " (Pacifier Suck)"}

# 'lisa', 'bart', 'homer' are all put on a list together.
# Because, print_values_of() takes 2 arguments.

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

