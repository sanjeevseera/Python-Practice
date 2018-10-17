a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a | b) # Union    {1, 2, 3, 4, 5, 6}
print(a.union(b)) # # Union    {1, 2, 3, 4, 5, 6}
print(a & b) # Intersection {3, 4}
print(a.intersection(b))     # {3, 4}
print(a < b) # Subset   False
print(b < a) # Subset   False
print(b <= b) # Subset True
print(b.issubset(b)) # Subset True
print(a > b ) # issuperset False
print(a > a)   # issuperset False
print(a >= a)   # issuperset True
print(a.issuperset(a)) #issuperset True
print(a - b) # Difference   {1, 2}
print(a.difference(b)) # Difference   {1, 2}
print(b - a) # {5, 6}
print(a ^ b) # Symmetric Difference {1, 2, 5, 6}
print(a.symmetric_difference(b)) # Symmetric Difference {1, 2, 5, 6}
print(a)
print(b)
b = a.copy()
print(a)
print(b)