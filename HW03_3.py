op,a,b=input("The opreator and oprands:").split()
a=int(a)
b=int(b)
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
else:
    try:
        print(a/b)
    except:
        print(-1)
