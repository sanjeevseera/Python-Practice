"""
Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
"""

import re
street = '21 Ramkrishna Road'
print(re.sub(r'Road','Rd.',street))