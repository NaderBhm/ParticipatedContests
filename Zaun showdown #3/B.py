def rev(x, L):
    seq = []
    g, d = 0, x - 1
    for i in range(x):
        if i % 2 == 0:
            seq.append(L[g])
            g += 1
        else:
            seq.append(L[d])
            d -= 1
    return seq
 
n = int(input())
for _ in range(n):
    x = int(input())
    L = list(map(int, input().split()))
    seq = rev(x, L)
    print(" ".join(map(str, seq)))