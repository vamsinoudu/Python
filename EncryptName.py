"""
Write a program that asks the user to enter his/her name and then partly encrypt and display it.
Please enter your name: Jimmy

Encrypted form is J***y

"""
name = input("Please enter your name: ")
encryptName = name[0] + "*" * (len(name) - 2) + name[-1]
print("Encrypted Name is: {}".format(encryptName))
