'''
Review concepts of: 
  * namespace
  * imports... (python path), where modules are found
  * not covered, but idea of packaging (pypi)
  * organize code in functions.  Keep them small and simple
  
'''

import usefulModule
import sys

obj = usefulModule.testclass()
obj.dosomething()
#obj.__private()

# demo of how you can send args to a script
print(f"name of script being executed is: {sys.argv[0]}")
print(f'args sent to this script are: {sys.argv[1:]}')


var1= 'better var1'
var2= 'this is var2'
print(var1, var2)

print(usefulModule.var1, usefulModule.var2)


myList = [2, 23, 234, 2, 3, 8, 97, 78, 9, 54, 3, 9, 23]
sumOfList = usefulModule.addUptheNums(myList)
print(f'the sum of the numbers is: {sumOfList}')

# if args are sent to script include them in the calculation of the sum
if sys.argv[1:]:
    # args are always sent as strings, so need to conver to numbers
    argListAsNums = usefulModule.convertToNums(sys.argv[1:])

    sumOfArgs = usefulModule.addUptheNums(argListAsNums)
    # now add those to the other sum
    newSum = sumOfArgs + sumOfList
    print(f"total after adding the args sent: {newSum}")