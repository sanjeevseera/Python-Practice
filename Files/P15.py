"""
Write a Python program to read a random line from a file.
"""


filePath1='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    print(lines)
    return random.choice(lines)
print(random_line(filePath1))