print("\tbc")  #    bc
print(r"\tbc") # \tbc
a = "abc"
print(a[0:])    # abc
print("44".isdigit())   # is the string made of digits only ?    True
print("44".isalpha())   # is the string made of alphabetic characters only ? False
print("44".isalnum())   # is the string made of alphabetic characters or digits only ?   True
print("Aa".isupper())   # is it made of upper cases only ?   False
print("aa".islower())   # or lower cases only ?   True
print("Aa".istitle())   # does the string start with a capital letter ?  True
text = "There are spaces but not only"
print(text.isspace())   # is the string made of spaces only ?  False
mystr = "this is a dummy string"
mystr = mystr.replace('dummy', 'great', 1)    # the 1 means replace only once   'this is a great string'
print(mystr)
mystr = "this is a line"
print(mystr.partition('is'))
print(mystr.rpartition('is'))
mystr = "this is a line"
print(mystr.split(' '))
print(mystr.split(' ',2))
print(mystr.split(' '))
print(mystr.split(' ',2))
print(mystr.rsplit(' '))
print(mystr.rsplit(' ',2))