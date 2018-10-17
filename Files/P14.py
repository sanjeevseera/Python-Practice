"""
Write a Python program to combine each line from first file with the corresponding line in second file.
"""

filePath1='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'
filePath2='D:\My Data\Python\workspace\Practice_exercise\src\delete1.txt'

with open(filePath1) as fh1, open(filePath2) as fh2:
    for line1, line2 in zip(fh1,fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
        