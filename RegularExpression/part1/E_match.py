"""
This function attempts to match RE pattern to string with optional flags.
Here is the syntax for this function
re.match(pattern, string, flags=0)
Here is the description of the parameters:
Parameter    Description
pattern    This is the regular expression to be matched.
string    This is the string, which would be searched to match the pattern at the beginning of string.
flags    You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.
The re.match function returns a match object on success, None on failure. We usegroup(num) or groups() function of match object to get matched expression.
Match Object Methods    Description
group(num=0)    This method returns entire match (or specific subgroup num)
groups()    This method returns all matching subgroups in a tuple (empty if there weren't any)
"""
#!/usr/bin/python
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print(matchObj)
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.groups() : ", matchObj.groups())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")