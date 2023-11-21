A,B,C=map(int,input().split())
 
if A!=0:
    if B*B-4*A*C<0:
        print(0)
    elif B*B-4*A*C==0:
        print(1)
        ANS=-B/(2*A)
        print(ANS)
    else:
        print(2)
        ANS=[(-B-(B*B-4*A*C)**(1/2))/(2*A)]
        ANS.append((-B+(B*B-4*A*C)**(1/2))/(2*A))
        ANS.sort()
        print(ANS[0])
        print(ANS[1])
elif A==0:
    if B!=0:
        print(1)
        ANS=(-C)/B
        print(ANS)
    else:
        if C==0:
            print(-1)
        else:
            print(0)
