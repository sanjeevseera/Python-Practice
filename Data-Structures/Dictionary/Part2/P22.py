"""
Write a Python program to find the highest 3 values in a dictionary
"""

def large(k):
    for i in LargeList:
        if my_dict[k] > my_dict[i]:
            print(LargeList)
            LargeList.remove(i)
            print(LargeList)
            LargeList.append(k)
            print(LargeList)
            k=i
            large(k)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} 
LargeList=[]
keyList=[]
for dk in my_dict.keys():
    keyList.extend(dk)
print(keyList)

for k in keyList:
    if len(LargeList) < 3:
        LargeList.append(k)
    else:
        large(k)
        
print(LargeList) 