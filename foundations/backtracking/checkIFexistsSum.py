def subset(working_set, k, n):
    if k == n:
        s = {k for k in working_set if working_set[k] == 1}
        solutions.append(s)
    else:
        k += 1
        for i in [0,1]:
            working_set[k] = i
            subset(working_set, k, n);
def func():
    sum = 10
    arr = [5,1,2,2,3,7]
    n = len(arr)
    global solutions
    solutions = []
    subset({}, 0, n)
    solutions.pop(0)
    for sol in solutions:
        s = list(sol)
        acc = 0
        for i in s:
            acc += arr[i-1]
        if acc == sum:
            for i in s:
                print(arr[i-1], end =" ")
            print()
func()
