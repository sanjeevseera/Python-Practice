"""
Write a Python program to separate and print the numbers and their position of a given string. 
"""

import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements.\
 Four elements are then added to the 60 ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
