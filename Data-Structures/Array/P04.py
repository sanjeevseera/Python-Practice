"""
Write a Python program to get the length in bytes of one array item in the internal representation. 
"""

from array import *
array_num = array('u', ['1', '3', '5', '7', '9'])
array_num1 = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Length in bytes of one array item: "+str(array_num.itemsize))
print("Length in bytes of one array item: "+str(array_num1.itemsize))