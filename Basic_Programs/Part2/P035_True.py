"""
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""
def sumdef(a,b):
    if(a==b or a+b==5 or abs(a-b)==5):
        return "TRUE"
    else:
        return "FALSE"

a,b=input("enetr 2 numbers with comma seperated:\n").split(",")

print(sumdef(int(a),int(b)))