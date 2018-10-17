"""
Write a Python program to sort a string lexicographically
"""

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3Resource'))
print(lexicographi_sort('quickbrown'))