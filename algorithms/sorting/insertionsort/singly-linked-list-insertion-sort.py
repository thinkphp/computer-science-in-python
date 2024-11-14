class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_sorted(head, data):
    # Create new node
    new_node = Node(data)

    # Special case for the head node or new node data is smaller than head
    if head is None or new_node.data <= head.data:
        new_node.next = head
        head = new_node
        return head

    # Locate the node before the point of insertion
    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

def print_list(head, sentinel_value=None):
    current = head
    while current is not None and current.data != sentinel_value:
        print(current.data, end=" ")
        current = current.next
    print()

if __name__ == "__main__":
    n = int(input("Numarul de elemente n = "))

    # Create the head of the list with a sentinel node
    BigNumber = float('inf')
    head = Node(BigNumber)

    # Insert nodes into the sorted list
    for i in range(n):
        num = int(input("Num = "))
        head = insert_sorted(head, num)

    print("Lista sortată:")
    print_list(head, sentinel_value=BigNumber)

