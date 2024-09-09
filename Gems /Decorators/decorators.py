"""
Decoratoarele sunt functiile care modifica alte functii sau metode, fara a schimba
efectiv codul original. Ele sunt utile pentru a adauga functionalitati comune in mai multe functii sau metode
,cum ar fi logarea, masurarea timpului de executie, memorarea rezultatelor, validarea datelor, autentificare

Decoratori: exemple practice:

Decorator de logare:

Output:
Apelare functie: Hello
Hello, Python!
Functia hello s-a terminat

"""
def log_function(func):

    def wrapper():
        print(f"Apelare functie: {func.__name__}")
        func()
        print(f"Functia {func.__name__} s-a terminat")

    return wrapper

@log_function
def hello():
    print("Hello, Python")

#hello()

"""
Decorator care masoara timpul de executie al unui program
"""

import time

def time_execution(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Timpul de executie: {end_time - start_time} seconds")

    return wrapper

@time_execution
def my_function():
    time.sleep(3)
    print("functia s-a terminat")
#my_function()


"""
Decorator pentru validare date
verifica daca argumentele date functiei sunt numere intregi, si doar atunci permite executie functiei
"""

print("_"*70)
print("Decorator pentru validare date:")

def validate_integers(func):

    def wrapper(a, b):

        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            print("Toti parametrii trebuie sa fie numere intregi!")

    return wrapper


@validate_integers
def add(a, b):
    return a + b

print(add(1,1))
print(add(1,'1'))
print(add('33','1'))


"""
Decorator pentru cache(memorarea rezultatelor)

Acest decorator salveaza rezultatele functiei pentru a evita calcule repetate inutile(costisitioare din punct de vedere al spatiului-timp)
"""

def cache_results(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper

@cache_results
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#print( factorial(5) ) # prima data calculeaza factorial(5)

#print( factorial( 5 ) ) # a doua oara foloseste cache-ul

#print( factorial(5) ) # a treia oara foloseste cache-ul

"""
Decorator pentru autentificare
"""

def check_authentification(func):

    def wrapper(user):
        if user.get("authenticated", False):
            return func(user)
        else:
            print("Utilizator neautentificat! Acces refuzat.")
    return wrapper

@check_authentification
def show_dashboard( user ):
    print(f"Salut, {user['name']} Bine ai venit la dashboard!")

user1 = {"name": "Alice", "authenticated": True}
user2 = {"name": "David", "authenticated": False}

show_dashboard( user1 ) #utilizator autentificat
show_dashboard( user2 ) #utilizator neautentificat
