import json

f = open('example4.txt', 'r+')
x = json.load(f)
print(x["firstName"])
