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
    while i * i <= n and prime is True:
        prime =  (n % i) != 0
        i += 1
    return prime

def create_list(arr):

  head = None
  for elem in arr:
      if head is None:
        head = Node()
        head.data = elem
        head.next = None
      else:
        c = Node()
        c.data = elem
        c.next = head
        head = c
  return head

def display( head ):
    while head:
        print(head.data, end = " ")
        head = head.next
    print()

def remove_primes( head ):
    q = Node()
    q.next = head
    last = q
    while head:
        if isPrime(head.data) is False:
            tmp = head
            last.next = head.next
            head = head.next
            del tmp
        else:
            head = head.next
            last = last.next
    return q.next

def reverse(list):
    curr = list
    next = None
    prev = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev

def main():
    arr = [1,2,3,4,5,6,7,8,9,7919]
    list = create_list(arr)
    list = reverse(list)
    display(list)
    new_list = remove_primes(list)
    display(new_list)

if __name__ == "__main__":
    main()
