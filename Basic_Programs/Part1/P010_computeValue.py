"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615
"""

n=int(input("enter n value:\n"))
print("output:"+ str(int("%s"%n)+int("%s%s"%(n,n))+int("%s%s%s"%(n,n,n))))

"""
output:
enter n value:
9
output:1107
"""