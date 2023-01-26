kg = float(input("Enter your weight in kg: "))
m = float(input("Enter your height in m: "))

bmi = kg / (m*m)

if (bmi >= 30):
    print(f"BMİ: {bmi}\nYou're obese!")
elif (bmi >= 25):
    print(f"BMİ: {bmi}\nYou're overweight!")
elif (bmi >= 18.5):
    print(f"BMİ: {bmi}\nYou're normal!")
else:
    print(f"BMİ: {bmi}\nYou're underweight!")
