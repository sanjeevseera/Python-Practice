"""
Write a Python program to find all three, four, five characters long words in a string
"""

import re
text = 'The quick brown fox jumps over the lazy dog.'
for s in re.findall(r'\b\w{3,5}\b',text):
    print(s)