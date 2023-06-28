class Set:

    arr = []

    def __init__(self,arr):

        self.arr = arr;

    def __add__(self,other):

        n = len(self.arr)
        m = len(other.arr)
        i = 0
        j = 0
        union = []

        while i < n and j < m:
            if self.arr[i] < other.arr[j]:
                union.append(self.arr[i])
                i += 1
            elif self.arr[i] > other.arr[j]:
                union.append(other.arr[j])
                j +=1
            else:
                i += 1

        while i < n:
            union.append(self.arr[i])
            i+=1
        while j < m:
            union.append(other.arr[j])
            j+=1
        return union

    def __and__(self,other):

        n = len(self.arr)
        m = len(other.arr)
        i = 0
        j = 0
        union = []
        intersect = []
        while i < n and j < m:
            if self.arr[i] < other.arr[j]:
                union.append(self.arr[i])
                i += 1
            elif self.arr[i] > other.arr[j]:
                union.append(other.arr[j])
                j +=1
            else:
                intersect.append(self.arr[i])
                i += 1
        while i < n:
            union.append(self.arr[i])
            i+=1
        while j < m:
            union.append(other.arr[j])
            j+=1
        return intersect

    def __str__(self):

        return str(self.arr)
def fn():
    set1 = Set([1,3,5,7,19,11])
    print("set1 = ",set1)
    set2 = Set([2,4,6,8,10,19])
    print("set2 = ",set2)
    union = set1 + set2
    intersect = set1 & set2
    print("Union = ",union)
    print("Intersection =",intersect)
fn()
