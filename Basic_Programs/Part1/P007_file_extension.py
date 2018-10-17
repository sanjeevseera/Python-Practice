"""
Write a Python program to accept a filename from the user and print the extension of that
"""

fileName=input("enter the file name with extension:\n")
extension=fileName.split(".")
print("The file extension is: %s" %extension[-1])

"""
output:
enter the file name with extension:
sam.ddss.dfg.ddf.py
The file extension is: py
"""