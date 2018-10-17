"""
Write a python program to find the longest words.
"""

filePath='D:\My Data\Python\workspace\Practice_exercise\src\delete.txt'

def longest_word(filename):
    infile=open(filename, 'r')
    words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word(filePath))
