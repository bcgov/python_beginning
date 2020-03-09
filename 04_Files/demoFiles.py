
'''
## Exercise:
* create a function that recieves a file path
* the function opens the file and...
* iterates over every line in the file...
* identify lines in the file that represent teams from the 'Central' division...
* creates a new list for teams in the central division...
* after all the central teams have been collected they are sorted...
* returns the sorted list
* call the function
'''

def getCentralTeams(teamsFilePath):
    divisionPostion = -2
    isHeader = True
    returnList = []
    with open(teamsFilePath, 'r') as teamsFh:
        for teamLine in teamsFh:
            if isHeader:
                header = teamLine
                isHeader = False
            else:
                teamList = teamLine.split(',')
                teamDivision = teamList[divisionPostion]
                teamname = teamList[1]
                if teamDivision.lower() == 'Central'.lower():
                    returnList.append(teamname)
    returnList.sort()
    return returnList

if __name__ == '__main__':
    teamsfilePath = r'C:\training\python\data\teams.csv'
    # centralTeams = getCentralTeams(teamsfilePath)
    # teamString = '\n'.join(centralTeams)
    # print(f"centralTeams: {teamString}")

    print(f'the file path is: {__file__}')
    