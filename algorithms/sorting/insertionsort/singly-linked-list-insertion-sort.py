class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def selection_sort(head):
    if not head:
        return

    current = head
    
    while current:
        # Assume the minimum node is the current node
        min_node = current
        next_node = current.next

        # Find the minimum element in the remaining unsorted list
        while next_node:
            if next_node.data < min_node.data:
                min_node = next_node
            next_node = next_node.next

        # Swap values between the current node and the found minimum node
        if min_node != current:
            current.data, min_node.data = min_node.data, current.data

        # Move to the next node to continue sorting
        current = current.next

if __name__ == "__main__":
    head = None

    # Adding elements to the list
    head = push(head, 5)
    head = push(head, 3)
    head = push(head, 8)
    head = push(head, 2)
    head = push(head, 10)
    head = push(head, 1)

    print("Unsorted List:")
    print_list(head)

    # Call Selection Sort
    selection_sort(head)

    print("Sorted List:")
    print_list(head)
