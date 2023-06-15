def fn():
  fd = open("hashuri.in", "r")
  fd_out = open("hashuri.out", "w")
  hash = set()
  for i in range(int(fd.readline())):
  
      op, key = map(int, fd.readline().split(" "))
      
      has_key = key in hash
      
      if op == 1 and not has_key:
         hash.add(key)
      elif op == 2 and has_key:
         hash.remove(key)
      elif op == 3:
           fd_out.write("%d\n" % int(has_key))
fn()         
       
