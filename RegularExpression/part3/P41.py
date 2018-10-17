"""
Write a Python program to remove everything except alphanumeric characters from a string. 
"""

import re
text1 = 'Python     Exercises124.;*'
print("Original string:",text1)
#print("Without extra spaces:",re.sub('[^a-zA-Z0-9]','',text1))
print("Without extra spaces:",re.sub('[\W_]+','',text1))