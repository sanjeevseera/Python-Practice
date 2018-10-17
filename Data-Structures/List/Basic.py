a = ['a', 'b','c']
print(a)
print(a.index('b'))     # 1
print(a.index('c', 1, 3)) #2
#print(a.index('b',2))   #  ValueError: 'b' is not in list
a.insert(1 ,'z')
print(a)                # ['a', 'z', 'b', 'c']
a.insert(4, 'a')
print(a)                # ['a', 'z', 'b', 'c', 'a']
print(a.count('a'))     # 2
print(a.count('s'))     # 0
a.remove('a')
print(a)                # ['z', 'b', 'c', 'a']
a.reverse()
print(a)                # ['a', 'c', 'b', 'z']
a.pop()
print(a)                # ['a', 'c', 'b']
a.sort()
print(a)                # ['a', 'b', 'c']
a.sort(reverse=True)
print(a)                # ['c', 'b', 'a']
a.sort(reverse=False)
print(a)                # ['a', 'b', 'c']
a.extend(['d','e','f','g'])
print(a)
print(a[::-1])          # ['c', 'b', 'a']
print(a[::-2])          # ['c', 'b']

