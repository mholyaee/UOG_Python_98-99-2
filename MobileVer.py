Str=input("Your mobile phone:")
flag=True
if len(Str)==11 and Str[0]=='0':
    for i in Str:
        n=int(i)
        if n>=0 and n<=9:
            pass
        else:
            flag=False
            break
else:
    print("This number phone is not valid")
    flag=False
if flag:
    print("Is valid")
else:
    print("Is not Valid")
