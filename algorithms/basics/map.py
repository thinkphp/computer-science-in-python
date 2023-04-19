class Person(object):

    def __init__(self, name, mountain, rank):
        self.name = name
        self.mountain = mountain
        self.rank = rank

    def __repr__(self):
        return self.name + " "+ self.mountain + " " + str(self.rank)

def update(person):
    person.rank += 1
    return person

def func():

    mountaineer1 = Person("Adrian","Bucegi", 1)
    mountaineer2 = Person("Dustin","Piatra Craiului", 10)
    mountaineer3 = Person("David","Fagaras", 11)
    mountaineer4 = Person("Scott","Retezat", 100)
    mountaineer5 = Person("Jurek","Buila Vanturita", 110)

    mountaineers = [ mountaineer1, mountaineer2, mountaineer3, mountaineer4, mountaineer5 ]

    for m in mountaineers:

        print( m )

    print()
    
    mountaineers = map(update, mountaineers)

    for m in mountaineers:

            print( m )
func()
