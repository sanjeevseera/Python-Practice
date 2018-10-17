"""
Write a Python program to generate a 3*4*2 3D array whose each element is *.
"""

array = [[ ['*' for col in range(2)] for col in range(4)] for row in range(3)]
print(array)