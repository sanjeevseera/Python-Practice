"""
 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
 except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def newStr(strN):
    char=strN[0]
    length=len(strN)
    strN=strN.replace(char,'$')
    strN=char+strN[1:]
    
    return strN
        

str=input("enter the string: ")
print(newStr(str))