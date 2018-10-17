"""
exponential-search
Exponential search involves two steps:
    1. Find range where element is present
    2. Do Binary Search in above found range.
The idea is to start with subarray size 1,
compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater.
Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i
(Why i/2? because we could not find a greater value in previous iteration)
"""
from BinarySearch import Binary_Search

def exponentialSearch(alist,item):
    i=0
    while i < len(alist):
        if alist[i] == item:
            return i
        elif alist[i] > item and i==0:
            return -1
        elif alist[i] > item:
            return Binary_Search(alist,item, (i//2)+1, i-1)
        elif i==0:
            i=1
        else:
            i=i*2

    if (i//2)+1 <= len(alist)-1:
        return Binary_Search(alist,item, (i//2)+1, len(alist)-1)
    return -1

def main():
    alist = [1,2,3,12]
    print("is Value in list: {}".format(exponentialSearch(alist,12)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(exponentialSearch(alist,212)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(exponentialSearch(alist,38)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(exponentialSearch(alist,1)))

if __name__ == "__main__":
    main()