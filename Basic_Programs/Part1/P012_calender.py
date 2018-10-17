"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 
"""

import calendar
from datetime import datetime

now = datetime.now()
m=int(now.strftime("%m"))
y=int(now.strftime("%Y"))
#m=int(input("enter month:\n"))
#y=int(input("enter year:\n"))
print(calendar.month(y,m))

"""
Output:
enter month:
6
enter year:
1998
     June 1998
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
"""