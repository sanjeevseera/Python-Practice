"""
Write a Python program to create and display all combinations of letters,
 selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output: 
ac
ad
bc
bd
"""

dicts={'1':['a','b'], '2':['c','d']}
keyList=[]
comboList=[]
MixedcomboList=[]
for dk in dicts.keys():
    keyList.extend(dk)

for k in range(len(keyList)-1):
    comboList.extend([a+b for a in dicts[keyList[k]] for b in dicts[keyList[k+1]]])
print("combinations of letters:-> %s"%comboList)

for k in keyList:
    for j in keyList:
        if k!=j:
            MixedcomboList.extend([a+b for a in dicts[k] for b in dicts[j]])
        else:
            pass          
print("Probability of combinations of letters:-> %s"%MixedcomboList)