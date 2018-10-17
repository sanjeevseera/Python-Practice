"""
 Write a Python program to find all words starting with 'a' or 'e' in a given string.
"""
import re

text = "The following example creates an ArrayList with a capacity of 50 elements.\
 Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
lists = re.findall("[ae]\w+", text)
# Print result.
print(lists)