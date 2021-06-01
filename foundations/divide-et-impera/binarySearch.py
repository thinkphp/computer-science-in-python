# recursion 1
def binsearch(lo, hi, list, key):
    if lo > hi:
       return False
    p = ( lo + hi ) >> 1
    if key == list[p]:
       return True
    if key > list[p]:
       return binsearch(p+1, hi, list, key)
    else:
       return binsearch(lo, p - 1, list, key)

# recursion 2
def _binsearch(lo, hi, list, key):
    if lo <= hi:
      p = ( lo + hi ) >> 1
      if key == list[p]:
          return True
      if key > list[p]:
          return binsearch(p+1, hi, list, key)
      else:
          return binsearch(lo, p - 1, list, key)
    return False

#iteration 1
def _binsearch_(lo, hi, list, key):
    pos = False
    while lo <= hi:
        p = (lo + hi ) >> 1
        if list[p] == key:
            pos = True
            break
        elif key > list[p]:
            lo = p + 1
        else:
            hi = p - 1
    return pos

#iteration 2
def _binsearch_2(lo, hi, list, key):

    pos = False
    while not lo > hi and pos is False:
        p = (lo + hi ) >> 1
        if list[p] == key:
            pos = True
        elif key > list[p]:
            lo = p + 1
        else:
            hi = p - 1
    return pos


def searchBin(list, key):
    return _binsearch_2(0, len(list)-1, list, key)

# non recursion => iteration
def main():
    list = [-3,-1,11,22,44,55,77,88,101]
    print(list)
    key = -3
    if searchBin(list,key) is True:
       print(f'{key} exists in List')
    else:
       print(f'{key} not exist in List')
main()
