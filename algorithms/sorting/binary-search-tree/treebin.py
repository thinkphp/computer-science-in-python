class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):

    if root is None:

        return Node(value)

    if value < root.data:

        root.left = insert(root.left, value)

    elif value > root.data:

        root.right = insert(root.right, value)

    return root

def inorder(root):
    if root.left is not None:
        inorder(root.left)
    print(root.data, end = " ")
    if root.right is not None:
        inorder(root.right)

def main():

    root = Node(1)
    insert(root, -2)
    insert(root, -3)
    inorder(root)

main()
