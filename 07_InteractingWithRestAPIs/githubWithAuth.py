import requests
import urllib
import json
import pprint
import os

# The root url for api calls. 
# for url joining... make sure ends with a '/'
rootUrl = 'https://api.github.com/'

# specific end point.
# if you have a github account you can put your name in here..
user = 'franTarkenton'
endpoint = f'gists'
# glue the root url and end point together... (make sure root url has a trailing / or this won't work as expected)
dstUrl = urllib.parse.urljoin(rootUrl, endpoint)
print(f'dstUrl: {dstUrl}')

# authentication
personalAccessToken = os.environ['GHTOKEN']
auth=requests.auth.HTTPBasicAuth(user, personalAccessToken)

# params
# get the contents of the file to upload
with open('07_InteractingWithRestAPIs/dummyGist.md') as fh:
    dummyGistContent = fh.read()

#dummyGistContent = dummyGistContent.replace('\n', r'\n')
print(f"dummyGistContent: {dummyGistContent}")

createGistParams = {
    "description": "a long long time ago",
    "public": True,
    "files": {
        "dummyGist.md": {
            "content": dummyGistContent
        }
    }
}
# making a post request
resp = requests.post(dstUrl, json=createGistParams, auth=auth)
# print the status_code
print(f'status code: {resp.status_code}')

# get the actual data from the request object
jsonData = resp.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(jsonData)
