"""
Write a Python program to append text to a file and display the text.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

file=open(filePath,"r+")
fileData=file.read()
print(fileData)
file.write("\nsanjeev\n")
file.close()
file1=open(filePath,"r")
fileData1=file1.read()
print(fileData1)
file1.close()