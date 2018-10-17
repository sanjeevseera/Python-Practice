"""
 Write a Python program to get the file size of a plain file.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

file=open(filePath,'r')

print("Size of file:%s"%file.seek(0,2))

file.close()