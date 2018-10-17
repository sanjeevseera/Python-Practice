"""
Write a Python function to get a string made of 4 copies of the last two characters of a specified string 
(length must be at least 2). Go to the editor
Sample function and result : 
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""

def newstr(str):
    if len(str)>=2:
        return str[-2:]*4
    else:
        return str

str=input("enter a string:\n")

print(newstr(str))