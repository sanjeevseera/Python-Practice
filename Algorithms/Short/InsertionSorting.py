"""
Insertion Sort
"""

def Insertionsort(alist):
    count=0
    nlist=[]
    for i in range(1,len(alist)):
        for j in range(len(alist[:i])):
            count +=1
            if alist[j] > alist[i]:
                nlist.extend(alist[:j])
                nlist.append(alist[i])
                alist[i:] = alist[i+1:]
                nlist.extend(alist[j:])
                alist=nlist
                nlist=[]
                break
    del nlist
    print(count)
    return alist             
        
alist = [2, 10, 5, 1, 7, 37, 12, 11, 14, 111, 21, 8, 28, 31, 35, 36, 0]
print("Actual list:\n{}".format(alist))
print("Shorted list:\n{}".format(Insertionsort(alist)))
