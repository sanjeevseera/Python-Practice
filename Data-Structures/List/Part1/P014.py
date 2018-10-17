"""
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""

lists=[1,2,3,4,5,6,7,8,9,10,12,14,13,15,17]

lists=[x for x in lists if x%2!=0]
print(lists)