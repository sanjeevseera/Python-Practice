"""
Write a Python program to list all files in a directory in Python
"""
from os import listdir
from os.path import isfile, join

path = "D:\My Data\Python\workspace\Practice_exercise\src\python-basic\Part2"
#files_list = [f for f in listdir(path) if isfile(join(path, f))]
files_list = []
for f in listdir(path):
        if isfile(f):
            files_list.append(f)
print(files_list);