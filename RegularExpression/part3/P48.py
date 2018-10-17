"""
Write a Python program to check a decimal with a precision of 2.
"""

def is_decimal(num):
    import re
    result = re.search(r"^[0-9]+(\.[0-9]{1,2})?$",num)
    return bool(result)

print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123'))
print(is_decimal('0.21'))

print(is_decimal('123.1214'))
print(is_decimal('3.124587'))
print(is_decimal('e666.86'))