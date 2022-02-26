"""
11.	Write a Python program to convert temperatures to and from celsius, fahrenheit
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

"""
celsius = float(input("Enter the temperature in celsius:"))
celsiusToFahrenheit = celsius*9/5 + 32
print(celsius,  "°C is",  celsiusToFahrenheit,  "in Fahrenheit")

fahrenheit = float(input("Enter the temperature in fahrenheit:"))
fahrenheitToCelsius = (fahrenheit - 32)*5/9
print(fahrenheit,   "°F is",    round(fahrenheitToCelsius,  2),   "in celsius")



