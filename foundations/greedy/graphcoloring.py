def plus(arr, n):

    return list(map(lambda x: x + 1, arr))

def func():
    # we have 7 countries to color
    n = 7
    matrix = [[0,1,1,1,0,0,1],
              [1,0,1,1,0,0,0],
              [1,1,0,1,1,0,1],
              [1,1,1,0,1,0,1],
              [0,0,1,1,0,1,1],
              [0,0,0,0,1,0,1],
              [1,0,1,1,1,1,0]]

    mapColors = []

    mapColors = [0] * (n)

    color = -1

    ok = True

    mapColors[0] = 0

    for i in range(1, n):

        ok = False

        color = -1

        while ok is not True:

              color += 1

              ok = True

              for j in range(0, i):

                  if 1 == matrix[j][i] and mapColors[j] == color:

                      ok = False
        mapColors[i] = color

    mapColors = plus(mapColors, 1)

    print(mapColors)

func()
