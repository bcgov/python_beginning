# create a dictionary with the following key value pairs
# -------------------
# key       | value
# -------------------
# ANA  |   Anaheim Ducks
# ARI  |   Arizona Coyotes
# BOS  |   Boston Bruins
teamDict = {'ANA': 'Anaheim Ducks',
            "ARI":  "Arizona Coyotes",
            "BOS":  "Boston Bruins"
            }


# Add an element to the dictionary
# MTL |  Montréal Canadiens
teamDict['MTL'] = 'Montréal Canadiens'

# Modify the value associated with the key BOS to 'disgrace'
teamDict['BOS'] = 'disgrace'
teamDict['BOS'] = None


#del teamDict['BOS']
print(teamDict['BOS'])


header= ['col1', 'col2', 'col3']
dataLine = ['Kevin', 'Tony', 'Frank']

lineDict = {}
for indexPos in range(0, len(header)):
    keyVal = header[indexPos]
    data = dataLine[indexPos]
    
    lineDict[keyVal] = data
print(lineDict)
theData = lineDict['col3']
print(f'column 3 contains the data{theData}')


complextStruct = {
    'team': 'montreal',
    'players': [
        {
            'fullname': 'Kevin Netherton',
            'playerSalery': 10000000,
            'position': 'R'
        }, 
        {   'fullname': 'Scott Sharp', 
            'playerSalery': 235000000,
            'position': 'C'
        }
    ],
    'coaches': [
        {"fullname": 'Claude Julien', 
         "coacheType": "head coach"
        },
        {'fullname': 'Kirk Muller',
         'coacheType': 'assistant coach'
        }, 
        {'fullname': 'Stephane Waite', 
         'coacheType': "goalie coach"
        },
        {'fullname': 'Dominique Ducharme', 
         'coacheType': "assistant coach"}
    ]
}

# what is the second players position on the great montreal canadiens.
answer1 = complextStruct['players'][0]['playerSalery']
print(f'survey says ...{answer1}' )

# write a loop that prints the names of the all the assistant coaches
assistantCoachNames = []
for coach in complextStruct['coaches']:
    coachtype = coach['coacheType']
    coachName = coach['fullname']
    if coachtype == 'assistant coach':
        assistantCoachNames.append(coachName)
    print(coach)

print(f'the assistant coaches are {assistantCoachNames}')