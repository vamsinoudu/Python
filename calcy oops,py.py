"""
Write a python program to make a calculator using the concept of classes, objects and functions.
 The calculator software should give options to the user and based on the input from the user, the operation, must be performed.

A Sample run is:

"""


class calculator():
    def __init__(self):
        self.value_1 = "x"
        self.value_2 = "x"

    def addition(self):
        addition = value_1 + value_2
        print("Answer is ", addition)

    def subtraction(self):
        subtraction = value_1 - value_2
        print("Answer is ", subtraction)

    def multiplication(self):
        multiplication = value_1 * value_2
        print("Answer is ", multiplication)

    def division(self):
        division = value_1 / value_2
        print("Answer is ", int(division))


value_1 = int(input("Enter the number:"))
value_2 = int(input("Enter the number :"))

obj = calculator()
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
