# Assertions:
# python provide the Assert statement to check the logical expression True or False.
# Programme will execution when the statement only True ,otherwise it will show Assertion error when it is False.
# The following code shows the usage of assertion statement.

# Example:
try:
    num = int(input("Enter the number:"))
    assert num % 2 == 0
    print("printed number is", num, "even number")
except AssertionError:
    print("please enter the even number .")
