"""
5.	A school has the following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

"""
students = float(input("Enter your marks :"))
if students < 25:
    print("F")
elif 25 <= students <= 45:
    print("E")
elif 45 <= students <= 50:
    print("D")
elif 50 <= students <= 60:
    print("C")
elif 60 <= students <= 80:
    print("B")
elif students > 80:
    print("A")


