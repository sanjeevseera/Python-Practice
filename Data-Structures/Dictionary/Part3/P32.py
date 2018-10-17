"""
Write a Python program to print a dictionary line by line
"""

students = {'Aex':{'class':'V','rolld_id':2},
            'san': 123,
        'Puja':{'class':'V','roll_id':3}}
for a in students:
    if isinstance(students[a], dict):
        print(a,'{')
        for b in students[a]:
            print (b,':',students[a][b])
        print('}')
    else:
        print (a,':',students[a])
        