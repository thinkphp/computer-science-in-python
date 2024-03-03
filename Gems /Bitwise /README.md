Reprezentarea interna a numerelor intregi
-----------------------------------------

Z = {+-,+-2,+-3,....}

Reprezentarea in memorie a numerelor intregi se face printr-o secventa de cifre 0 si 1. Aceasta secventa  poate avea o lungime de 8 biti, 16biti sau 64 de biti.

Forma de memorare a intregilor se numeste cod complementar. In functie de lungimea reprezentarii se stabileste domeniul valorilor care pot fi stocate.

a = 8

Modul de reprezentare (in cod complementar) va fi prezentat in cele ce urmeaza, folosind reprezentarea pe 8 biti, valabila pentru tipul char din C/C++/JAVA/Python.

```
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _

7 6 5 4 3 2 1 0

bit de semn:

- 0 daca numarul este pozitiv
- 1 daca numarul este negativ
```

Se observa ca numerotarea pozitiilor se face de la dreapta la stanga (de la 0 la 7),pozitia 7 fiind rezervata pentru bitul de semn (0 pentru numerele pozitive si 1 pentru numerele negative). REzulta ca doar 7 biti (pozitiile 0 - 6) se folosesc pentru reprezentarea valorii absolute a numarului. (-20 => valoarea absoluta este 20).

Numerele intregi pozitive se convertesc in baza 2 si se face complementarea cu cifre 0 nesemnificative pana la completarea celor 7 biti.

Spre exemplu luam numarul 8 in baza 10. Si dorim sa-l convertim in baza 2.
```

               /\ 
8:2 = 4 rest 0 ||
4:2 = 2 rest 0 ||
2:2 = 1 rest 0 ||
1:2 = 0 rest 1 ||

```

8(in baza 10) = 1000(in baza 2)

5 in baza 10 = 101 in baza 2

14(in baza 10) = 1110 (in baza 2)

3 2 1 0
1 1 1 0

      0*2^0 + 1*2^1 + 1*2^2 + 1*2^3 = 0 + 2 + 4 + 8 = 14

    
1000 (in baza 2) = ? in baza 10

0*2^0 + 0*2^1 + 0*2^2 + 1*2^3 = 2^3 = 8

10101 in baza 2 = 21 in baza 10


Sa determinam forma de reprezentare a numarului intreg 5.

```
5 in baza 10 = 101 in baza 2

5(10) = 101(2)

Vor fi necesare 4 cifre de 0 nesemnificative , pentru completarea primilor 7 biti, iar pozitia 7 va fi 0 deoarece numarul este pozitiv.


_ _ _ _ _ _ _ _

0 0 0 0 0 1 0 1
_ _ _ _ _ _ _ _

7 6 5 4 3 2 1 0

pe 16 biti (2octeti sau 2 bytes):


                 _ _ _ _ _ _ _ _
     
  0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
                 _ _ _ _ _ _ _ _

 14              7 6 5 4 3 2 1 0 

  8(2) = 00001000

-8(2) = ?

```
Nu in acelasi mod se face reprezentarea numerelor intregi negative. Pentru aceasta este necesara efectuarea urmatorilor pasi:

1.determinarea reprezentarii interne a numarului ce reprezinta  valoarea absoluta a numarului initial. Aceasta are bitul de semn egal cu zero.

2. se calculeaza complementul fata de 1 a reprezentarii obtinute la pasul anterior. Cu alte cuvinte bitul 1 devine 0, iar bitul 0 devine 1.

3. se aduna 1 (adunarea in baza 2) la valoarea obtinuta.


1 + 1 = 0 transport 1

0 + 1 = 1

1 + 0 = 1

0 + 0 = 0


24+
47
=
71  (transport 1)


Exemplu: -8

- reprezentam valoarea absoluta a numarului 8. 

8 = 0000 1000 (pe 8 biti)

- complementul fata de 1 => 1111 0111

- reprezentarea obtinuta dupa adunarea cu 1 este: 

     111 
1111 0111 +
0000 0001 
---------        
1111 1000


1 in baza 2 = 0000 0001

 8 in baza 2 = 0000 1000
-8 in baza 2 = 1111 1000

Dupa cum observal bitul de semn este 1 ceea ce ne indica faptul ca avem de a face cu un numar negativ.

