"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
"""

def sumof(a,b,c):
    if(a+b+c >= 15 and a+b+c <= 20):
        return 20 
    else:
        return a+b+c
    
    
a,b,c=input("enetr 3 numbers with comma seperated:\n").split(",")

print(sumof(int(a),int(b),int(c)))