import json, urllib2

response = urllib2.urlopen("http://data.police.uk/api/crimes-street/all-crime?lat=52.587846&lng=-2.126226&date=2017-01")


#woodside http://data.police.uk/api/crimes-street/all-crime?lat=52.651725&lng=-2.485432&date=2017-01
#home http://data.police.uk/api/crimes-street/all-crime?lat=52.6861541&lng=-2.4676499&date=2017-01

#print response.read()
#response = open(nameofFile, read/write)

crimes = json.loads(response.read())

def crime_finder(crime):
    #if "Stafford" in crime['location']['street']['name']:
        print crime['category'] + ' ' + crime['location']['street']['name']
        print crime['location']['longitude']
        print crime['location']['latitude']

for crime in crimes:
    crime_finder(crime)
    

