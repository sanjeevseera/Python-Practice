"""
interpolation-search
Step1: In a loop, calculate the value of “pos” using the probe position formula.
pos = lo + ((item-alist[lo])*(hi-lo) // (alist[hi]-alist[lo]))
Step2: If it is a match, return the index of the item, and exit.
Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array.
Otherwise calculate the same in the right sub-array.
Step4: Repeat until a match is found or the sub-array reduces to zero.
"""

def interpolationSearch(alist,item,lo,hi):
    i = lo + ((item-alist[lo])*(hi-lo) // (alist[hi]-alist[lo]))
    if i>hi:
        return -1
    elif lo == hi and alist[l0] != item:
        return -1
    elif alist[i] == item:
        return i
    elif alist[i] > item:
        return interpolationSearch(alist,item, lo, i-1)
    elif alist[i] < item:
        return interpolationSearch(alist,item, i+1, hi)
    else:
        return -1

def main():
    alist = [1,2,3,12] #[2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(interpolationSearch(alist,12, 0, len(alist)-1)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(interpolationSearch(alist,212, 0, len(alist)-1)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(interpolationSearch(alist,38, 0, len(alist)-1)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(interpolationSearch(alist,1, 0, len(alist)-1)))

if __name__ == "__main__":
    main()