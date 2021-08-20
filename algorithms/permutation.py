def perm( level ):
    if level == n + 1:
       for i in range(1, level):
           fout.write(str(sol[i]) + " ")

       fout.write("\n")
    else:
        for i in range(1, n + 1):
            if visited[ i ] is False:
               sol[ level ] = i
               visited[ i ] = True
               perm(level + 1)
               visited[ i ] = False
def main():
    global n, sol, visited, fout
    fin = open("permutari.in", "r")
    fout = open("permutari.out", "w")
    n = int(fin.readline().strip())
    sol = [ -1 ] * (n + 1)
    visited = [ False ] * (n + 1)
    perm(1)
main()
