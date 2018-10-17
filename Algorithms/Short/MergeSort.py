"""
Merge Sort
"""
def merge(alist, l, m, r):
    if l == m:
        if alist[l] > alist[r]:
            (alist[l],alist[r]) = (alist[r],alist[l])
    else:
        temp=[]
        i=l
        j=m+1
        while i < m+1 and j < r+1:
            if alist[i] < alist[j]:
                temp.append(alist[i])
                i +=1
            else:
                temp.append(alist[j])
                j +=1
        if j < r+1:
            temp.extend(alist[j:r+1])
        if i < m+1:
            temp.extend(alist[i:m+1])
        alist[l:r+1] = temp
        del temp


def mergeSort(alist, l, r):
    if l < r:
        m = (l+r)//2
        mergeSort(alist, l, m)
        mergeSort(alist, m+1, r)
        merge(alist, l, m, r)
    return alist


def main():
    alist = [2, 10, 5, 7, 1, 37, 12, 11, 14, 111, 21, 8, 28, 31, 35, 36, 0]
    print("Actual list:\n{}".format(alist))
    print("Shorted list:\n{}".format(mergeSort(alist, 0, len(alist)-1)))

if __name__ == "__main__":
    main()