# Machine Learning, Deep Learning
#
# - disciplina, o ramura AI (Artificial Intelligence)
# - subdisciplina, subramura a ML - simulare a retelei neuronale
#
# Mean - the average value - valoarea medie dintr-un sir de numere - un concept statistic
# Median - the mid point value
# Mode - the most common value
#
#

from scipy import stats
import numpy
import statistics

def mean(speed):

    #sa calculam mean

    # a,b,c => mean = (a + b + c) / 3

    #calculam size-ul vectorului speed
    n = len( speed )

    # calculam suma celor n element din vector
    get_sum = sum( speed )

    #calculam mean-ul
    mean = get_sum / n

    #returnam mean-ul
    return mean

def main():

    #un vector care retine vitezele unor masini
    speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    answer = mean( speed )

    print("Mean / Average is: ", str( answer ))

    x = numpy.mean( speed )

    x2 = statistics.mean(speed)

    print("Mean calculat cu numpy is: ", x)

    print("Mean calculat cu modulul statistics is: ", x2)

    answer = numpy.median(speed)

    answer2 = statistics.median(speed)

    print("Meadian cu modulul numpy = ", answer)

    print("Meadian cu modulul statistics = ", answer2)

    speed.sort()

    print(speed)

    n = len(speed)
    # 1 2 3 4 5 6 7 8
    # 0 1 2 3
    # n = 7
    #



    if n % 2 == 0:
        median1 = speed(n//2)
        median2 = speed(n//2-1)
        median = (median1 + median2) / 2
    else:
        median = speed[n//2]
    print("Median is: ", median)

    print(statistics.median([1,2,3,4,5,6,7,8]))
    print(numpy.median([1,2,3,4,5,6,7,8]))

    #Mode
    speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 99, 99]
    # vector = [3,4,5,6,7,8,7,3,3,4,4]
    # mode = {3,4}
    x = statistics.mode(speed)
    y = stats.mode(speed)
    print("Mode cu modulul statistics is: ", x)
    print("Mode cu scipy is: ", y)

    speed.sort()

    counting = []

    print(speed)

    i = 0

    while i < len(speed):

        counting.append(speed.count(speed[i]))

        i+=1

    print("Counting = ", counting)

    dictinary = dict(zip(speed, counting))

    print(dictinary.items())

    ans = { k for (k,v) in dictinary.items() if v == max(counting) }

    print(ans)

    #dict = o structura de date prin care adaugam elemente perechi, despartite cu :
    #dictinar = {"egg":"ou", "car":"masina"}

    #lista = [1,2,3,4,5]

    #print(type(dictinar))

    #dictinar2 = {"table":"masa",
    #             "house": "casa",
    #             "vacantion":
    #             "vacanta"}

    #in python
    # Data Structures
    # list, tuple,dict
    # list = [1,2,3,4]
    # tuplu = (1,2,3,4,5,6)
    # dict = {"a":"b", "c":"d"}
    # set = {1,2,3,4,5}
    #

    #lista1 = [1,2,3]
    #lista2 = [5,7,8]
    #res = dict(zip(lista1, lista2))
    #print(res)

    #lista_noastra = []
    #lista_noastra.append(1)
    #lista_noastra.append(2)
    #lista_noastra.append(3)
    #print(lista_noastra)

    a = [1,2,3,4,9,-1]#keys
    b = [7,6,7,8,7,7]#values
    c = dict(zip(a,b))
    d = []#empty
    # c.items() = {(1,7), (2,6), (3,7), (4,8), (9,7)}
    print(c.items())
    for (key,value) in c.items():
        if value == 7:
            #adauga in vectorul d  key
            d.append( key )
    print(d)
    w = [k for (k,v) in c.items() if v == 7]
    # este echivalenta cu liniile 153 - 154
    print(w)

main()
