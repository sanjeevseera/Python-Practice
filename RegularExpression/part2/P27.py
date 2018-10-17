"""
Write a Python program to separate and print the numbers of a given string.
"""

import re
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
print(text)
text=re.split('\D+',text)
for dig in text:
    print(dig)