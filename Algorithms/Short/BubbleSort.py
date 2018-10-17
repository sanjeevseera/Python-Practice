"""
Bubble Sort
"""
def Bubblesort(alist):
    count=0
    for i in range(len(alist)-1):
        for j in range(i+1,len(alist)):
            count +=1
            if alist[i] > alist[j]:
               temp = alist[i]
               alist[i] = alist[j]
               alist[j] = temp
        print(alist)
    print(count) 
    return alist

alist = [2, 10, 5, 1, 7, 37, 12, 11, 14, 111, 21, 8, 28, 31, 35, 36, 0]
print("Actual list:\n{}".format(alist))
print("Shorted list:\n{}".format(Bubblesort(alist)))