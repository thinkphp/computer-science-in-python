def query(string):

    i = 0
    icurr = 0
    imax = 0
    lmax = 1

    n = len(string)

    while i <= n:
      if i - icurr > lmax:
          lmax = i - icurr
          imax = icurr
      icurr = i
      while i < n-1 and int(string[i])+1 == int(string[i+1]):
        i += 1
      i += 1
    subseq=[]
    for i in range(imax, imax + lmax):
        subseq.append(string[i])
    return [imax, lmax, subseq]

def func():
    string = "777712345677771234522222345678999888"
    search = query(string)
    print(search)
func()
