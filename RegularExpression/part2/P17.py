"""
 Write a Python program to check for a number at the end of a string.
"""

import re
def match_num(string):
    if re.match(r".*\d$",string):
        return True
    else:
        return False
print(match_num('sanjeev1'))
print(match_num('1seera'))