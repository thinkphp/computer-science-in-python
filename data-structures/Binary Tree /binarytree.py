def main():
    n = 8
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    def read():
        nonlocal n
        n = int(input("nodes = "))
        for i in range(1,n+1):
            print("node %d:"%i)
            node = int(input("left = "))
            left[i] = node
            node = int(input("right = "))
            right[i] = node
    def inorder(node):
        if node != 0:
            inorder(left[node])
            print("%d "%node, end = " ")
            inorder(right[node])
    def preorder(node):
        if node != 0:
            print("%d "%node, end = " ")
            preorder(left[node])
            preorder(right[node])
    def postorder(node):
        if node != 0:
           postorder(left[node])
           postorder(right[node])
           print("%d "%node, end = " ")
    read()
    print(left)
    print(right)
    print()
    print("Inorder: ")
    inorder(1)
    print()
    print("Preorder: ")
    preorder(1)
    print()
    print("Postorder: ")
    postorder(1)

if __name__ == "__main__":
    main()
