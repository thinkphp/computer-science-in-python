def display_database():
  for key, value in dictionary.items():
    print("%s %s" % (key, value))


def get(search):
  resultset = dictionary.get(search)
  for i in resultset:
    print(i)


def database():
  global dictionary
  dictionary = {
    "a": [{
      "the verb": "past tense, past participle"
    }, {
      "to arise": "arose, arisen => aparea"
    }, {
      "to awake": "awoke, awoke => a se trezi"
    }],
    "b": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to be": "was/were, been => a fi"
      },
      {
        "to bear": "bore, born => to give birth"
      },
      {
        "to bear": "bore, borne => a purta"
      },
      {
        "to beat": "beat, beaten => a bate"
      },
      {
        "to bear": "bore, borne => a deveni"
      },
      {
        "to begin": "began, begun => a incepe"
      },
      {
        "to bend": "bent, bent => a indoi"
      },
      {
        "to bind": "bound bound => a lega"
      },
      {
        "to bite": "bite, bitten => a musca"
      },
      {
        "to blew": "blew, blewen => a sufla"
      },
      {
        "to break": "broke, broken => a sparge"
      },
      {
        "to breed": "bred, bred => a creste"
      },
      {
        "to bring": "brought, brought => a aduce"
      },
      {
        "to broadcast": "broadcast, broadcast => a radiodifuza"
      },
      {
        "to build": "built, built => a construi"
      },
      {
        "to burn": "burnt, burnt => a arde"
      },
      {
        "to buy": "bought, bought => a cumpara"
      },
      {
        "to burst": "burst, burst => a exploda"
      },
    ],
    "c": [{
      "the verb": "past tense, past participle"
    }, {
      "to cast": "cast, cast => a arunca"
    }, {
      "to catch": "caught, caught => a prinde"
    }, {
      "to choose": "chose, chosen => a alege"
    }, {
      "to cling": "clung, clung => a se agata"
    }, {
      "to come": "came, came => a veni"
    }, {
      "to cost": "cost, cost => a costa"
    }, {
      "to creep": "crept, crept => a se tara"
    }, {
      "to cut": "cut, cut => a taia"
    }],
    "d": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to deal": "dealt,dealt => a avea de-a face"
      },
      {
        "to dig": "dug, dug => a sapa"
      },
      {
        "to do": "did, done => a taia"
      },
      {
        "to draw": "drew, drown => a desena"
      },
      {
        "to dream": "dreamt(dreamed),dreamt(dreamed) => a visa"
      },
      {
        "to drink": "drank, drunk => a desena"
      },
      {
        "to drive": "drove, droven => a conduce"
      },
      {
        "to dwell": "dwelt, dwelt => a locui"
      },
    ],
    "e": [{
      "the verb": "past tense, past participle"
    }, {
      "to eat": "ate, eaten => a manca"
    }],
    "l": [{
      "the verb": "past tense, past participle"
    }, {
      "to leave": "left, left => a manca"
    }, {
      "to let": "let, let => a permite"
    }, {
      "to lose": "lost, lost => a pierde"
    }, {
      "to lend": "lent, lent => a imprumuta"
    }, {
      "to lay": "laid, laid => a aseza"
    }, {      
      "to lean": "leant, leant => a inclina"
    }],
    "m": [{
      "the verb": "past tense, past participle"
    }, {
      "to meet": "met, met => a intalni"
    }, {
      "to mean": "meant, meant => a insemna"
    }],
    "u": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to understand": "understood, understood => a intelege"
      },
    ],
    "t": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to tell": "told, told => a spune"
      },
      {
        "to teach": "taught, taught => a preda"
      },
      {
        "to take": "took, taken => a lua"
      },
      {
        "to throw": "threw, thrown => a arunca"
      },
    ],
    "w": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to write": "won, won => a castiga"
      },
      {
        "to win": "won, won => a castiga"
      },
      {
        "to wear": "wore, worn => a purta"
      },
    ],
    "p": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to pay": "paid, paid => a plati"
      },
      {
        "to put": "put, put => a pune"
      },
    ],
    "r": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to run": "ran, run => a alerga"
      },
      {
        "to read": "read, read => a citi"
      },
      {
        "to ring": "rang, rung => a suna"
      },
    ],
    "s": [
      {
        "the verb": "past tense, past participle"
      },
      {
        "to speak": "spoke, spoken => a spune"
      },
      {
        "to sit": "sat, sat => a sta"
      },
      {
        "to send": "sent, sent => a trimite"
      },
      {
        "to see": "saw, seen => a vedea"
      },
      {
        "to say": "said, said => a spune"
      },
      {
        "to sell": "sold, sold => a vinde"
      },
      {
        "to sleep": "slept, slept => a vinde"
      },
      {
        "to sink": "sank, sunk => a scufunda"
      },
      {
        "to sing": "sang, sung => a scufunda"
      },
      {
        "to shut": "shut, shut => a scufunda"
      },
      {
        "to spend": "spent, spent => a cheltui"
      },
      {
        "to show": "showed, showed/showen => a arata"
      },
    ],
    "f": [{
      "the verb": "past tense, past participle"
    }, {
      "to freeze": "froze, frozen=> a ingheta"
    }, {
      "to forbid": "forbade, forbidden=> a interzice"
    }, {
      "to forget": "forgot, forgotten=> a uita"
    }],
    "k": [{
      "the verb": "past tense, past participle"
    }, {
      "to keep": "kept, kept => a pastra"
    }]
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
