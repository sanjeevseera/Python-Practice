"""
 Write a python program to convert camel case string to snake case string.
"""
import re

def camel_to_snake(text):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    print(str1)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))
