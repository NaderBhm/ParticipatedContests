n,m=map(int,input().split())
print((str(int((n/m))+1)+" ")*(n%m)+((str(int(n/m))+" ")*(m-(n%m))))