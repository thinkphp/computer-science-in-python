def combo( arr ):

    shrinkFactor = 1.3

    swapped = True

    n = len(arr)

    gap = n

    while gap > 1 or swapped is True:

          if gap > 1:

             gap = int (gap / shrinkFactor )

          i = 0

          swapped = False

          while i + gap < n:

                if arr[ i ] > arr[ i + gap ]:

                   arr[i], arr[i + gap] = arr[i + gap], arr[i]

                   swapped = True

                i += 1
    return arr

def main():
    fin = open('algsort.in','r')
    fout = open('algsort.out','w')
    N = int(fin.readline().strip())
    arr = fin.readline().strip().split(" ")
    arr = [int(i) for i in arr]
    arr = combo(arr)
    print(arr)
    fout.write(' '.join(map(str, arr)))
main()
