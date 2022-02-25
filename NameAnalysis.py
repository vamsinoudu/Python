"""
To pass this exercise you must demonstrate that you are able to

Write a program that asks the user to enter his/her full name and the program process and manipulate the text of his/her name.

Your full name is PETER CAMBRIDGE
"""
Name = input("Please enter your first name: ")
last_name = input("Please enter your last name:")
print("Your full name is ", Name, last_name)
print("Your initials are", Name[0], last_name[0])
print("First name length is", len(Name))
print("Last name length is", len(last_name))
print("Full name length is ", len(Name) + len(last_name))
print("First name starts with", Name[0])
print("First name ends with", Name[4])
print("Last name starts with", last_name[0])
print("Last name ends with", last_name[-1])
print("First name indexes are 0-", len(Name) - 1)
print("Last name indexes are 0-", len(last_name) - 1)
print("First name trims", Name[0:3])
print("First name trims", Name.strip("p"))
print("Last name trims", last_name[0:3])
print("Last name trims", last_name.strip("cam"))
