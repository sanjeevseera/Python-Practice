"""
Write a Python program to find the second largest number in a list.
"""

def second_large(lists):
    n1=lists[0]
    n2=lists[1]
    if n1>n2:
        f_large=n1
        s_large=n2
    else:
        f_large=n2
        s_large=n1
    for n in lists[2:]:
        if n>s_large:
            if n>f_large:
                s_large=f_large
                f_large=n
            else:
                s_large=n
                
    print(f_large,s_large)
    return s_large
        

lists=[1,-9,3,45,-3,0,123]

print(second_large(lists))