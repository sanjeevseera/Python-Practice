"""
Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output: 
example
w3resource
github
stackoverflow
"""

import re

ldata=["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for s in ldata:
    print(re.sub(r' ?\([^)]+\)','',s))