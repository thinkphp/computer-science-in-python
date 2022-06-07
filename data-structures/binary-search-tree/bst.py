class Node:
 
    def __init__(self, key):
 
        self.left = None
 
        self.right = None
 
        self.data = key
 
def search(root, key):
 
    if root is None:
 
        return False
 
    elif root.data == key:
 
        return True
 
    elif root.data > key:
 
        return search(root.left, key)
 
    else:
        return search(root.right, key)
 
def insert(root, val):
 
    if root is None:
 
        print("added to BST: ", val)
 
        return Node(val)
 
    elif root.data > val:
 
        root.left = insert(root.left, val)
 
    elif root.data < val:
 
        root.right = insert(root.right, val)
 
    return root
 
def inorder(root):
 
    if root.left is not None:
 
        inorder(root.left)
 
    print(root.data, end = " ")
 
    if root.right is not None:
 
        inorder(root.right)
 
def preorder(root):
 
    print(root.data, end = " ")
 
    if root.left is not None:
 
        preorder(root.left)
 
    if root.right is not None:
 
        preorder(root.right)
 
def main():
 
    vec = [ 55, 22, 11, 22, 0, 33, 44, 555, 101, -101 ]
 
    print( vec )
 
    root = Node(-1 )
 
    for i in vec:
 
        insert( root, i )
 
 
    print("Inorder traversal:", end = " ")
 
    inorder(root)
 
    print()
 
    print("Preorder traversal:", end = " ")
 
    preorder(root)
 
    key = -101
    r = search(root, key)
 
    print()
 
    if r is True:
 
        print("%d is Found" % key)
 
    else:
 
        print("%d Not Found" % key)
main()
