# a function that recieves on arguement
def functionWithArgs(argNumberOne):
    print(f"argNumberOne is {argNumberOne}")

# functions can also recieve multiple arguements
def functionWithMultiArgs(argOne, argTwo, argThree, ArgArg):
    print(f"argOne is: {argOne}")
    print(f"ArgArg is: {ArgArg}")

# functions can return data also
def addUpTheArgs(arg1, arg2):
    newData = arg1 + arg2
    return newData

# returning multiple values
def returnMultipleValues(arg1, arg2):
    newData = arg1 + arg2
    # to return multiple values put the data into list
    returnList = [arg1, arg2, newData]
    return returnList

# call the function that takes one arguement
functionWithArgs('arg sent to function')

# caling a funtion that recieves multiple args, the function 
# "functionWithMultiArgs" is expecting 4 args.  Any less or any more
# will generate an error.
# in the call below:
#    'one' goes into the arg: argOne
#    'two' goes into the arg: argTwo
#    'three' goes into the arg: argThree
#    'four' goes into the arg: ArgArg
functionWithMultiArgs("one", 'two', 'three', 'four')

# calling the add up function but instead of sending the args 
# based on positions we are sending using the names.
# this way the order doesn't matter
# the returned value from the function goes into "joinedValue"
joinedValue = addUpTheArgs(arg2='Is The Greatest', arg1='Guy Lafleur')
print(f"joinedValue is: {joinedValue}")

joinedValuesList = returnMultipleValues(arg2='Is The Greatest', arg1='Guy Lafleur')
print(f"joinedValuesList: {joinedValuesList}")
