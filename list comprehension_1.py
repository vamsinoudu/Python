"""
1. Using list comprehension, construct a list from the squares
of each element in the list.

"""

s = [x ** 2 for x in range(10)]
print(s)
'''

'''
lst_1 = [1, 2, 3, 4]  # taking the number from lst_1 to lst_2
lst_2 = [x for x in lst_1]
print(lst_2)

list_3 = [x for x in range(1200, 2000, 130)]
print(list_3)
"""
3. Use list comprehension to contruct a new list
 but add 6 to each item.
"""
list_5 = [100, 200, 300, 400]
list_4 = [x + 6 for x in list_5]
print(list_4)
'''
4. Given dictionary is consisted of vehicles and their
weights in kilograms. Contruct a list of the names of vehicles
with weight below 5000 kilograms.
In the same list comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400,
 "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}


'''

dict_1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400,
          "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
lst = [i.upper() for i in dict_1 if dict_1[i] < 5000]
print(lst)
listVehicle = [key for key in dict_1.keys() if dict_1[key] < 5000]  # Second answer
print(listVehicle)

"""
5. Using list comprehension, construct a list from the squares of each
element in the list, if the square is greater than 50.

"""
number_1 = [2, 4, 6, 8, 10]
number_2 = [i ** 2 for i in number_1 if i ** 2 > 50]
print(number_2)