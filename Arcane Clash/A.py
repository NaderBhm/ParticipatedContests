n=int(input())
L=list(map(int, input().split()))
res=[float('inf')]*n
 
for i in range(n):
    if L[i]==0:
        res[i]=0
    elif i>0:
        res[i]=res[i-1]+1
 
for i in range(n-2,-1,-1):
    res[i]=min(res[i],res[i+1]+1)
 
print(*res)