# Write a program that reads an integer value from the user and prints output whether it is odd or even.
# Enter a number: 13
# 13 is “even”

#  EvenOddNumbers.py

number_1 = int(input("Enter a number : "))
if number_1 % 2 == 0:
    print(" even")
else:
    print("odd")
print(number_1)