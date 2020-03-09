# 
def getMiddleCharacter(inputVar):
    position = len(inputVar) / 2
    positionInt = int(position)
    return inputVar[positionInt]

middle = getMiddleCharacter('Victor Mete')
# can I print the variable 'positionInt' here?  why or why not.

franchiseAbbrev = ['MTL', 'CHI', 'BOS', 'WPG', 'CGY', 'EDM', 'VAN', 'OTT']
# how do i get a list from WPG forward
franchiseAbbrev[3:]
# how do I refer to the element OTT
# how do I refer to the element MTL

# create a function that iterates through all of the above and returns elements with the letter 't'

def getT(franchiseAbbrev):
    returnList = []
    for elem in franchiseAbbrev:
        if 'T' in elem.upper():
            returnList.append(elem)
    return returnList

withT = getT(franchiseAbbrev)
print(withT)

# delete the elements BOS and CGY from the list
franchiseAbbrev = ['MTL', 'CHI', 'BOS', 'WPG', 'CGY', 'EDM', 'VAN', 'OTT']
garbageList = ['BOS', 'CGY']
print(f'fixed: {set(franchiseAbbrev) - set(garbageList)}')
del franchiseAbbrev[2]

del franchiseAbbrev[3]
print(f'fixed list is: {franchiseAbbrev}')
