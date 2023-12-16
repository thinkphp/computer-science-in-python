# https://codeforces.com/problemset/problem/106/B
##
##
##   5 (numarul de laptop-uri)
##
#laptop 1: 2100 512 150 200
#       2: 2000 2048 240 350
#       3: 2300 1024 200 320
#       4: 2500 2048 80 300
#       5: 2000 512 180 150
##
class laptop:
    def __init__(self,speed, ram, hdd, cost):
        self.speed = speed
        self.ram = ram
        self.hdd = hdd
        self.cost = cost

def solve_problem_laptop():
    #citim numarul N de laptopuri din Input Standard
    n = int(input())
    #declaram un vector sau un array de laptop-uri, unde laptop este o clasa
    vec = [ laptop ] * n
    #print( vec )
    for i in range( n ):
        #read speed, ram, hardisk, cost
        s, r, h, c = map(int, input().split())

        #adaugam un vector fiecare instanta a clasei laptop
        vec[ i ] = laptop( s, r, h, c )

    #print(vec)
    com = [ 0 ] * n

    #n = numarul de laptopuri
    for i in range( n ):
        for j in range( n ):
            if i != j:
                if vec[i].speed < vec[j].speed and vec[i].ram < vec[j].ram and vec[i].hdd < vec[j].hdd:
                      com[ i ] = 1
                      break
    #print(com)
    maximum = int(1e12)
    idx = -1
    for i in range(n):
        if com[i] == 0:
            if maximum > vec[i].cost:
                idx = i + 1
                maximum = vec[i].cost
    print(idx)
solve_problem_laptop()
