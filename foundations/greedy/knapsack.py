class Object:
    def __init__(self, w, v, index):
        self.weight = float(w)
        self.value = float(v)
        self.index = int(index)
    def __repr__(self):
        return repr((self.index, self.weight, self.value))
arr = []
filepath = 'knapsack.in'
with open(filepath) as fp:
   lines = fp.readlines()
   content = [x.strip() for x in lines]
   capacity = float(content[0])
   content.pop(0)
   i = 0
   for item in content:
       ob = item.split(" ")
       arr.append(Object(ob[0], ob[1], i))
       i+=1
arr = sorted(arr, key = lambda x: x.weight/x.value)

i = 0
while capacity > 0:
    if capacity > arr[i].weight:
        capacity -= arr[i].weight
        i+=1
    else:
        capacity = -capacity

for j in range(0, i):
    print("Object:%d. weight=%f value=%f completed"%(arr[j].index, arr[j].weight, arr[j].value))
if capacity < 0:
    print("Object:%d. weight=%f value=%f %f fractional"%(arr[i].index, arr[i].weight, arr[i].value, capacity))
