shape = input("Enter the shape of the building(square, rectangular or round): ")

if (shape == "square"):
    length = int(input("Enter the length: "))
    area = length ** 2
    print(f"Area = {area}")

elif (shape == "rectangular"):
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    print(f"Area = {area}")

elif (shape == "round"):
    radius = int(input("Enter the radius: "))
    area = 3.14*(radius**2)
    print(f"Area = {area}")
    
else:
    print("Invalid definiton..")
