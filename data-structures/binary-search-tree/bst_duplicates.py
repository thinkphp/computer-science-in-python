class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        self.count = 1

def insert(root, value):
    if root is None:
        return Node(value)
    elif value > root.data:
        root.right = insert(root.right, value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.count+=1
    return root

def inorder(root):
    if root.left is not None:
        inorder(root.left)
    if root.count == 1:
        print(root.data, end = " ")
    else:
        for i in range(root.count):
            print(root.data, end = " ")
    if root.right is not None:
        inorder(root.right)

def main():
    root = Node(8)
    insert(root, 5)
    insert(root, 4)
    insert(root, -2)
    insert(root, -3)
    insert(root, -3)
    insert(root, 0)
    insert(root, 0)
    insert(root, 0)
    insert(root, 4)
    insert(root, 8)
    inorder(root)
main()
