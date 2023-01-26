fav_rest = input("Enter your favourite restaurant:")
print(f"Your favourite restaurant is {fav_rest}.")

int_fav = input("Enter your favourite number:")
print(f"Your favourite number is {int_fav}.")

"""The code below returns an error.
Integers are detected the presence of digits or other whole numbers.
number_fav_rest is not in base 10."""

number_fav_rest = int(fav_rest)
print(number_fav_rest)
