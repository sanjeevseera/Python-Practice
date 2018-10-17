"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
"""

values=input("Input some comma-separated numbers: ")

lists = values.split(",")
tuples=tuple(lists)
print(lists)
print(tuples)

"""
output:
Input some comma-separated numbers: 2,4,12,34,45,56,1
['2', '4', '12', '34', '45', '56', '1']
('2', '4', '12', '34', '45', '56', '1')
"""