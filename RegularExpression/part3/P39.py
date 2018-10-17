"""
Write a Python program to remove multiple spaces in a string.
"""

import re
text1 = 'Python     Exercises'
print("Original string:",text1)
#print("Without extra spaces:",re.sub(' {2,}',' ',text1))
print("Without extra spaces:",re.sub(' +',' ',text1))
