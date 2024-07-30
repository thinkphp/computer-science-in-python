from abc import ABC, abstractmethod
import random

class Jucator(ABC):
    @abstractmethod
    def alege_film(self):
        pass

    @abstractmethod
    def nivel_satisfactie(self, film_ales):
        pass

class JucatorPreferinte(Jucator):
    def __init__(self, preferinte_filme):
        self.preferinte_filme = preferinte_filme

    def alege_film(self):
        # Alege filmul cu cel mai mare nivel de satisfactie
        return max(self.preferinte_filme, key=self.preferinte_filme.get)

    def nivel_satisfactie(self, film_ales):
        return self.preferinte_filme.get(film_ales, 0)

class JucatorAleator(Jucator):
    def __init__(self, preferinte_filme):
        self.preferinte_filme = preferinte_filme

    def alege_film(self):
        # Alege aleator un film din lista de preferinte
        return random.choice(list(self.preferinte_filme.keys()))

    def nivel_satisfactie(self, film_ales):
        return self.preferinte_filme.get(film_ales, 0)

class JocFilmeSumaZero:
    def __init__(self, jucator1, jucator2):
        self.jucator1 = jucator1
        self.jucator2 = jucator2

    def joaca(self):
        film1 = self.jucator1.alege_film()
        film2 = self.jucator2.alege_film()

        print(f"Jucătorul 1 a ales: {film1}")
        print(f"Jucătorul 2 a ales: {film2}")

        satisfactie1 = self.jucator1.nivel_satisfactie(film2)
        satisfactie2 = self.jucator2.nivel_satisfactie(film1)

        print(f"Nivel de satisfacție pentru Jucătorul 1: {satisfactie1}")
        print(f"Nivel de satisfacție pentru Jucătorul 2: {satisfactie2}")

        if satisfactie1 > satisfactie2:
            print("Jucătorul 1 câștigă runda!")
        elif satisfactie2 > satisfactie1:
            print("Jucătorul 2 câștigă runda!")
        else:
            print("Este remiză!")

# Exemplu de utilizare a claselor
preferinte_jucator1 = {
    "Film A": 8,
    "Film B": 3,
    "Film C": 5
}

preferinte_jucator2 = {
    "Film A": 2,
    "Film B": 9,
    "Film C": 4
}

jucator_preferinte = JucatorPreferinte(preferinte_jucator1)
jucator_aleator = JucatorAleator(preferinte_jucator2)
joc = JocFilmeSumaZero(jucator_preferinte, jucator_aleator)

# Jucăm mai multe runde pentru a vedea rezultatele
for _ in range(5):
    joc.joaca()
    print("---")
