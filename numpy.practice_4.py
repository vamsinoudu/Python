"""
4.	Use a list of alphabets and find out the vowels from the same? Please do the same with filter method
"""
import alphabets as alphabets

A: alphabets="HelloWorld"
print(list(filter(lambda x: x in ['a','i','o','u'], alphabets)))
