d = {'first':'string value', 'second':[1,2], 'third':'hello'}
print(d.items())            # dict_items([('first', 'string value'), ('second', [1, 2])])
#print(d.has_key('first'))   # has_key removed from python3
if 'first' in d:
    print('True')
print(d.get('first'))       # string value
print(d.pop('first'))       # string value
print(d)                    # {'second': [1, 2], 'third': 'hello'}
d.popitem()
print(d)                    # {'second': [1, 2]}  it will remove any one item
d.clear()
print(d)                    # {}
d1 = {'a':1}
d2 = {'b':2, 'c':2}
d1.update(d2)
print(d1)
t = {'first':'string value', 'second':[1,2], 'third':'hello'}
print([x for x in t.values()])      # ['string value', 'hello', [1, 2]]
print([x for x in t.keys()])        # ['first', 'second', 'third']
print([x for x in t.items()])       # [('third', 'hello'), ('first', 'string value'), ('second', [1, 2])]
