import stdio
import algorithms as algo
import mathematics as math

def main():
    stdio.writeln("Hello, Universe! stdio")
    print("Hello, Universe! (print - built-in)")
    a = 1111
    b = 2222
    print("Euclid(a,b)=>")
    stdio.writeln("Euclid(a,b)=")
    stdio.writeln(algo.euclid_it(a,b))
    stdio.writeln(algo.euclid_rec(a,b))
    print("Cifra de Control = ")
    stdio.writeln(algo.ControlDigit1(a))
    stdio.writeln(algo.ControlDigit2(b))
    stdio.writeln(math.sqrt(2))
    a = 4
    b = 1
    math.FirstDegreeEquation(a, b)
    vec = [9,8,7,6,5,4,3,2,1,0]
    algo.sorting(vec)
    for i in vec:
        stdio.writeln( i )
    A, B, C = [int(i) for i in input().split()]
    print(*math.QuadraticEquation(A, B, C), sep="\n")
main()
