class Node:
    def __init__(self):
        self.data = None
        self.next = None

def create_list(arr):
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

def merge_lists(list1, list2)-> Node:

    if list1.data < list2.data:
        list = list1
        last = list1
        list1 = list1.next
    else:
        list = list2
        last = list2
        list2 = list2.next

    while list1 and list2:
        if list1.data < list2.data:
            last.next = list1
            last = list1
            list1 = list1.next
        else:
            last.next = list2;
            last = list2
            list2 = list2.next
    if list1:
        last.next = list1
    else:
        last.next = list2
    return list

def display(h):
    while h:
        print(h.data, end = " ")
        h = h.next
    print()
def main():
    arr1 = [10,4,2,1]
    arr2 = [11,9,7,5,3,-1,0]
    list1 = create_list(arr1)
    list2 = create_list(arr2)
    print("List1: ")
    display(list1)
    print("List2: ")
    display(list2)
    print("Merged: ")
    merged = merge_lists(list1, list2)
    display(merged)

if __name__ == "__main__":
    main()
