'''
Se citesc doua numere naturale n1 si n2. Se cere sa se calculeze catul
si restul impartirii intregi a lui lui n1 la n2 fara a utiliza operatori de
imparatire. doar structura repetitiva while.

Cum procedam?

Exemplu numeric:

n1 = 10
n2 = 3

10 - 3 >= 0 n1 = n1- n2 = 7; C = 1
7 - 3 >= 0 n1 = n1 - n2 = 4; C = 2
4 - 3 >= 9 n1 = 4 - 3 = 1; C = 3
1 - 3 < 0, se iese din structura repetitiva si se afiseaza pe ecran catul si restul 1

in limbajul pseudocod, natural:

intreg n1, n2, c
Citim de la tastatura n1 si n2
c <-- 0

Cat timp n1 - n2 >= 0 executa

  c = c + 1
  n1 = n1 - n2

Scrie pe ecran c, n1

'''

def impartire():

    n1 = int(input("n1 = "))
    n2 = int(input("n2 = "))

    catul = 0

    while n1 - n2 >= 0:

        catul = catul + 1 #catul += 1

        n1 = n1 - n2

    print("catul = ", catul)

    print("restul = ", n1)

impartire()
