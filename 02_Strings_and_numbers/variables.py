"""
This is a multiline comment.  

Multilines are defined by triple quotes.

Type of quotes doesn't matter just that you are consistent.


"""

'''
Example of multiline with single quotes
'''

varibles = "this is the value of the variable: variable"

# This is a single line comment

# More on strings
anotherVariable = 'can use single quotes also'

stringWithQuotesInIt = "enclose the 'string' in the opposing type of quotes"
stringWithQuotesInIt2 = 'putting "double quotes" inside singles'

override = 'using backslash to embed a single quote \' in a single quoted string'
overrideDouble = "same thing but with a double quote \" is also possible"

# you saw print in hello world!
# you can also print variables
print(override)

# joining two string variables together
var1 = 'thing 1'
var2 = 'thing 2'
joinVar = var1 + var2
print(joinVar)

# you can join two strings together with more control using "f-strings"
# Note the f before the quotes.  That is what makes it an f-string
newString = f"var1 + var2 = {joinVar}"
print(newString)

# Another example


# you can put f strings into print statements
print(f"the new string is: {newString}")






