def check(a,b,x,t):
    hours=0
    days=0
    passedweekend=0
    for i in range(x,7*n):
        if i%7==5 or i%7==6:
            passedweekend+=1
            continue
        days+=1
        for j in range(2):
            if available[a][i][j] and available[b][i][j]:
                hours+=4
                if hours>=t:
                    return days+x+passedweekend
    return -1
 
n,m,q=map(int,input().split())
L=[]
for _ in range(q):
    L.append(list(map(int,input().split())))
 
available = [[[1 for _ in range(2)] for _ in range(7*n)] for _ in range(m)]
for x in L:
    if x[0]==1:
        available[x[1]-1][x[2]-1]=[0,0]
    elif x[0]==2:
        available[x[1]-1][x[2]-1][x[3]-1]=0
    elif x[0]==3:
        print(check(x[1]-1,x[2]-1,x[3]-1,x[4]))
