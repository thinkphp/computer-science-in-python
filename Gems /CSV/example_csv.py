'''
CSV = Comma-separeted Values => este un format simplu de fisier text
utilizat pentru a stoca date tabulare cum ar fi datele din foi de calcul sau baze de date.

Datele sunt separate prin virgule (sau alte delimitatoare - tab-uri, punct si virgula), delimitatoare,
iar fiecare linie reprezinta un rand de date.
'''

import csv

#datele de scris intr-un fisier csv
header = ["Name","Age","Town"]
rows = [
       ["David","20","Brasov"],
       ["Ann","22","Sibiu"],
       ["Dacia","21","Cluj"]
]

#cum scriem intr-un fisier CSV
with open("fisier.csv","w",newline='') as file:
    ob_writer = csv.writer(file) #creeaza un obiect writer care poate scrie randurile in fisierul CSV
    ob_writer.writerow(header) #scrie in fisier antetul , un singur rand
    ob_writer.writerows(rows)  #scrie randuri multiple
with open("fisier.csv","r",newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

'''
Recapitulare:
Citirea CSV:
= csv.reader() pentru a itera prin randuri si coloane dintr-un fisier CSV
Scrierea csv:
csv.writer() pentru a adauga anteturi si randuri intr-un fisier
Delimitatori personalizati:
foloseste parametru delimiter pentru a gestiona delimitatori non-standard.

import csv
Modulul este utilizat pentru manipularea fisierelor csv, fiecare ca vrei
sa citeste date , sa le scrii sau sa le manipulezi in formate diferite.
'''
