class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort(head):
    if not head:
        return

    swapped = True
    lptr = None  # Last sorted position

    while swapped:
        swapped = False
        current = head

        # Traverse the list up to the last sorted position
        while current.next != lptr:
            if current.data > current.next.data:
                # Swap the data of the two nodes
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next

        # Update the last sorted position
        lptr = current

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

