def func():

    class MapColoring:

          def __init__(self, nodes, edges, data):
              self.nodes = nodes
              self.data = data
              self.matrix = [[0 for i in range(nodes+1)] for j in range(nodes+1)]
              self.stack = [0] * (nodes+10)

              for edges in data:
                  x, y = edges[0], edges[1]
                  self.matrix[x][y] = 1
                  self.matrix[y][x] = 1

          def displayMatrixAdjcent(self):

              for i in range(1, self.nodes+1):
                  for j in range(1, self.nodes+1):
                      print(self.matrix[i][j], end = " ")
                  print("")

          def init(self):
              self.stack[self.level] = 0

          def succ(self):
              if self.stack[self.level] < 4:
                 self.stack[self.level] += 1
                 return True
              return False

          def valid(self):
              for i in range(0, self.level):
                  if self.matrix[ self.level ][ i ] == 1 and self.stack[self.level] == self.stack[i]:
                      return False
              return True

          def sol(self):
              return self.level == self.nodes

          def printf(self):
              for i in range(1,self.nodes+1):
                   print(self.stack[i], end = " ")
              print()

          def searchSolutions(self):
              self.stack[1] = 1
              self.level = 2

              while self.level > 0:
                  h = True
                  v = False
                  while h is True and v is False:
                        h = self.succ()
                        if h is True:
                            v = self.valid()
                  if h is True:
                      if self.sol() is True:
                          self.printf()
                      else:
                          self.level +=1
                          self.init()
                  else:
                      self.level-=1

    nodes = 5
    edges = 8
    data = [ [1,2],[1,4],[2,3],[2,5],[3,1],[3,5],[4,5] ]
    ob = MapColoring(nodes, edges, data)
    ob.searchSolutions()
func()
