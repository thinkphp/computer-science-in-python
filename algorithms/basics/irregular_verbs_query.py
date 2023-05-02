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
    "a":[{"the verb":"past tense, past participle"},
         {"to arise":"arose, arisen => aparea"},
         {"to awake":"awoke, awoke => a se trezi"}],
    "b":[{"the verb":"past tense, past participle"},
         {"to be":"was, been => a fi"},
         {"to bear":"bore, born => to give birth"},
         {"to bear":"bore, borne => a purta"},
         {"to beat":"beat, beaten => a bate"},
         {"to bear":"bore, borne => a deveni"},
         {"to begin":"began, begun => a incepe"},
         {"to bend":"bent, bent => a indoi"},
         {"to bind":"bound bound => a lega"},
         {"to bite":"bite, bitten => a musca"},
         {"to blew":"blew, blewen => a sufla"},
         {"to break":"broke, broken => a sparge"},
         {"to breed":"bred, bred => a creste"},
         {"to bring":"brought, brought => a aduce"},
         {"to broadcast":"broadcast, broadcast => a radiodifuza"},
         {"to build":"built, built => a construi"},
         {"to burn":"burnt, burnt => a arde"},
         {"to buy":"bought, bought => a cumpara"},
         {"to burst":"burst, burst => a cumpara"},
         ],

    }

def func():
    database()

    ch = 'y'
    while ch == 'y':
      intro = "Welcome to my App Irregular Verbs\nWith passion and love for May Ann Campanera\nSearch for a letter:"
      letter = input(intro)
      if letter in dictionary.keys():
         get(letter)
      else:
         print("Not Found.")
      ch = input("Do you want more? y/n?")
func()
