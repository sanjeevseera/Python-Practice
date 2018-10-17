"""
Write a Python program to copy the contents of a file to another file
"""

filePath1='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'
filePath2='D:\My Data\Python\workspace\Practice_exercise\src\delete1.txt'

f1=open(filePath1,'r')
f2=open(filePath2,'a')

f2.write(f1.read())
f2=open(filePath2,'r')
print(f2.read())