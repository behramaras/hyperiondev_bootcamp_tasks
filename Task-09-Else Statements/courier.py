price = int(input("Enter the price of the package they would like to purchase: "))
distance = int(input("Enter the total distance of the delivery in kms: "))
extra = 0

choose = input("Would you prefer an air delivery or freight delivery: ")

if (choose == "air"):
    distance *= 0.36

else:
    distance *= 0.25
    
insruance = input("Do you want an insurance?(yes or no): ")

if (insruance == "yes"):
    extra += 50

else:
    extra += 25
    
gift = input("It is a gift?(yes or no): ")

if (gift == "yes"):
    extra += 15

else:
    pass

delivery = input("Do you want a priority or standart delivery?: ")

if (delivery == "priority"):
    extra += 100

else:
    extra += 20

total = price + distance + extra

print(f"Cost of the package: {total}")
