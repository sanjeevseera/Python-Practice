"""
Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case
"""

class py_solution:
    def __init__(self):
        self.str1=''
    def get_str(self,s):
        self.str1=s
    def print_str(self):
        print(self.str1.upper())
 
str1 = py_solution()     
str1.get_str("sanjeev")
str1.print_str()