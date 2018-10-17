"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
"""
def newstr(str):
    str=str.replace(str[str.index('not'):str.index('poor')+4],'good')
    return str

str=input("Enter string: ")

print(newstr(str))