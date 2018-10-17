"""
Binary Search
Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array.
If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.
"""

def Binary_Search(alist,item, l, r):
    i=(r+l)//2
    if l == r and alist[l] != item:
        return -1
    elif alist[i] == item:
        return i
    elif alist[i] > item:
        return Binary_Search(alist,item, l, i-1)
    elif alist[i] < item:
        return Binary_Search(alist,item, i+1, r)
    
alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
print("is Value in list: {}".format(Binary_Search(alist,12, 0, len(alist)-1)))
alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
print("is Value in list: {}".format(Binary_Search(alist,212, 0, len(alist)-1)))