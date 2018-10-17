"""
Write a Python program to count the number of lines in a text file.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

file=open(filePath,'r')
print(len(file.read().split('\n')))