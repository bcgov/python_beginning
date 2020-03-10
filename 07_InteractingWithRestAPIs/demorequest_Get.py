import requests
import urllib
import json

# The root url for api calls. 
# for url joining... make sure ends with a '/'
rootUrl = 'https://api.github.com/'

# specific end point.
# if you have a github account you can put your name in here..
user = 'franTarkenton'
endpoint = f'users/{user}/gists'
# glue the root url and end point together... (make sure root url has a trailing / or this won't work as expected)
dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
print(f'dstUrl: {dstUrl}')

headers = {'Accept': 'application/json'}

# making a get request
resp = requests.get(dstUrl, headers=headers)
# print the status_code
print(f'status code: {resp.status_code}')

# get the actual data from the request object
jsonData = resp.json()

# dump the data to a file
# a lot of data so dump to file for inspection
outFile = f'github_{user}_gists.json'
with open(outFile, 'w') as fh:
    json.dump(jsonData, fh, sort_keys=True, indent=4)
print(f"num gists returned: {len(jsonData)}")