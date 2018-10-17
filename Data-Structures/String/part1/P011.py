"""
Write a Python program to remove the characters which have odd index values of a given string.
"""

def newstr(str):
    for i in range(len(str)-1,0,-1):
        if i%2:
            str=str.replace(str[i:],str[i+1:])
    return str

str=input("enter the string:")

print(newstr(str))