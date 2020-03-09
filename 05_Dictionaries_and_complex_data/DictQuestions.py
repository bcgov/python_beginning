'''
Dictionary Questions

'''

# Step 1.
# import the json data contained in the file ../data/players_t8.json

# Step 2. 
# verify that your data import was successful by printing the first player in the struct

# Step 3. 
# create an iteration that iterates over each player

# Step 4. 
# create a new list, and populate it with players that are from canada.
import json
import sys

jsonFile = r'C:\training\python\data\players_t8.json'
with open(jsonFile, 'r') as playerFH:
    playerData = json.load(playerFH)

firstPlayer = playerData['data'][0]
#print(f'first player data is: {firstPlayer}')


canadianPlayerList = []
playerListOfDicts = playerData['data']

for playerDict in playerListOfDicts:
    # going to use 'nationality' to identify canadians
    
    playerNationality = player['nationality']
    playerName = player['fullName']
    if playerNationality == 'CAN':
        canadianPlayerList.append(playerName)
    
print(f"There are {len(canadianPlayerList)}")
canadianPlayerString = '\n'.join(canadianPlayerList)
print(f"the canadians are: {canadianPlayerString}")





