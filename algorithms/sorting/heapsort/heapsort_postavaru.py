def up( child ):

    parent = child // 2

    while parent != 0:

          if Heap[parent] >= Heap[ child ]:

              aux = Heap[parent]

              Heap[parent] = Heap[child]

              Heap[child] = aux

              child = parent

              parent = child // 2
          else:
              break

def down( parent ):

    while 2 * parent <= sizeH:

          child = 2 * parent

          if 2 * parent + 1 <= sizeH and Heap[ 2 * parent + 1 ] < Heap[ 2 * parent ]:

              child += 1

          if Heap[parent] <= Heap[child]:

              break

          aux = Heap[ parent ]

          Heap[ parent ] = Heap[ child ]

          Heap[ child ] = aux

          parent = child          

def insertHeap( value ):

    global sizeH, Heap

    sizeH += 1

    Heap[ sizeH ] = value

    up( sizeH )



def removeHeap():

    global Heap, sizeH

    ret = Heap[1]
    Heap[1] = Heap[sizeH]
    sizeH -= 1
    down(1)
    return ret

def main():

    global Heap, sizeH

    f = open("algsort.in","r")

    fout = open("algsort.out","w")

    n = int( f.readline().strip())

    data = f.readline().strip().split(" ")

    arr = [int(value) for value in data]

    Heap = [ 0 ] * 500500

    sizeH = 0

    for i in range(0, n):

        insertHeap( arr[ i ] )

    for i in range(0, n):
    
        print(removeHeap(), end = " ")
        fout.write(str(removeHeap()) + " ")
main()
