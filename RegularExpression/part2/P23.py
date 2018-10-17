"""
Write a Python program to replace whitespaces with an underscore and vice versa.
"""

import re

text='_sanjeev_seera sanjeev_seera '
print(text)
text=re.sub(r'_','M_M',text)
text=re.sub(r' ','_',text)
text=re.sub(r'M_M',' ',text)
print(text)