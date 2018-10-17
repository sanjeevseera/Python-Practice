"""
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
"""

def numType(num):
    if(num%2 == 0):
        return "The number u entered is EVEN"
    else:
        return "The number i entered id ODD"

num=int(input("enter a number:\n"))

print(numType(num))