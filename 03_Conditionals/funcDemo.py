'''
def getMiddleCharacter(inputVar):
    position = len(newVar) / 2
    positionInt = int(position)
    return inputVar[positionInt]
middle = getMiddleCharacter('Victor Mete')
# can I print the variable 'positionInt' here?  why or why not.
'''

franchiseAbbrev = ['MTL', 'CHI', 'BOS', 'WPG', 'CGY', 'EDM', 'VAN', 'OTT']
# how do i get a list from WPG forward
franchiseAbbrev[3:]
# how do I refer to the element OTT
franchiseAbbrev[-1]

# how do I refer to the element MTL
franchiseAbbrev[0]

# create a function that iterates through all of the above and returns elements with the letter 't'

def getElemsWith_t(inputList):
    tElemsLst= []
    for elem in inputList:
        if 't' in elem.lower():
            tElemsLst.append(elem)
    return tElemsLst

franchiseAbbrev = ['MTL', 'CHI', 'BOS', 'WPG', 'CGY', 'EDM', 'VAN', 'OTT']
withT = getElemsWith_t(franchiseAbbrev)
print(f'with t is: {withT}')

# delete the elements BOS and CGY from the list
#del franchiseAbbrev[2]
#del franchiseAbbrev[3]
#print(franchiseAbbrev)

def removeBad(inputlist, toRemove):
    newList = []
    for elem in inputlist:
        if elem not in toRemove:
           newList.append(elem)
    return newList

franchiseAbbrev = ['MTL', 'CHI', 'BOS', 'WPG', 'CGY', 'EDM', 'VAN', 'OTT']
team2Remove = ['BOS', 'CGY']
NoBad = removeBad(franchiseAbbrev, team2Remove)
print(NoBad)





