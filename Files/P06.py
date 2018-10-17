"""
Write a Python program to read a file line by line store it into a variable
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

file=open(filePath,'r')
fdata=file.readlines()
print(fdata)
file.close()