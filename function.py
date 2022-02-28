# feb 28
# functions
"""
Take the input from user and build the calculator as per user requirements?

"""


def add(number1, number2):
    add = number1 + number2
    return add


def sub(number1, number2):
    sub = number1 - number2
    return sub


def mult(number1, number2):
    mult = number1 * number2
    return mult


def div(number1, number2):
    div = int(number1 / number2)
    return div


number1 = int(input("enter the numbers:"))
number2 = int(input("enter the numbers:"))

choice = int(input("press 1 for add,press 2 for sub,press 3 for mult,press 4 for div:"))
if choice == 1:
    result = add(number1, number2)
    print(result)

elif choice == 2:
    result = sub(number1, number2)
    print(result)

elif choice == 3:
    result = mult(number1, number2)
    print(result)

elif choice == 4:
    result = div(number1, number2)
    print(result)

else:
    print("not valid")
