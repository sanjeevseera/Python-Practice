"""
Write a Python program to find the second smallest number in a list.
"""

def second_small(lists):
    n1=lists[0]
    n2=lists[1]
    if n1<n2:
        f_small=n1
        s_small=n2
    else:
        f_small=n2
        s_small=n1
    for n in lists[2:]:
        if n<s_small:
            if n<f_small:
                s_small=f_small
                f_small=n
            else:
                s_small=n
                
    print(f_small,s_small)
    return s_small
        

lists=[1,-9,3,45,-3,0,123]

print(second_small(lists))