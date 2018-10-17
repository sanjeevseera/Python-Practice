"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

def occu(sen):
    dict={}
    for c in sen:
        if c in dict.keys():
            dict[c]+=1
        else:
            dict[c]=1
    return dict

sentence=input("Enter the sentence:\n").split(' ')

print(occu(sentence))