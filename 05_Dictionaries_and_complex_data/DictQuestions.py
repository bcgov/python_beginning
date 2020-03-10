'''
Dictionary Questions

'''
import json
import os.path

dataDir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '..', 'data'))

jsonFile = os.path.join(dataDir, 'players_t8.json')

with open(jsonFile) as jsonFH:
    playerdata = json.load(jsonFH)


# first player in struct
playerdata['data'][0]
canadianPlayers = []
for player in playerdata['data']:
    if player['nationality'] == 'CAN':
        canadianPlayers.append(player['fullName'])

#print(f'canadian players: {len(canadianPlayers)}')
#print(f'the total number of player is {len(playerdata["data"])}')
# Step 1.
# import the json data contained in the file ../data/players_t8.json

# Step 2. 
# verify that your data import was successful by printing the first player in the struct

# Step 3. 
# create an iteration that iterates over each player

# Step 4. 
# create a new list, and populate it with players that are from canada.

jsonFile = r'C:\Kevin\proj\python_training\data\teams.json'
with open(jsonFile) as jsonFH:
    playerdata = json.load(jsonFH)

print(playerdata['teams'][0]['venue']['timeZone']['id'])