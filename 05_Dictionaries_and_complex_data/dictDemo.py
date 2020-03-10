# create a dictionary with the following key value pairs
#-------------------
# key       | value
#-------------------
# ANA  |   Anaheim Ducks
# ARI  |   Arizona Coyotes
# BOS  |   Boston Bruins
hockeyTeambySinan = {'ANA': 'Anaheim Ducks', 'ARI': 'Arizona Coyotes',
      'BOS': 'Boston Bruins'}


# Add an element to the dictionary
# MTL |  Montréal Canadiens
hockeyTeambySinan['MTL'] = 'Montréal Canadiens'

# Modify the value associated with the key BOS to 'disgrace'
hockeyTeambySinan['BOS'] = 'disgrace'
del hockeyTeambySinan['BOS']


def demoDict():
    ## Using conditional statements with Dictionaries
    simpleDict = {'ANA': 'Anaheim Ducks',
                'ARI': 'Arizona Coyotes',
                'BOS': 'Boston Bruins',
                'BUF': 'Buffalo Sabres',
                'CAR': 'Carolina Hurricanes'}
    for keyval in simpleDict:
        print(f'keyval: {keyval}')
        if keyval == 'ANA':
            print(f'found the ducks {keyval}')
        elif simpleDict[keyval] == 'Boston Bruins':
            print(f'terrible!  just terrible')
        else:
            print(f"team key is {keyval}, teamValue is {simpleDict[keyval]}")

demoDict()
