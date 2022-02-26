"""
8.	A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.


"""
class_held = int(input("Number of classes held:"))
class_attend = int(input("Number of classes attended :"))
percentage = class_attend/class_held*100
if percentage > 75:
    print("percentage of class attended:", percentage, "%")
    print("student is allowed for exam")
else:
    print("student not allowed for exam", percentage)
