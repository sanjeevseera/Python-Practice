"""
Write a Python program to read an entire text file.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\Files\P01.py'

file=open(filePath,'r')
filedata=file.read()
print(filedata)
file.close()