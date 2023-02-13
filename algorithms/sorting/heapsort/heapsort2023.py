def up(child):

    parent = child//2

    while parent != 0:
        if Heap[parent] >= Heap[child]:
            Heap[parent], Heap[child] = Heap[child], Heap[parent]
            child = parent
            parent = child // 2
        else:
            break

def down(parent):

    while 2 * parent <= size:

        child = 2 * parent

        if 2 * parent + 1 <= size and Heap[2 * parent + 1] < Heap[2 * parent]:
            child+= 1

        if Heap[parent] <= Heap[child]:
            break

        Heap[parent], Heap[child] = Heap[child], Heap[parent]

        parent = child

def remove():
    global size
    min = Heap[1]
    Heap[1] = Heap[size]
    size-=1
    down(1)
    return min

def insert(value):
    global size
    size +=1
    Heap[size] = value
    up(size)

def func():

    global Heap, size

    arr = [8,7,6,-2,3,4,0,19]
    Heap = [0] * 20
    size = 0
    for i in arr:
        insert(i)
    print("size=%d"%size)
    for i in range(len(arr)):
        print(remove(), end = " ")

func()
