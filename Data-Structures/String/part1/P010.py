"""
Write a Python program to change a given string to a new string where the first and last chars have been exchanged
"""

def newstr(str):
    return str[-1]+str[1:-1]+str[0]

str=input("enter the new string:")

print(newstr(str))