"""
A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
An example run of the program (numbers in bold are typed in by the user)

Enter your age: 63
Your ticket costs £2.00
"""
Age = int(input("Enter your age :"))
full_price = 6
half_price = 3
third_price = 2
if Age <= 16:
    print("your ticket costs £ :",  half_price)
elif Age > 60:
    print("your ticket costs £ :",  third_price)
else :
    print("your ticket costs £ :",  full_price)
print(Age)


