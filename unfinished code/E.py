#n=int(input())
#n,k=map(int,input().split())
#L=list(map(int,input().split()))

x=int(input())
for _ in range(x):
    n=int(input())
    L=list(map(int,input().split()))
    turn="First"
    while len(L)>0:
        print(L)
        if L[0]==1:
            L.pop()
        elif L.count(1)%2==1 or L.count(1)==0:
            L[0]=1
        else:
            L.pop(0)  
        turn="First" if turn=="Second" else "Second"
        print(L)
    if turn=="Second" :
        print("First")
    else:
        print("Second")


