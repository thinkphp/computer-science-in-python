"""
Generators (concept fundamental in Python)
Generatoarele sunt functii care returneaza un iterator, folosind cuvantul cheie yield
"""

# un generator care returneaza numere consecutive de la 0 pana la un numar dat

def count_up_to(max_value):
    count = 0
    while count <= max_value:
        yield count
        count += 1

# folosirea generatorului
for num in count_up_to(10):
    print(num)
"""
Output:
0
1
2
3
4
5
6
7
8
9
10
"""

"""
Generator de numere pare
"""

print("Generator de numere pare:")
print("_"* 20)
def even_numbers(max_value):
    for num in range(max_value+1):
        if num % 2 == 0:
            yield num

for even in even_numbers(10):
    print(even)


print("Generator de numere impare:")
print("_"* 20)
def odd_numbers(max_value):
    for num in range(max_value+1):
        if num % 2 != 0:
            yield num

for odd in odd_numbers(10):
    print(odd)

"""
Generator pentru sirul lui Fibonacci

Acest generator produce elementele din sirul lui Fibonacci, in care fiecare numar este suma celor doua
numere precedente
"""

print("Generator pentru sirul lui Fibonacci:")
print("_"* 20)


def Fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

for fib in Fibonacci(100):
    print(fib, end = " ")
