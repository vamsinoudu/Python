"""
4.	A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity Suppose, one unit will cost 100.
Judge and print total cost for user.

"""
# solution:
customer = int(input("Cost of purchased quantity :"))
discount = customer * 10/100
if customer > 1000 :
    print("your discount price is ", discount)
else:
    print(" sorry your ticket price not reached above 1000 INR. ")
