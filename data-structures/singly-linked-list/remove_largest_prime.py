class Node:
    def __init__(self):
        self.data = None
        self.next = None

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    prime = True
    i = 2
    while i * i <= n and prime:
        prime = (n % i) != 0
        i+=1
    return prime

def CreateList( arr ):
        head = None
        for i in arr:
            if head is None:
                head = Node()
                head.data = i
                head.next = None
            else:
                c = Node()
                c.data = i
                c.next = head
                head = c
        return head

def remove_largest_prime(head):

    q = head
    temp = None
    max = 0

    if isPrime( head.data ):
        max = head.data
    else:
        max = 0

    while q.next is not None:
      if isPrime(q.next.data) and q.next.data > max:
         max = q.next.data
         temp = q
      q = q.next

    if max != 0:
        if temp is None:
            aux = head
            head = head.next
            del aux
        else:
            aux = temp.next
            temp.next = temp.next.next
            del aux
    return head

def display(head):
    while head:
        print(head.data , end = " ")
        head = head.next
    print()
def main():
    arr = [1,2,3,4,7919,5,6,7,8,9,10]
    list = CreateList(arr)
    display( list )
    head = remove_largest_prime( list )
    display(head)


if __name__ == "__main__":
    main()
