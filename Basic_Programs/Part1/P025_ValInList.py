"""
Write a Python program to check whether a specified value is contained in a group of values
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

groupList=input("enter group of values by comma seperated:\n").split(",")
Val=input("enter value to check:\n")

if(Val in groupList):
    print("True")
else:
    print("False")