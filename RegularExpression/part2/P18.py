"""
Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
"""

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important 12345")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))


#def my_match(str1):
#    if re.search(r'[0-9]{1,3}',str1):
#        return True
#    else:
#        return False

#print(my_match("san1j2e3ev"))
#print(my_match("san12je3ev"))
#print(my_match("san123jeev"))
#print(my_match("san1234jeev"))
#print(my_match("sanjeev"))