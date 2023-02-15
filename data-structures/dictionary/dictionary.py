def database():

        global myDic
        myDic = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Brazil": "Brasil",
        "Bolovia":"La Paz",
        "Columbia": "Bogota",
        "Venezuela": "Caracas",
        "Ecuador":"Quito",
        "Paraguay": "Asunsion",
        "Uruguay": "Montevideo",
        "French Guyana": "Cayenne",
        "Suriname": "Paramaribo",
        "Guyana": "Georgetown",
        "Peru": "Lima"
        }

def get2(string):

    for key, value in myDic.items():

        if key == string.capitalize():

            return value

    return "This key does not exist!"

def get3(string):

    return myDic.get(string)

def get(string):

    for key, value in myDic.items():

        if value == string:

            return key

    return "Does not exist this entry"

def func():

    database()

    print("List of South America Countries and Capitals")
    country = str(input("Country = "))

    capital = get2(country)

    print(capital)
func()
