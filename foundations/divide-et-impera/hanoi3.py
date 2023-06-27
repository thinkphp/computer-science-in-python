fin = open("hanoi.in","r")
fout = open("hanoi.out","w")
def h(d, s, a, t):
    if d == 1:
        fout.write('{} -> {}\n'.format(s, t))
        return
 
    h(d - 1, s, t, a)
    fout.write('{} -> {}\n'.format(s, t))    
    h(d - 1, a, s, t)
    

n=int(fin.read())


fout.write(str((1<<n)-1))
fout.write("\n")            
h(n,'A','B',
