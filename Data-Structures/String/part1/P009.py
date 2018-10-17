"""
Write a Python program to remove the nth index character from a nonempty string
"""

str=input("enter the string:")
n=int(input("enter the index:"))

str=str.replace(str[n:],str[n+1:])
print(str)