"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2
"""

def copies(string,n):
    if(len(string)<2):
        return string*n
    else:
        return string[:2]*n
    
string,n=input("Enter string and number by comma seperated:\n").split(",")

print("new string: %s"%copies(string,int(n)))