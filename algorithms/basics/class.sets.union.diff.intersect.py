class Set:

    set = []

    def __init__(self,Thelist):
        self.set = Thelist

    def __sub__(self,other):
        out = []
        for el in self.set:
            found = False
            for el2 in other.set:
                if el == el2:
                   found = True
                   break
            if found is False:
               out.append(el)
        return out

    def __add__(self,other):
        out = []
        for i in other.set:
            out.append(i)
        for el in self.set:
            found = False
            for el2 in other.set:
                if el == el2:
                   found = True
                   break
            if found is False:
               out.append(el)
        out.sort()
        return out



    def __and__(self,other):
        out = []
        for el in self.set:
            found = False
            for el2 in other.set:
                if el == el2:
                    found = True
                    break
            if found is True:
                out.append(el)
        return out

def fn():
    list1 = [1,2,3,4,5,6,7,102]
    print(list1)
    list2 = [10,101,2,3,102,202]
    list2.sort()
    print(list2)
    set1 = Set(list1)
    set2 = Set(list2)
    print("Intersect: ",set1&set2)
    print("Union",set1+set2)
    print("Diff",set1-set2)
fn()
