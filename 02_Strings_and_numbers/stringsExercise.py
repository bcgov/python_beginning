player = 'guy lafeur'
player2 = 'Steve Shutt'
newVar = player + player2
print(newVar)

# create a variable called "player" and make it equal to: 'Guy Lafleur'
player = 'guy lafeur'

# create a variable called "player2" and make it equal to: 'Steve Shutt'
player2 = 'Steve Shutt'

# join the two variables player and player2 together to create a new variable
playersJoined = player + player2

# join the two variables together in print statement
print(player + player2)
print(playersJoined)
# add a space in between the two variables
print(player + ' '  + player2)

# you can also join together two variables in a print statement 
# by delimiting (separating) them using a comma (,)
# Use this technique to print the two variables player, and player2

print("example of print comma operator", player,  player2, 2)
print(player + player2 + str(2))

myVar = 'Montreal Canadians'
statement = f"The greatest hockey team of all time: {{}} {myVar}"
print(statement)


statement = f"The greatest hockey team of all time:  {player + ' ' + player2}"
# create a new variable called "team" and make it equal to 
# 'Montreal Canadians'
team = 'Montreal Canadians'

# create an f-string that combines the variable "team" with the text "are the greatest"
statement = f"{team} are the greatest"
# do the same thing above only in a print statement.
print(statement)

print(f"{team} are the greatest")


var = 'some text in a variable'
newVar = var + 'other text'
var2 = 'Another variable going here'
print(f"the variable var is {var}")

newVar = player + ", total characters is: " + str(len(player))
longString = '''
NLdNfmp8zQGPblz5QC8K49uvc2nxlwDbctIsZpKdYFAfAGOZsPncIcQvG
mGZNddBNhEVU8pDRSqBQOMRkTWT1ZrKR67YnrVqMrnMcxqx9RKGeG2l95pXIN50Y
zmyuM0lG4MqEESyPHCcT3QFybScWfYRHZupQI6um9pxAyiFCDwADKPrChD5r1FpvTW3Eko2XxOoJh
AeHngK95Wq3YcBywWGsdKHeIiZEE3ggSJpJ9GFRQEDlhlE3gjvVBDH635vyoAxEoJt72gPzp8V
'''
print(len(longString))

# Capitalize the first letter in the string using the method capitalize
greatTweets = '  windmills are the greatest threat in the us to both bald and golden eagles\n '
print(greatTweets)
newVar = greatTweets.strip().capitalize()
print(newVar)

# Capitalize the first character of every word using the 'title' method
titleFormat = newVar.title()
print(titleFormat)
del titleFormat
print(titleFormat)




# Remove leading and trailing whitespace

