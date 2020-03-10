
'''var = 'I am a var'
if not var.islower():
    print("its all lower case")


listOfPlayers =  ['Gordie Howe', 'Alex Ovechkin', 'Jean Beliveau',
                  'Brett Hull', "Jesus McDavid",  'Guy Lafeur', 
                  'Mike Bossy', 'Phil Esposito', 'Carey Price', 
                  'Mats Naslund']
for player in listOfPlayers:
    if player[0].upper() == 'G':
        print(f"Players with names that start with G: {player}")
        break
    

print(f"player after list is {player}")
# -----------------------------------------------------------
stringList = ['ama', 'aa', 'ab', 'abc', 'bad', 'lol', 'dog', 'cat', 'a', 'f', 'x']
# Given the list of strings "stringList", return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
count = 0
for word in stringList:
    if len(word) >= 2:
        lastChar = word[-1]
        firstChar = word[0]
        if lastChar == firstChar:
            count += 1
            print(f'found : {word}')
print(f"the answer is:{count}")

count = 0
for word in stringList:
    lastChar = word[-1]
    firstChar = word[0]
    if len(word) >= 2 and lastChar == firstChar:
        count += 1
        print(f'found : {word}')
print(f"the answer is:{count}")




inputList = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# # Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
xList = []
restList = []
for elem in inputList:
    print(f'{elem[0].upper}')
    if elem[0].upper == 'X':
        xList.append(elem)
    else:
        restList.append(elem)
xList.sort()
restList.sort()
xList.extend(restList)
print(f"xList: {xList}")


class testClass:
    def __init__(self):
        self.prop = 'a prop'

    def prop(self):
        print('this is a method')

tst = testClass()
print(tst.prop)
print(tst.prop())
'''

for num in range(3):
    print(f"num is: {num}")
print('*'*30)
for num in range(1, 4):
    print(f"num is: {num}")
print('*'*30)

for num in range(1, 12, 4):
    print(f"num is: {num}")


# create a while loop that iterates through the list "inputList" until it finds a string that 
# contains a number
# * Hint: take a look at the string methods here to find the correct method.
#      https://docs.python.org/3/library/stdtypes.html#string-methods
inputList = ['aba', 'xyz', 'aa', 'x', 'bb4b', '', 'x', 'xy', 'xyx', 'xx', '234','aaa', 'be', 'abc', 'hello']

cnter = 0
while cnter < len(inputList):
    print(f"elem is: {inputList[cnter]}")
    elem = inputList[cnter]
    elemHasDigit = False
    for char in elem:
        if char.isdigit():
            elemHasDigit = True
            break
    if elemHasDigit:
        print(f'the position is: {cnter}, {elem}')
        break


    cnter += 1
 


