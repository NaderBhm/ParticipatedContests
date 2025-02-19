x=int(input())
for _ in range(x):
    n,k=[int(x) for x in input().split()]
    L=list()
    for i in range(n):
        L.append(list([int(z) for z in input().split()]))
    somm=0
    Test=True
    for i in range(n//2):
        if Test==False:
            break
        for j in range(n//2):
            if L[i][j]!=L[n-i-1][n-j-1]:
                if somm==k:
                    Test=False
                    print("NO")
                    break 
                else:
                    somm+=1
    if Test:
        print("Yes")
