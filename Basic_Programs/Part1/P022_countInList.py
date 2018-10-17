"""
Write a Python program to count the number 4 in a given list
"""

numbers=input("enter the numbers with comma seperated:\n").split(",")
count=0
for i in numbers:
    if int(i) == 4:
        count+=1

print("number of 4s in list: %i"%count)