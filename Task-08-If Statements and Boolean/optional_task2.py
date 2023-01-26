temperature = True
weekend = True
sunny = True

query_temperature = input("Is the temperature greater than 20 degrees?(Yes or No)")
query_weekend = input("Is the weekend?(Yes or No)")
query_sunny = input("Is it sunny?(Yes or No)")

if query_temperature == "No":
    temperature = False

if query_weekend == "No":
    weekend = False

if query_sunny == "No":
    sunny = False
    
if temperature == True:
    top = "a short-sleeved shirt"

if temperature == False:
    top = "a long-sleeved shirt"

if weekend == True:
    bottom = "a short"

if weekend == False:
    bottom = "a jean"

if sunny == True:
    take = "a cap"

if sunny == False:
    take = "a raincoat"

print(f"You should wear {top}, {bottom} and {take}.")

