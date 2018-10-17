"""
This function searches for first occurrence of RE pattern within string with optional flags.
Here is the syntax for this function:
re.search(pattern, string, flags=0)
Here is the description of the parameters:
Parameter    Description
pattern    This is the regular expression to be matched.
string    This is the string, which would be searched to match the pattern anywhere in the string.
flags    You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.
The re.search function returns a match object on success, none on failure. We use group(num) or groups() function of match object to get matched expression.
Match Object Methods    Description
group(num=0)    This method returns entire match (or specific subgroup num)
groups()    This method returns all matching subgroups in a tuple (empty if there weren't any)
"""
#!/usr/bin/python
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print(searchObj)
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group() : ", searchObj.groups())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")