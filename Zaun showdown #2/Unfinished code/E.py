z = int(input())
for _ in range(z):
    n = int(input())
    L = list([int(x) for x in input().split()])
    s=0
    max=L[0]
    for i in range(n):
        s=L[i]
        if(max<s):
            max=s
        j=i+1
        while((j<n)and(abs(L[j])%2)!=(abs(L[j-1])%2)):
            s+=L[j]
            if(max<s):
                max=s
            j+=1
    print(max)
    
        
