t=int(input())
for _ in range(t):
    a,b,c,x,y=list(map(int,input().split()))
    x=x-a
    y=y-b
    if (x>0):
        if c>x:
            c=c-x
            x=0
        else:
            x=x-c
            c=0
    if(y>0):
        y=y-c
    if (y>0) or (x>0):
        print("NO")
    else:
        print("YES")