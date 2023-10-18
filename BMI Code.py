Weight = int(input("Enter your weight in Kgs: "))
Height = float(input("Enter your Height in meters : "))

print()
BMI = Weight/(Height**2)
print(BMI)
print()

if BMI < 18.5 :
    print("Underweight Sir")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal BMI , Good ")
else :
    print("Overweight Sir ")
