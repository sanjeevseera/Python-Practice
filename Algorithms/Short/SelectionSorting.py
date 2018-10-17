"""
Selection Sorting
"""
def selection_sort(alist):
    for i in range(len(alist)-1):
        sel_ind = i
        for j in range(i+1,len(alist)):
            if alist[sel_ind] > alist[j]:
                sel_ind = j
        if sel_ind != i:
            (alist[sel_ind], alist[i]) = (alist[i], alist[sel_ind])
    return alist


#alist = [2, 10, 5, 1, 7, 37, 12, 11, 14, 111, 21, 8, 28, 31, 35, 36, 0]
alist = [64, 25, 12, 22, 11]
print("Actual list:\n{}".format(alist))
print("Shorted list:\n{}".format(selection_sort(alist)))