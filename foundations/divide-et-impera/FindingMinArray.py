def findMin(arr, left, right):

    if left == right:
        return arr[left]
    else:
        m = (left + right) >> 1
        a = findMin(arr, left, m);
        b = findMin(arr, m + 1, right)
        if a < b:
           return a
        else:
           return b

def main():

    arr = [1,23,-13,421,5,10];
    min = findMin(arr, 0, len(arr) -1)
    print(min)

main()
