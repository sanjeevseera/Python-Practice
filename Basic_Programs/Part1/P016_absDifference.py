"""
Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference.
"""

num=int(input("enter any number:\n"))

def difference(n):
    if n>17:
        return (n-17)*2
    elif n<17:
        return 17-n
    else:
        return 0
    
print(difference(num))