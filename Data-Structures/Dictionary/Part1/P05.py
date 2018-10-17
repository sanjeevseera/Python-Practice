"""
Write a Python program to iterate over dictionaries using for loops
"""


d = {'x': 10, 'y': 20, 'z': 30}
print(d.keys())
print(d.values())
print(d.items()) 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)
    