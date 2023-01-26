side1 = int(input("Enter the length for one side of the triangle: "))
side2 = int(input("Enter the length for one side of the triangle: "))
side3 = int(input("Enter the length for one side of the triangle: "))

semi = (side1+side2+side3)/2

area = (semi*(semi-side1)*(semi-side2)*(semi-side3))**0.5

print(f"Area = {area}")
