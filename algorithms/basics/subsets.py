import sys

def generate_subsets(strr, n):

    #f = open("submultimi.out", "w")

    total = pow(2, n)
    
    for i in range(1, total):

        for x in range(0, n):

            if i & (1<<x) != 0:

               #sys.stdout.write(str(x+1) + " ")
               sys.stdout.write(strr[x] + " ")
               #f.write(str(x+1) + " ")	

        #f.write("\n")
        print ""
               

def main():

    str = "abc"
    #f = open("submultimi.in", "r")
    #n = int(f.readline())    
    n = len( str )
    #n = 4

    generate_subsets(str, n)
main()