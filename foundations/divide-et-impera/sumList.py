# divide et impera
def __summa(lo, hi, arr):
 
    if lo == hi:
        return arr[lo]
    else:
        m = (lo + hi) >> 1
        a = __summa(lo, m, arr)
        b = __summa(m + 1, hi, arr)
        s = a + b
        return s
 
# loop standard
def _summa(arr):
    s = 0
    for i in range(0, len(arr)):
        s = s + arr[i]
    return s
 
# head and tail list
def summa(arr):
    if arr == []:
       return 0
    else:
       return arr[0] + summa(arr[1:])
def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    n = len(arr)
    s = __summa(0, len(arr) - 1, arr)
    print(s)
    print(s == summa(arr) == _summa(arr) == n * (n  + 1 )//2)
main()
