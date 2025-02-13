#n=int(input())
#n,k=map(int,input().split())
#L=list(map(int,input().split()))

n,l=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
space=0
for i in range(n-1):
    space=max(space,L[i+1]-L[i])
space=space/2
if L[0]!=0:
    space=max(space,L[0])
if L[n-1]!=l:
    space=max(space,l-L[n-1])
print(space)