a,b=input("Enter 2 measures:").split()
a=int(a)
b=int(b)
if a>0 and b>0:
    if a==b:
        print("square")
    else:
        print("rectangle")
if a<=0:
    print("a<0")
if b<=0:
    print("b<0")

    
