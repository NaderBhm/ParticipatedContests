x=int(input())
for _ in range(x):
    n=int(input())
    x11,y11,x12,y12=map(int,input().split())
    x21,y21,x22,y22=map(int,input().split())
    if set(range(x11,x12+1)).intersection(set(range(x21,x22+1))) or set(range(y11,y12+1)).intersection(set(range(y21,y22+1))):
        print(1)
    else:
        print(2)