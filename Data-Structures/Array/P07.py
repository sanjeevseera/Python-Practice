"""
Write a Python program to append items from inerrable to the end of the array
"""

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))

array_num.extend(array_num)
print("New array: "+str(array_num))