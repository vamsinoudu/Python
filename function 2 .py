# function
"""
BMI calculator
"""
name1 = 'joga'
weight_kg1 = 75
height_m1 = 1.70
name2 = 'bogo'
weight_kg2 = 68
height_m2 = 2


def bmi_calculator(name, weight_kg, height_m):
    bmi = weight_kg / height_m ** 2
    print("BMI IS:", end=" ")
    print(bmi)
    if bmi < 18:
        return name + " is normal"
    else:
        return name + "is over weight "


result1 = bmi_calculator(name1, weight_kg1, height_m1)
print(result1)
result2 = bmi_calculator(name2, weight_kg2, height_m2)
print(result2)

# km = convert(miles)
# 1 km = 0.62137 miles


run_km = int(input("enter the kilometers:"))
one_mile = 0.62


def mile(run_km, one_mile):
    mile = run_km * one_mile
    return mile


result = mile(run_km, one_mile)
print(result, "in miles")
