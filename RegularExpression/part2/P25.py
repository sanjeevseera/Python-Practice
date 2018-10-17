"""
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
"""

#date='2107-10-03'
#print(date)
#date=date.split('-')
#date.reverse()
#print('-'.join(date))


import re
def change_date_format(dt):
    cdate=re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})',dt)
    print(cdate.group(1))
    print(cdate.group(2))
    print(cdate.group(3))
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))
