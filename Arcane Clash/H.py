L=list(map(int,input().split()))
x=sum(L)/2
if sum(L)%2!=0:
    print("No")
else:
    L.sort()
    for i in range(6-2):
        for j in range(i+1,6-1):
            for k in range(j+1,6):
                if L[i]+L[j]+L[k]==x:
                    print("Yes")
                    exit(0)
    print("No")