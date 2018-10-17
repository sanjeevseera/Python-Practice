"""
fibonacci-search
The idea is to first find the smallest Fibonacci number that is greater than or equal to the length of given array.
Let the found Fibonacci number be fib (m’th Fibonacci number).
We use (m-2)’th Fibonacci number as the index (If it is a valid index).
Let (m-2)’th Fibonacci Number be i, we compare arr[i] with x, if x is same, we return i.
Else if x is greater, we recur for subarray after i, else we recur for subarray before i.
"""
def fibonacciSearch(alist,item,nl):
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1
    if nl>1:
        while fibM<nl:
            fibMMm2 = fibMMm1
            fibMMm1 = fibM
            fibM = fibMMm2 + fibMMm1
        offset = -1
        while fibM > 1:
            i = min(offset+fibMMm2, nl-1)
            if alist[i] == item:
                return i
            elif alist[i] < item:
                fibM = fibMMm1
                fibMMm1 = fibMMm2
                fibMMm2 = fibM - fibMMm1
                offset = i
            elif alist[i] > item:
                fibM = fibMMm2
                fibMMm1 = fibMMm1 - fibMMm2
                fibMMm2 = fibM - fibMMm1
        return -1
    elif alis[0]==item:
        return 0
    else:
        return -1
    return -1

def main():
    alist = [1,2,3,12] #[2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(fibonacciSearch(alist,12, len(alist))))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(fibonacciSearch(alist,12, len(alist))))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(fibonacciSearch(alist,212, len(alist))))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(fibonacciSearch(alist,38, len(alist))))
    alist = [2, 5, 7, 12, 14, 21, 28, 31, 36, 38]
    print("is Value in list: {}".format(fibonacciSearch(alist,1, len(alist))))

if __name__ == "__main__":
    main()