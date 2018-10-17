"""
Write a Python program to get the last part of a string before a specified character.
http://www.w3resource.com/python-exercises
http://www.w3resource.com/python
"""

str1 = 'http://www.w3resource-com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])