"""
 Write a Python program to count the number of strings where the string length is 2 or more and 
 the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
def counts(lists):
    count=0
    for l in lists:
        if len(l)>2 and l[0]==l[-1]:
            count+=1
    return count
            

print(counts(['abc', 'xyz', 'aba', '12231', '1']))