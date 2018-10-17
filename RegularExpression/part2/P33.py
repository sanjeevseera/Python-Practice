"""
Write a Python program to find all five characters long word in a string.
"""

import re
text = 'The quick brown fox jumps over the lazy dog.'
for s in re.findall(r'\b\w{5}\b',text):
    print(s)