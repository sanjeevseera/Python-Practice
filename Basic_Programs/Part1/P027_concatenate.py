"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""

def concat(slist):
    n=len(slist)
    if(n!=0):
        return slist[-n]+concat(slist[1:n])
    else:
        return ''
    
slist=input("enter list values by space seperated:\n").split(" ")
print(concat(slist))

"""
output:
enter list values by space seperated:
sa nj ee v. se e ra
sanjeev.seera
"""