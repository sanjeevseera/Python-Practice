"""
 Write a Python program to match if two words from a list of words starting with letter 'P'
"""

import re

# Sample strings.
words = ["Python A PHP", "Java JavaScript", "c c++"]

for lwords in words:
    if re.search(r'P\w+ .*P\w',lwords):
        print(lwords)