"""
Quick Sort
"""
def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark -1
            
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def quickSort(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)
    return alist

alist = [2, 10, 5, 1, 7, 37, 12, 11, 14, 111, 21, 8, 28, 31, 35, 36, 0]
print("Actual list:\n{}".format(alist))
print("Shorted list:\n{}".format(quickSort(alist,0,len(alist)-1)))