class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def insert(root, key):

       if root is None:
           root = Node(key)

       elif root.data > key:
            root.left = insert(root.left, key)

       elif root.data < key:
            root.right = insert(root.right, key)

       return root

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

def mostlyRight(root):

    if root.left != None:
       root = root.left

    return root

def delete(root, key):

    if root is None:
       return root
    elif root.data < key:
         root.right = delete(root.right, key)
    elif root.data > key:
         root.left = delete(root.left, key)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left == None:
             temp = root.right
             root = None
             return temp

        elif root.right == None:
             temp = root.left
             root = None
             return temp
        elif root.left is not None and root.right is not None:
            temp = mostlyRight(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)


    return root


def search(root, key):

    pass


def main():
    root = Node(10)
    insert(root, 4)
    insert(root, 7)
    insert(root, 3)
    insert(root, -3)
    insert(root, 13)
    insert(root, 5)
    inorder(root)

    print()

    key = 13
    print("Delete %d" % key)
    delete(root, key)

    inorder(root)
main()
