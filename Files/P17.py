"""
Write a Python program to remove newline characters from a file. 
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

def remove_newlines(fname):
    flist = open(fname).readlines()
    print(flist)
    return [s.rstrip('\n') for s in flist]

print(remove_newlines(filePath))
