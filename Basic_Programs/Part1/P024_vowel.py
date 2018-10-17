"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

char=input("enter a letter:").lower()
vowels=('a','e','i','o','u')
if(char in vowels):
    print("letter you entered is VOWEL")
else:
    print("letter you entered is not VOWEL")