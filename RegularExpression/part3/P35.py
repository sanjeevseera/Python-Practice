"""
Write a Python program to find all words which are at least 4 characters long in a string
"""

import re
text = 'The quick brown fox jumps over the lazy dog.'
for s in re.findall(r'\b\w{4,}\b',text):
    print(s)