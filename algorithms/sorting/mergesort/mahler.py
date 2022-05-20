def merge(lo, m, hi, arr):

    i = lo
    j = m + 1
    aux = []

    while i <= m and j <= hi:
        if arr[i] < arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    while i <= m:
        aux.append(arr[i])
        i+=1
    while j <= hi:
        aux.append(arr[j])
        j+=1

    ind = 0
    for k in range(lo, hi + 1):
        arr[k] = aux[ind]
        ind += 1


def divide_et_impera( lo, hi, arr):

        if lo == hi:
           return

        m = ( lo + hi ) >> 1

        divide_et_impera(lo, m, arr)
        divide_et_impera(m + 1, hi, arr)
        merge(lo, m, hi, arr)

def mergesort( arr ):

    divide_et_impera(0, len( arr ) - 1, arr)

def main():

    arr = [9,8,7,6,-5,4,3,2,1]

    mergesort( arr );

    print( arr )

main()
