stringList = ['ama', 'aa', 'ab', 'abc', 'bad', 'lol', 'dog', 'cat', 'a', 'f', 'x']
# Given the list of strings "stringList", return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

count = 0
answerList = []
for word in stringList:
    if len(word) >= 2:
        firstChar = word[0]
        lastChar = word[-1]
        if firstChar == lastChar:
            count += 1
            answerList.append(word)
print(f'answer is: {count}: elems are: {answerList}')




inputList = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# # Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

xList = []
otherList = []
for elem in inputList:
    if 'x' == elem[0]:
        xList.append(elem)
    else:
        otherList.append(elem)

xList.sort()
otherList.sort()
finalUnnecessarySortedListFromHll = xList[:]
#finalUnnecessarySortedListFromHll = xList.copy()

finalUnnecessarySortedListFromHll.extend(otherList)
print(f'sorted list is {finalUnnecessarySortedListFromHll}')

# create a while loop that iterates through the list "inputList" until it finds a string that 
# contains a number
# * Hint: take a look at the string methods here to find the correct method.
#      https://docs.python.org/3/library/stdtypes.html#string-methods

returnValue = None
inputList = ['aba', 'xyz', 'aa', 'x', 'bbb', '', 'x', 'xy', 'xyx', 'xx', '234','aaa', 'be', 'abc', 'hello']
for someDamnText in inputList:
    for character in someDamnText:
        if character.isdigit():
            returnValue = someDamnText
            break
    if returnValue is not None:
        break
print(returnValue)

returnValue = None
inputList = ['aba', 'xyz', 'aa', 'x', 'bbb', '', 'x', 'xy', 'xyx', 'xx', 'aaa', 'be', 'abc', 'hello']
#for someDamnText in inputList:

counter = 0
found = False
while counter < len(inputList) and not found:
    someDamnText = inputList[counter]
    for character in someDamnText:
        if character.isdigit():
            returnValue = someDamnText
            found = True
    counter += 1
print(f"returnValue: {returnValue}")









