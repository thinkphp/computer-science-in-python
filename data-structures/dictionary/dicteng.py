def display_database():
    for key, value in dictionary.items():
        print("%s %s" % (key,value))

def get(search):
    resultset = dictionary.get(search)
    for i in resultset:
        print(i)

def database():
    global dictionary
    dictionary = {
    "a":[{"abbreviate":"xx-xx-xx"},
         {"abduct":"asdasd"},
         {"abecedarian":"asdasd"},
         {"abasement":"asdas"},
         {"aback":"asdasd"},
         {"ability":"asdas"},
         {"abnegation":"asdasd"}],
    "b":[{"bean":"asdasd"},
         {"base":"asdasd"},
         {"base-minded":"asdasd"},
         {"base-spirited":"asdasdsa"},
         {"bash":"asdasda"},
         {"bashfulness":"asdasdas"},
         {"basically":"asdasdas"},
         {"belief":"asdasdas"},
         {"believer":"asdasd"},
         {"beneath":"asdasdas"}],
    "c":[{"calculus":"asd"},
         {"cage":"asdas"},
         {"caddie":"asdas"},
         {"candid":"asdas"},
         {"cancel":"Asdas"},
         {"canyon":"ASdasd"}]
    }

def func():
    database()

    ch = 'y'
    while ch == 'y':
      letter = input("Letter of Alphabet = ")
      if letter in dictionary.keys():
         get(letter)
      else:
         print("Not Found.")
      ch = input("Do you want more? y/n?")
func()
