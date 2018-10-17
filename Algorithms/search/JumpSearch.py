"""
Jump Search
For example,
suppose we have an array arr[] of size n and block (to be jumped) size m.
Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on.
Once we find the interval (arr[km] < x < arr[(k+1)m]),
we perform a linear search operation from the index km to find the element x
m = √n
"""
import math

def JumpSearch(alist,item):
    Step = math.sqrt(len(alist))
    for i in range(0,len(alist),int(Step)):
        if alist[i] == item:
            return i
        elif alist[i]>item and i==0:
            return -1
        elif alist[i]>item:
            for j in range(i-Step+1,i):
                if alist[j]==item:
                    return j
            return -1
        elif i+int(Step) > len(alist)-1 and i != len(alist)-1:
            for j in range(i+1,len(alist)):
                if alist[j]==item:
                    return j
            return -1
    return -1

def main():
    alist = [1,2,3,12] #[2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(JumpSearch(alist,12)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(JumpSearch(alist,212)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(JumpSearch(alist,38)))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(JumpSearch(alist,1)))

if __name__ == "__main__":
    main()