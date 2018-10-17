"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
"""

def sum(num):
    if(num[0] == num[-1] and num[0] == num[1]):
        return (int(num[0])+int(num[1])+int(num[-1]))*3
    else:
        return int(num[0])+int(num[1])+int(num[-1])
    
numbers=tuple(input("enter 3 numbers:\n").split(","))

print(sum(numbers))