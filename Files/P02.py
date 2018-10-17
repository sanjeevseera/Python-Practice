"""
Write a Python program to read first n lines of a file.
"""
from itertools import islice

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'
n=2
file=open(filePath,'r')
#filedata=file.read()
#print(filedata)
for line in islice(file, n):
    print(line)
file.close()