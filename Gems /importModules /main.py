import stdio
import algorithm

def main():
    a = int(input("a="))
    b = int(input("b="))
    answer = algorithm.euclid_rec(a,b)
    stdio.writeln("Euclid(a,b) = " + str( answer ))
    algorithm.FirstDegreeEquation(a,b)
    n = input("Dati un N = ")
    stdio.writeln(algorithm.controlDigit(N))
main()
