"""
Write a Python program that matches a string that has an a followed by three 'b'.
"""

import re
def text_match(text):
    #patterns = 'ab*?'
    if re.search(r'ab{3}?',  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("abbbc"))
print(text_match("abbbbc"))