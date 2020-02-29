'''
* demo concept that module can be an executable as well as a library 
  by organizing this way.
'''

def addUptheNums(inList):
    """
    :param inList: a list of numbers.  The list must only contain 
                   numbers
    :return: the sum of all the number in the input list
    """
    sum = 0
    for num in inList:
        sum = sum + num
    return sum

def convertToNums(inList):
    """
    :param inList: a list of numbers that may be strings or some other type

    :return: the int representation of the strings
    """
    newList = []
    for inParam in inList:
        newList.append(float(inParam))
    return newList

if __name__ == '__main__':
    # these lines call the actual function without 
    # these lines we only have a function definition
    newSum = addUptheNums([34, 23, 22, 7889, 23,1, 3, 877])
    print(f"the sum is {newSum}")
