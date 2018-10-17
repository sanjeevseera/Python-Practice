"""
Write a Python program where a string will start with a specific number.
"""

import re
def match_num(string):
    if re.match(r"5",string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))
