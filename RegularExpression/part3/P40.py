"""
Write a Python program to remove all whitespaces from a string.
"""

import re
text1 = 'Python     Exercises'
print("Original string:",text1)
print("Without extra spaces:",re.sub('\s+','',text1))
#print("Without extra spaces:",re.sub(' ','',text1))