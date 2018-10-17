"""
Linear Search
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
"""

def linearSearch(l,n):
    for i in l:
        if i is n:
            return l.index(i) ,True
    else:
        return None , False
    
l = [1,2,3,4,'s',3.0,20]
ind , bl = linearSearch(l,'s')
print("is Value in list: {} \nIndex is : {}".format(bl,ind))