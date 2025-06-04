x=int(input())
for _ in range(x):
    n=int(input())
    L=list(map(int,input().split()))
    L.sort(reverse=True)
    while len(L)>0 and L.count(L[0])%2==0:
        temp=L[0]
        while len(L)>0 and L.count(temp)>0:
            L.remove(L[0])
    if len(L)==0:
        print("No")
    else: 
        print("Yes")
 
    
 