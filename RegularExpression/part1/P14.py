"""
Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
"""

import re
def text_match(text):
    if re.search(r'^[a-zA-Z0-9_]*$',  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))
