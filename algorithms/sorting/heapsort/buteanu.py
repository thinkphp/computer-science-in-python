ef down(parent):

    while 2 * parent <= size:

          child = 2 * parent

          if 2 * parent + 1 <= size and Heap[2 * parent + 1] <  Heap[2 * parent]:
                child += 1

          if Heap[ parent ] <= Heap[ child ]:
              break

          Heap[child], Heap[parent] = Heap[parent], Heap[child]

          parent = child


def remove():

    global size

    min = Heap[1]
    Heap[1] = Heap[size]
    size -= 1
    down(1)

    return min

def insertHeap( elem ):

    global size

    size += 1

    Heap[ size ] = elem

    up( size )


def heapsort(vec):

    global Heap, size

    size = 0

    Heap = [0] * 100

    for item in vec:
        insertHeap( item )

    print("Heap sort using min-heap")
    for i in vec:
        min = remove()
        print(min, end = ", ")

heapsort([-26,-14,3,0,-6,-7,1,23])
