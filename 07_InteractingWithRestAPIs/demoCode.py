# http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/

# requests module docs: https://requests.readthedocs.io/en/master/

import requests
import os.path
import pprint
import urllib
import codecs
import json
import requests.auth

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
# add to get player
roster?season={season}
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

    with codecs.open('data/teams.json', 'w', "utf-8") as outfile:
        json.dump(jsonData, outfile)

    return jsonData


def getteamIds():
    teamData = getTeams()
    teamIds = []
    for team in teamData['data']:
        teamIds.append(team['id'])
    return teamIds

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

    with codecs.open(f'players_t{team}.json', 'w', "utf-8") as outfile:
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

def getAllPlayers():
    teamids = getteamIds()
    print(teamids)
    for teamID in teamids:
        pass
        

def createTeamsCSV():
    outFile = 'data/teams.csv'
    fh = codecs.open(outFile, 'w', 'utf-8')
    teamsData = getTeams()
    csvHeader = ['id', 'name', 'arena', 'city', 'abbrev', 
                 'teamName', 'location', 'inceptionYear', 
                 'division', 'conference']
    fh.write(','.join(csvHeader) + '\n')
    for teamData in teamsData['teams']:
        lineList = []
        lineList.append(teamData['id'])
        lineList.append(teamData['name'])
        lineList.append(teamData['venue']['name'])
        lineList.append(teamData['venue']['city'])
        lineList.append(teamData['abbreviation'])
        lineList.append(teamData['teamName'])
        lineList.append(teamData['locationName'])
        lineList.append(teamData['firstYearOfPlay'])
        lineList.append(teamData['division']['name'])
        lineList.append(teamData['conference']['name'])
        for elemPos in range(0, len(lineList)):
            lineList[elemPos] = str(lineList[elemPos])
            

        lineStr = ','.join(lineList)
        print(f"lineList {','.join(lineList)}")
        if lineList:
            fh.write(','.join(lineList) + '\n')
    fh.close()


class GithubAPI():

    def __init__(self):
        self.rootUrl = 'https://api.github.com/'
        self.pac = os.environ['GHTOKEN']

    def getHeader(self):
        header = ""

    def getUserRepos(self, user):
        endPoint = 'users/franTarkenton/repos'
        fullUrl = urllib.parse.urljoin(self.rootUrl, endPoint)
        print(f"fullUrl: {fullUrl}")

        resp = getUserRepos

    def getGists(self, user):
        endPoint = f'users/{user}/gists'
        fullUrl = urllib.parse.urljoin(self.rootUrl, endPoint)
        print(f"fullUrl: {fullUrl}")
        resp = requests.get(fullUrl)
        print(f'status_code: {resp.status_code}')
        gistData = resp.json()
        #PP.pprint(gistData)
        print(f"num recs={len(gistData)}")

    def getGistsWithAuth(self, user):
        endPoint = f'users/{user}/gists'
        fullUrl = urllib.parse.urljoin(self.rootUrl, endPoint)
        print(f"fullUrl: {fullUrl}")
        auth=requests.auth.HTTPBasicAuth(user, self.pac)
        resp = requests.get(fullUrl, auth=auth)
        print(f'status_code: {resp.status_code}')
        gistData = resp.json()
        #PP.pprint(gistData)
        print(f"num recs={len(gistData)}")


    #https://api.github.com/users/franTarkenton/repos

if __name__ == '__main__':
    #getTeams()
    #createTeamsCSV()
    # mtrl = 8
    #getPlayersByTeam('8')

    #getAllPlayers()
   
    gapi = GithubAPI()
    #gapi.getGists('franTarkenton')
    gapi.getGistsWithAuth('franTarkenton')

    
    #getFranchises()

    # mtl = 1
    #