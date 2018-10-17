"""
Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for d in (d1,d2):
    for dk,dv in  d.items():
        if dk in d3.keys():
            d3[dk] = d3[dk]+dv
        else:
            d3[dk]=dv
print(d3) 