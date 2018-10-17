"""
Write a Python function that takes a list of words and returns the length of the longest one
"""

def Lword(wlist):
    word=wlist[0]
    for w in wlist[1:]:
        if len(w)>len(word):
            word=w
    return word

wlist=input("enter the words by comma separated:...").split(',')

print(Lword(wlist))