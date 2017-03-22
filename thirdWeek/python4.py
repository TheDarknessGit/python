import json

person = {}
person["firstName"] = "Dayle"
person["surname"] = "Warfield"
person["gender"] = "Male"

f = open('example4.txt', 'a')

json.dump(person, f)

#f.write(str(person) + '\n')

f.close()
