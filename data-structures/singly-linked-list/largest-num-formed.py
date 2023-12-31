'''
/*
                _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . ___
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
def display(head):
    while head:
        print(head.data, end = " ")
        head = head.next
def CreateList(nr):
    head = None
    while nr:
        if head is None:
            head = Node()
            head.data = nr % 10
            head.next = None
        else:
            c = Node()
            c.data = nr % 10
            c.next = head
            head = c
        nr //= 10
    return head

def findLargestNum( list ):
    s = 0
    c = list
    arr = [0] * 10
    while c:
        arr[c.data] = 1
        c = c.next
    for i in range(9, -1, -1):
        if arr[i] == 1:
            s = s * 10 + i
    return s
def main():
    nr = 1578
    list = CreateList( nr )
    largest = findLargestNum( list )
    print(largest)

if __name__ == "__main__":
    main()
