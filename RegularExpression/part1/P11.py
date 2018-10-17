"""
Write a Python program that matches a word at end of string, with optional punctuation
"""

import re
def text_match(text):
        if re.search(r'\w+\S*$',  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))
