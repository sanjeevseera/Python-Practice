"""
HeapSort
"""
def heapify(alist, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and alist[i] < alist[l]:
        largest = l

    if r < n and alist[largest] < alist[r]:
        largest = r

    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]  # swap
        heapify(alist, n, largest)


def heapSort(alist):
    n = len(alist)
    for i in range(n, -1, -1):
        heapify(alist, n, i)

    for i in range(n-1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]  # swap
        heapify(alist, i, 0)
    return alist


#arr = [12, 11, 13, 5, 6, 7]
#heapSort(arr)
#print("Sorted array is")
#print(arr)

alist = [2, 10, 5, 1, 7, 37, 12, 11, 14, 111, 21, 8, 28, 31, 35, 36, 0]
print("Actual list:\n{}".format(alist))
print("Shorted list:\n{}".format(heapSort(alist)))