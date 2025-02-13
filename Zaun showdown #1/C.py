n=int(input())
for i in range(n):
    ch=input()
    if ch.find("a")==-1:
        print("No")
    else:
        ss="a"
        test=True
        for i in range(1,len(ch)):

            if (ss+str(chr(97+i))) in ch: 
                ss=ss+str(chr(97+i))
            elif str(chr(97+i)+ss) in ch:
                ss=str(chr(97+i))+ss
            else:
                test=False
                break 
        if test:
            print("Yes")
        else:
            print("No")