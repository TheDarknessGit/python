import json, urllib2

response = urllib2.urlopen("http://data.police.uk/api/crimes-street/all-crime?lat=52.137837&lng=-0.898248&date=2017-01")

crimes = json.loads(response.read())

def crime_finder(crime):
    #if "Stafford" in crime['location']['street']['name']:
        print crime['category'] + ' ' + crime['location']['street']['name']
        print crime['location']['longitude']
        print crime['location']['latitude']

for crime in crimes:
    crime_finder(crime)
    

