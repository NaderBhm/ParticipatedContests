x=int(input())
for _ in range(x):
    n=int(input())
    L=list([int(z) for z in input().split()])
    i=-1
    j=n
    s1,s2=0,0
    res=0
    while(i<j):
        if(s1<=s2):
            i+=1
            s1+=L[i]
        else:
            j-=1
            s2+=L[j]
        if(s1==s2 and i!=j):
            res=(n-j+i+1)
    print(res)
            
