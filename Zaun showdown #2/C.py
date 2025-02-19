x=int(input())
for _ in range(x):
    n=int(input())
    L=list([int(z) for z in input().split()])
    L[L.index(min(L))]+=1
    summ=1
    for i in L:
        summ*=i
    print(summ)