class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

def CreateList():
    front = None
    back = None
    arr = [1,2,3,4,5,6,7]
    for num in arr:
        if front is None:
            c = Node()
            c.data = num
            c.next = None
            c.prev = None
            front = back = c
        else:
            c = Node()
            c.data = num
            c.next = None
            c.prev = back
            back.next = c
            back = c

    return [front, back]

def display_left(front):
    c = front
    while c:
        print(c.data, end =" ")
        c = c.next
    print()

def display_right(back):
    c = back
    while c:
        print(c.data, end =" ")
        c = c.prev
    print()

def remove(front, back, remove_node):

    if front.data == remove_node:
        tmp = front
        front = front.next
        if front:
            front.prev = None
        del tmp

    elif back.data == remove_node:
        tmp = back
        back = back.prev
        if back:
            back.next = None
        del tmp
    else:
        c = front
        while c.data != remove_node:
            c = c.next
        c.prev.next = c.next
        c.next.prev = c.prev
        del c
    return front, back

def main():
    list = CreateList()
    front = list[0]
    back = list[1]
    display_left(front)
    display_right(back)
    remove_node = 1
    front, back = remove(front, back, remove_node)
    print("remove:%d\n"%remove_node)
    display_left(front)
    display_right(back)
    remove_node = 7
    front, back = remove(front, back, remove_node)
    print("remove:%d\n"%remove_node)
    display_left(front)
    display_right(back)
    remove_node = 4
    front, back = remove(front, back, remove_node)
    print("remove:%d\n"%remove_node)
    display_left(front)
    display_right(back)

if __name__ == "__main__":
    main()