Putem trage concluzia ca numerele intregi care se pot reprezenta pe 8 biti sunt cuprinse intre:

1000 0000 si 0111 1111


Pe 16 biti:

1000 0000 0000 0000 = ? in baza 10

0111 1111 1111 1111 = ? in baza 10


Operatori la nivel de bit:

Operatorii pe biti se pot aplica datelor ce fac parte din tipurile intregi. Operatiile se efectueaza asupra bitilor din reprezentarea numerelor.

1. Operatorul de negatie

Acest operator una intoarce numarul intreg a carui reprezentare interna se obtine din reprezentarea interna a numarului initial prin complementarea fata de 1 a fiecarui bit.

1 devine 0
si 
0 devine 1

Exemplu:

~5 = -6

5 in baza 2 = 0000 0101

1111 1010 

6 in baza 2 = 0000 0110 

 1111 1001+
         1
-------------
 1111 1010

-6 in baza 2 = 1111 1010

~5  = 1111 1010 

~5 = -6

Operatorul de conjunctie &

Este un operator binar care returneaza numarul intreg a carui reprezentare interna

se obtine prin conjunctia bitilor care apar in reprezentarea interna a operanzilor.
Conjuctia se face cu toate perechile de biti situati pe aceeasi pozitie.

Exemplu:

5 & 3 = 

Reprezentarea interna a lui 5 = 0000 0101
Reprezentarea interna a lui 3 = 0000 0011


  0000 0101 &
  0000 0011
  ---------
  0000 0001

  5 & 3 = 1

true si true = true
true si false = false
false si true = false
false si false = false          


Operatorul de disjunctie |

Este un operator binar care returneaza numarul intreg a carui reprezentare interna
se obtine prin disjunctia bitilor care apar in reprezentarea interna a operanzilor.
Disjunctia se face intre bitii situati pe aceeasi pozitie.

a = 8
b = 12
a | b

din logica matematica am aflat urmatorul lucru:

true SAU true = True

true SAU false = True

false SAU true = TRue

false SAU false = False 

true  = 1
false = 0

a = 15
b = 3 

15 = 0000 1111
3 =  0000 0011

0000 1111 |
0000 0011
---------
0000 1111

a | b = 15

4 + 8 + 16 + 32 = 12 + 16 + 32 = 28 + 32 = 60
Operatorul sau exclusiv

XOR sau ^

Este un operator binar care returneaza numarul intreg a carui reprezentare interna 
se obtine prin operatia Sau exclusiv asupra bitilor care apar in reprezentarea interna a operanzilor. Operatia se face intre bitii situati pe aceeasi pozitie.

Exemplu:
15 XOR 3

in python simbolul ^

15 = 0000 1111
3 =  0000 0011


0000 1111^
0000 0011
---------
0000 1100   

Aceasta reprezentare este data de numarul intreg: 12

0000 1100 = 0*2^0 + 0 * 2^1 + 1*2^2 + 1*2^3 + 0 + 0 + 0 + 0 = 4 + 8 = 12


Operatorul Shift Left <<


Este un operator binar care returneaza numarul intreg a carui reprezentare este obtinuta  din reprezentarea  interna a primului operand prin deplasare la stanga
cu un numar de biti egal cu al doilea operand.

4 << 2 == 16

0000 0100 => 0001 0000 -> 1*2^4 = 16


Operatorul Shift Right >>

Este un operator binar care returneaza numarul intreg a carui reprezentare este obtinuta din reprezentarea interna a primului operand prin deplasa la dreapta
cu un numar de biti egali cu al doilea operand.

Prin deplsare la dreapta toti bitii din reprezentarea interna a numarului
se pierd , iar ultimii se completeaza cu zero.

14 >> 2 == 3

14 = 0000 1110 >> 2 
0000 0011 =>3 in baza 10

Problema:


Realizati un program care determina numarul de cifre de 1 din reprezentarea binara
a unul numar natural nenul n mai mic decat 100000000


8 =  00001000 (2)

pe 8 biti: 00001000

pe 16 biti: 00000000 00001000

pe 32 de biti: 00000000 00000000 00000000 00001000

pe 64 de biti: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00001000

n = 8

counter = 0

for i de la 0 la 32 

    daca intalnim un bit de 1 din reprezentarea sa , atunci contorizam variabila counter
    counter = counter + 1


    


