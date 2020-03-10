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
# how would I refer to the position of the second players on the team montreal
print(f"the team is {complextStruct['team']}")
print(complextStruct['players'][1]['position'])

# write a loop that prints the names of the all the assistant coaches
assistCoachList = []
for coachDict in complextStruct['coaches']:
    print(coachDict)
    # print just the coach name
    print(f"coach name is {coachDict['fullname']}")
    if coachDict['coacheType'] == 'assistant coach':
        assistCoachList.append(coachDict['fullname'])

    # getting the assistant coaches
print(f'assistant coaches are: {assistCoachList}')
