"""
Write a Python program to create a histogram from a given list of integers.
"""

nlist=input("enter numbers with comma seperated:\n").split(",")
for i in range(len(nlist)):
    nlist[i]=int(nlist[i])
    print("*"*nlist[i])

"""
otput:
2,3,12,1,0,23
**
***
************
*

***********************
"""