"""
Write a Python program to remove words from a string of length between 1 and a given number.
"""

import re
text = "The quick brown fox jumps over the lazy dog."
# remove words between 1 and 3
print(re.sub(r'\W*\b\w{1,3}\b','', text))