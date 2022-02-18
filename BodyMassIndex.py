# Enter your weight in (kg): 75
# Enter your height in (m): 1.70
#
# Your BMI is: 25.95
#
# You are in the “overweight” range.

weight_1 = float(input("Enter your weight in (kg) :"))
height_2 = float(input("Enter your height in (m): "))
BMI = weight_1 / height_2**2
print("your BMI is :", round(BMI,2))
if BMI < 18.5:
    print("You are in the Underweight range ")
elif 18.5 <= BMI < 24.9:
    print("You are in the Normal range")
elif 25 <= BMI < 29.9:
    print("You are in the Overweight range ")
elif BMI >= 30:
    print("You are Obese")
