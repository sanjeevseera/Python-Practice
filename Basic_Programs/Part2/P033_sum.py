"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
"""

def sumof(a,b,c):
    if(a==b or a==c or b==c):
        return 0
    else:
        return a+b+c
    
    
a,b,c=input("enetr 3 numbers with comma seperated:\n").split(",")

print(sumof(int(a),int(b),int(c)))