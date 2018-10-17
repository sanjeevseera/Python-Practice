"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
"""

from datetime import date

sanjeev_DOB=date(int(input("enter sanjeev: Year:")),int(input("enter sanjeev: Month")),int(input("enter sanjeev: Day")))
santhi_DOB=date(int(input("enter santhi: Year")),int(input("enter santhi: Month")),int(input("enter santhi: Day")))
print("sanjeev D.O.B: %s" %sanjeev_DOB)
print("santhi D.O.B: %s" %santhi_DOB)
print("days difference: %s days" %(santhi_DOB-sanjeev_DOB).days)