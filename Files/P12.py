"""
Write a Python program to write a list to a file.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete1.txt'

file=open(filePath,'w')

lists=['I','LOVE','INDIA','Seera Sanjeev']

for s in lists:
    file.write("%s\n"%s)
file.close()
file=open(filePath,'r')    
print(file.read())
file.close()