def merge(left, m, right, vec):
 
    i = left
    j = m + 1
    aux = []
 
    while i <= m and j <= right:
 
          if vec[i] < vec[j]:
             aux.append(vec[i])
             i += 1
          else:
             aux.append(vec[j])
             j += 1
 
    while i <= m:
          aux.append(vec[i])
          i += 1
    while j <= right:
          aux.append(vec[j])
          j += 1
    k = 0
    for i in range(left, right+1):
        vec[i] = aux[k];
        k += 1
 
def divideEtImpera(left, right, vec):
 
    if left < right:
            m = (left + right) >> 1
            divideEtImpera(left, m, vec)
            divideEtImpera(m + 1, right, vec)
            merge(left, m, right, vec)
 
def mergesort(vec):
    divideEtImpera(0, len(vec) - 1, vec)
 
def main():
    vec = [9,8,7,6,5,4,3,2,1,0,-1]
 
    print(vec)
 
    mergesort(vec)
 
    print(vec)
 
main()
