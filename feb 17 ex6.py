"""
6.	Take input of the age of 3 people by user and determine oldest and youngest among them.

"""

Ram = int(input(" Ram Enter your age :"))
Gopi = int(input("Gopi Enter your age :"))
Raj = int(input(" Raj Enter your age :"))

if Ram > Gopi and Ram > Raj:
    print("Ram is Older")
elif Gopi > Ram and Gopi > Raj:
    print(" Gopi is older ")
else:
    print("Raj is older")
if Ram < Gopi and Ram < Raj:
    print("Ram is younger")
elif Gopi < Ram and Gopi < Raj:
    print("Gopi is younger")
else:
    print("Raj is younger")

