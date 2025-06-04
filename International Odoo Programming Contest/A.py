ch=input()
odoo=ch.find('.odoo.com')
if odoo == -1:
    print("No")
else:
    ch=ch[:odoo]
    if len(ch)<4 or len(ch)>30:
        print("No")
    else:
        if ch.lower() != ch:
            print("No")
        else:
            if ch[0].isalnum() and ch[-1].isalnum():
                for i in range(1,len(ch)):
                    if ch[i].isalnum() or ch[i]=='-':
                        continue
                    else:
                        print("No")
                        break
                else:
                    print("Yes")
            else:
                print("No")