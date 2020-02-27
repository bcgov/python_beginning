# http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/

# requests module docs: https://requests.readthedocs.io/en/master/

import requests
import os.path
import pprint
import urllib
import json

PP = pprint.PrettyPrinter(indent=4)

rootUrl = 'https://records.nhl.com/site/api/'
endpoint = '/franchise-team-totals'


rootUrl = 'https://statsapi.web.nhl.com/api/v1/'
endpoint = 'teams'


# why use this method instead of string concat!
# - its more robust.. don't have to worry about if the url end or starts with a slash
# - does it all for you
# - avoids re-inventing the wheel
dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
print(f'dstUrl: {dstUrl}')
'''
resp = requests.get(dstUrl)
print(f'status_code is: {resp.status_code}')
jsonResp = resp.json()
newDict = {}
for team in jsonResp['teams']:
    newDict[team['abbreviation']] = team['name']

print('-'*30)
print(pprint.pformat(newDict))

endpoint = 'statTypes'
#https://statsapi.web.nhl.com/api/v1/statTypes 
dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
resp = requests.get(dstUrl)
jsonResp = resp.json()
print(pprint.pformat(jsonResp))
'''

def getFranchises():
    endpoint = f'franchise'
    rootUrl = 'https://records.nhl.com/site/api/'
    dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
    print(f"dstUrl: {dstUrl}")
    resp = requests.get(dstUrl)
    jsonData = resp.json()
    PP.pprint(jsonData)
        

def getTeams():
    endpoint = f'teams'
    rootUrl = 'https://statsapi.web.nhl.com/api/v1/'
    dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
    print(f"dstUrl: {dstUrl}")
    resp = requests.get(dstUrl)
    jsonData = resp.json()

    #PP.pprint(resp.json())
    teamIdLookup = {}
    for teamData in jsonData['teams']:
        teamIdLookup[teamData['id']] = teamData['name']

    PP.pprint(teamIdLookup)

def getPlayersByTeam(team):
    endpoint = f'player/byTeam/{team}'
    # for urljoin to work must have a / at the end of the rootUrl
    rootUrl = 'https://records.nhl.com/site/api/'
    dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
    print(f'dstUrl: {dstUrl}')
    header = {"Content-Type": "application/json",
            "Accept": "application/json", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0" }
    resp = requests.get(dstUrl, headers=header)
    jsonData = resp.json()

    with open(f'players_t{team}.json', 'w') as outfile:
        json.dump(jsonData, outfile)
    names = {}

    for playerData in jsonData['data']:
        if not names:
            PP.pprint(playerData)
        names[playerData['fullName']] = playerData

    namesList = names.keys()
    namesList = list(namesList)
    print(f"type: {type(namesList)}")
    namesList.sort()
    print('\n'.join(namesList))

if __name__ == '__main__':
    #getTeams()
    # mtrl = 8
    getPlayersByTeam('8')