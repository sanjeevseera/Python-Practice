"""
 Write a Python program to convert a dictionary to OrderedDict.
"""

import collections
student = [("Student_name", "Alex"),
        ("ID", 5),
        ("Class", 'V'),
        ("Country", 'USA')]

student = collections.OrderedDict(student)
print(student)
