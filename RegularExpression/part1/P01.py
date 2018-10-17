"""
Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
"""

import re
def is_allowed_specific_char(string):
    #charRe = re.compile(r'[^a-zA-Z0-9.]')
    #string = charRe.search(string)
    string1 = re.search(r'[^a-zA-Z0-9]',string, re.M|re.I)
    return not bool(string1)

print(is_allowed_specific_char("ABCDEFabcdef123450a.")) 
print(is_allowed_specific_char("*&%@#!}{"))