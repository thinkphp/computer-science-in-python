def quicksort(lo, hi, vec):

    i = lo
    j = hi
    pivot = vec[ (lo + hi) >> 1]

    while i <= j:
        while vec[i] < pivot:
              i += 1
        while vec[j] > pivot:
              j -= 1
        if i <= j:
            vec[i], vec[j] = vec[j], vec[i]
            i += 1
            j -= 1
    if lo < j:
        quicksort(lo, j, vec)
    if i < hi:
        quicksort(i, hi, vec)

def main():

    fin = open("algsort.in", "r")
    fout = open("algsort.out", "w")

    N = int(fin.readline().strip())
    vec = fin.readline().strip().split(" ")
    vec = list(map(int, vec))

    for i in range(0, N):
        print(vec[i], end = ' ')

    quicksort(0, N - 1, vec)

    print()

    for i in range(0, N):
        fout.write(str(vec[i]) + " ")
        #print(vec[i], end = " ")

    print()
main()
