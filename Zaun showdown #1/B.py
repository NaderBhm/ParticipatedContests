n=int(input())
Li=list()
for i in range(n):
    Li.append(list(map(int,input().split())))
counter=0
for i in range(n):
    for j in range(n):
        if Li[i][1]==Li[j][0]:
            counter+=1
        j+=1
    i+=1
print(counter)
    

            
