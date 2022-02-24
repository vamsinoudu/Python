'''
Write a program that asks the user for two whole number Celsius values,
and then prints a Celsius/Fahrenheit conversion chart for all whole number Celsius values between (and including)
the two values entered. You can use C to F conversion formula F = C * 9/5 + 32

'''
temp_1 = int(input("Enter the first amount in Celsius:"))
temp_2 = int(input("Enter the last amount in Celsius:"))
print("CELSIUS\t\tFAHRENHEIT")

for i in range(temp_1, temp_2 + 1):
    formula = i * 9 / 5 + 32
    print(i, "\t\t", formula)

