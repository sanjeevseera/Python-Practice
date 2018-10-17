"""
Write a Python program to remove a specified item using the index from an array
"""

from array import *
array_num = array('i', [4, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.pop(1) # .insert(index, values)
print("New array: "+str(array_num))

