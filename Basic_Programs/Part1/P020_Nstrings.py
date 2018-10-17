"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string
"""

str,n=input("enter the string and number by comma seperated:\n").split(",")

print("larger string: %s" %(str*int(n)))