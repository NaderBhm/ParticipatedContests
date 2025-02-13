
n=int(input())
ch=""
for i in range(1,n+1):
    if i%2==1:
        ch+="I hate "
    else:
        ch+="I love "
    if i<n:
        ch+="that "
print(ch+"it")

