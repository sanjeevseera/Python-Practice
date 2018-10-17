"""
Write a Python program to find sequences of one upper case letter followed by lower case letters.
"""

import re
def text_match(text):
    #patterns = 'ab*?'
    if re.search(r'^[A-Z]{1}[a-z]+$',  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("Aabcbbbc"))
print(text_match("aabAbbbc"))
print(text_match("AababbbB"))
print(text_match("ABababbbc"))