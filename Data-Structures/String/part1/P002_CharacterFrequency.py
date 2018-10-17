"""
Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

def charFrequency(str):
    charsDict={}
    for c in str:
        if c in charsDict.keys():
            charsDict[c]+=1
        else:
            charsDict[c]=1
      
    return charsDict

str=input("Enter the string: ")
print(charFrequency(str))