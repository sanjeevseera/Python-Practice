"""
Write a Python program to read a file line by line and store it into a list.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

file=open(filePath,'r')
fList=[]
fList.extend(file.readlines())
print(fList)
file.close()