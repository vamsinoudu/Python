"""
9.	Modify the above question to allow student to sit if he/she has medical cause.
 Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly

"""


person = input("Do you have a medical cause?")
if person.lower() == 'yes':
    print("Not allowed")
elif person.lower() == 'no':
    print("Allowed")

