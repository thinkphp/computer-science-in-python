import stdio
import algorithms as algo

def main():
    a = int(input("a="))
    b = int(input("b="))
    answer = algo.euclid_rec(a,b)
    stdio.writeln("Euclid(a,b) = " + str( answer ))
    algo.FirstDegreeEquation(a,b)
    n = int(input("Dati un N = "))
    stdio.writeln(algo.controlDigit(n) )
main()
