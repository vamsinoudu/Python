# 1.	A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
salary_details = float(input("Your salary"))
employee_details = float(input(" year of service"))
net_bonus = float(5/100 * salary_details)
if employee_details > 5:
    print("net bonus amount ",  net_bonus)
elif employee_details < 5:
    print("your not eligible")

