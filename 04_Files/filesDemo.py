'''
* create a function that recieves a file path
* the function opens the file and...
* iterates over every line in the file...
* identify lines in the file that represent teams from the 'Central' division...
* creates a new list for teams in the central division...
* after all the central teams have been collected they are sorted...
* returns the sorted list
* call the function
'''


def getCentralTeams(teamsFile):
    returnList = []
    with open(teamsFile, 'r') as fh:
        firstLine = True
        for line in fh:
            if firstLine:
                firstLine = False
                continue
            line = line.strip()
            lineList = line.split(',')
            if lineList[-2].lower() == 'central':
                returnList.append(lineList[1])
                print(lineList)
    
            #print(line)
    return returnList
    

teamsFilePath = r'C:\Kevin\proj\python_training\data\teams.csv'

centralTeams = getCentralTeams(teamsFilePath)
print(centralTeams)

