'''
Mostenire OOP

Extinderea unei clasei in programarea orientata pe obiecte se refera la crearea unei noi clase
bazate pe o clasa existenta. Aceata practica este cunoscuta sub numele de MOSTENIRE (Inheritance)
In Python mostenirea permite unei clase sa prea comportamentele si caracteristicile (atributele si metodele)
unei alte clase, oferindu-i posibilitatea de a adauga si modifica functionalitati.

1. Clasa de baza  - este clasa pe care o extindem
2. Clasa derivata - este clasa care extinde clasa de baza , adaugand functionalitati suplimentare


'''
# clasa de baza
class Animal:
    def __init__(self, name):
        self.name = name
    def vorbeste(self):
        return "Acesta animal vorbeste"

#clasa derivata
class Caine( Animal ):

    def vorbeste(self):
        return f"{self.name} Hau! Hau!"

#alta clasa derivata
class Pisica( Animal ):
    def vorbeste(self):
        return f"{self.name} Miau! Miau!"

cainele_meu = Caine("Tom")
pisica_mea = Pisica("Cat")

print(cainele_meu.vorbeste())
print(pisica_mea.vorbeste())

#clasa de baza
class Vehicul:

    def __init__(self, marca, year):
        self.marca = marca
        self.year = year

#clasa derivata
class Masina( Vehicul ):
    def __init__(self, marca, year, model,culoare):
        super().__init__(marca, year)
        self.model = model
        self.culoare = culoare

    def description(self):
        return f"Masina are marca '{self.marca}' modelul '{self.model}' fabricata in anul '{self.year}' si culoarea '{self.culoare}'"

masina = Masina("BMW",2001,"Z3","red")
print(masina.description())
