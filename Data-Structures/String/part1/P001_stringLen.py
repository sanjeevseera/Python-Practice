"""
Write a Python program to calculate the length of a string.
"""


def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

str= input("enter the string:")
print(string_length(str))

#print("string length: %s"%len(str))