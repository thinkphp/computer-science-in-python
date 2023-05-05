class Stack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.vec = [ 0 ] * (capacity + 2)

    def push(self, data):
        if not self.isFull():
            self.top += 1
            self.vec[self.top] = data
        else:
            print("Stack overflow")
            return

    def pop(self):
        if not self.isEmpty():
            data = self.vec[self.top]
            self.top-=1
            return data
        else:
            print("Stack Empty!")
            return

    def getTop(self):
        return self.vec[self.top]

    def TopIncrement(self):
        self.vec[self.top]+=1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.capacity == self.top - 1

    def __repr__(self):
        out = ""
        for i in range(0, self.top+1):
            if self.vec[i] != 0:
               out += str(self.vec[i]) + " "
        return out

def fn():
    n = 5
    st = Stack(5)
    st.push(1)
    print(st, end ="\n")
    while not st.isEmpty():
        if st.getTop() < n:
            st.push(st.getTop()+1)
        else:
            st.pop()
            st.TopIncrement()
        print(st,end="\n")
fn()
