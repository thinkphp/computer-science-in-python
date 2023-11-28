"""
Sequential Search:
the list or array is traversed sequentially and every element is checked.
"""

def main():
    numbers = [number for number in range(50, 0,-1)]
    result = linear(numbers, 1)
    print(result)


def linear(arr:list, target:int) -> int:
    """
        this function takes a list and a target number
        and do linear searching in array if
        function found number in array return
        index of it otherwise return -1
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def test_ok():
    n = [x for x in range(50)]
    assert linear(n, 4) == n.index(4)
    print("Assertion Completed!")


if __name__ == "__main__":
    main()
