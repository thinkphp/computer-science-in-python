# Trei operatori de comparare: <, >, ==
# lt = less than
# gt = greater than
# eq = equal
#
class Intreg:
    def __init__(self, a, b, c):
        #avem o singura data membra cu numele "a"
        self.a = a # am initializat si folosesc data membra
        self.b = b # am initializat dar nu o folosesc in algoritm
        self.c = c # am initializat dar nu o folosesc in algoritm
    #supraincare operator <
    # metoda magica care supraincarca operatorul less than
    def __repr__(self):

        return "DATA MEMBER a = " + str(self.a)

    def __lt__(self, other):

        if self.a < other.a:

            return "ob1 < ob2 (the ob1 is less than ob2)"

        elif self.a > other.a:

            return "ob1 > ob2 (the ob2 is less than ob1)"

        else:
            return "ob1 == ob2 (the ob2 is equal with ob1)"

    def __gt__(self, other):

        if self.a > other.a:
            return "ob1 > ob2 (the ob1 is greater than ob2)"
        elif self.a < other.a:
            return "ob1 > ob2 (the ob2 is greater than ob1)"
        else:
            return "ob1 == ob2 (the ob2 is equal with ob1)"

    def __eq__(self, other):
        if self.a == other.a:
           return "EGALE"
        else:
           return "Nu sunt egale"

def main():

    #am declarat un obiect de tip Intreg sau de clasa Intreg cu data membra a = 8
    obiect1 = Intreg( 18, 1, 2)
    print(obiect1)

    # al doilea obiect este de tip Intreg si va initializa data membra cu 7
    obiect2 = Intreg( 7, 3, 4)
    print(obiect2)

    print(obiect1 < obiect2)  # se apeleaza def __lt__(self, other):
    print(obiect1 > obiect2)  # def __gt__(self, other):
    print(obiect1 == obiect2) # def __eq__(self, other):

main()
