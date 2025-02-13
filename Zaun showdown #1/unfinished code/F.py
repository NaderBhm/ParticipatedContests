import math
def isPrime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

x=int(input())
for _ in range(x):
    a,b=map(int,input().split())
    if isPrime((a**2)-(b**2)):
        print("YES")
    else:
        print("NO")
