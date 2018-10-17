"""
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. 
"""

import re
def text_match(text):
    #patterns = 'ab*?'
    if re.search(r'a{1}.*b$',  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("Aabcbbbb"))
print(text_match("aabAbbbc"))
print(text_match("AababbbB"))
print(text_match("ABab---32b"))