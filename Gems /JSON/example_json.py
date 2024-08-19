'''
JSON

JavaScript Object Notation este un format de schimb de date usor si text-based
folosit pentru a reprezenta structuri de date si obiecte.
Este adesea utilizat pentru a trimite date intre client si server in aplicatii web si pentru a stoca date in fisier sau baze date.
'''

import json

# un dictionar ca va fi salvat intr-un fisier json
data = {

     "name": "David",
     "age": 20,
     "town": "Bv",
     "job": "coder"
}

print(data)

#salvarea dictionarului intr-un fisier JSON
with open("data.json","w") as file:
    json.dump(data, file, indent=4)


#incarcarea dictionarului din fisier JSON
with open("data.json","r") as file:
    loaded_data = json.load( file )
    print(loaded_data)


# json
x = '{ "name": "David", "age": 20, "city": "Bv"}'

# convertim x la un dictionar python3
y = json.loads( x )

print(type(y))
#rezultatul este un Dictionar Python
print(y["age"])
print(y["name"])
print(y["city"])
