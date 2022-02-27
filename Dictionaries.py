# dictionaries

symbol_to_name = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithum",
    "C": "carbon",
    "O": "Oxygen",
    "N": "Nitrogen"

}
print(symbol_to_name.keys())
print(symbol_to_name.values())
(symbol_to_name.update({"p": "phosphorus", "S": "sulphur"}))
print((symbol_to_name.update({"p": "phosphorus", "S": "sulphur"})))
print(symbol_to_name)
print(symbol_to_name.items())
del symbol_to_name["C"]
print(symbol_to_name)

# Roll number projects
student_details = {
    "shiva": "num23",
    "Om": "num24",
    "Cathode": "num25",
}
print(student_details)
print(student_details.keys())
print(student_details.values())
student_details.update({"gani": "num27", "ph-ani": "num29"})
print(student_details)
print(student_details.items())
del student_details["Om"]
print(student_details)
