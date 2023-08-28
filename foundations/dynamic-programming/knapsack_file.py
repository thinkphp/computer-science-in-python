class Object:
    def __init__(self, w, c):
        self.w = w
        self.c = c

def dynamic_programming_in_action(arr, N, Gmax):

    Profit = [[0 for j in range(Gmax+1 )] for i in range(0, N+1)]

    for i in range(1, N+1):

        for j in range(1, Gmax+1):

            if arr[i].w <= j:

               Profit[i][j] = max(arr[i].c + Profit[i-1][j-arr[i].w], Profit[i-1][j])

            else:

               Profit[i][j] = Profit[i-1][j]

    print(Profit[N][Gmax])

def fn():
    with open("rucsac2.in","r") as fp:
        lines = fp.readlines()
        content = [x.strip() for x in lines]
        num_of_objects = int(content[0].split(" ")[0])
        Gmax = int(content[0].split(" ")[1])
        arr = [0]
        for i in range(1,num_of_objects+1):
              w = int(content[i].split(" ")[0])
              c = int(content[i].split(" ")[1])
              arr.append(Object(w, c))

    dynamic_programming_in_action(arr, num_of_objects, Gmax)

fn()
