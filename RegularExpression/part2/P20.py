"""
Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'
"""
import re

text='The quick brown fox jumps over the lazy dog.'
matchs=re.search(r'fox',text)
print('Found "fox" in "The quick brown fox jumps over the lazy dog." from %d to %d' %(matchs.span()[0],matchs.span()[1]))
print('Found "fox" in "The quick brown fox jumps over the lazy dog." from %d to %d' %(matchs.start(),matchs.end()))