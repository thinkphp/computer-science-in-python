def _s_u_b_s_e_t_s(n):

    stack = [0]

    stack[-1] = 1
    
    for i in range(0, len(stack)):

        if stack[i] > 0:

           print(stack[i], end = '\n')

    while not len(stack) == 0 :

        if stack[-1] < n:

           stack.append(stack[-1] + 1)

        else:

           stack.pop()

           if len(stack)!= 0:

              stack[-1] += 1


        for i in range(0, len(stack)):

           if stack[i] > 0:
            
              print(stack[i], end = ' ')

        print()              


def s_u_b_s_e_t_s( n ):

    vec = [ 0 ] * ( n + 1 )

    s = 0

    while not s == n:

        vec[ n - 1 ] += 1

        for i in range(n - 1, 0, -1):

            if vec[ i ] > 1:

               vec[ i ] -= 2

               vec[i - 1] += 1
        s = 0

        print("{",end='')
        for i in range(0, n):
            s += vec[i]
            if vec[i]:
               print(i + 1, end = ',')

        print("\b}",end='')
        print()

def subsets( n ):

    sizeof = 2**n

    for i in range(1, sizeof):

        print("{",end = '')

        for j in range(0, n):

            if ( 1 << j ) & i:

                print( j + 1, end = ',')

        print("\b}\n",end = '')

def main():

    n = int( input("Give me:  N = ") )
    _s_u_b_s_e_t_s( n )    
main()
