"""
Write a Python program to count the frequency of words in a file.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

file=open(filePath,'r')
fdata=file.read().split('\n')
print(fdata)
dicts={}
for key in fdata:
    if key in dicts.keys():
        dicts[key]+=1
    else:
        dicts[key]=1

file.close()
print(dicts)