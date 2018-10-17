"""
Write a Python program to assess if a file is closed or not.
"""
filePath1='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

f = open(filePath1,'r')
print(f.closed)
f.close()
print(f.closed)
