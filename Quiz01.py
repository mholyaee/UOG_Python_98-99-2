a,b,c,d=(input("Enter four numbers:").split())
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if b>a:
    a,b=b,a
if c>a:
    a,c=c,a
if d>a:
    a,d=d,a
print("The max number is:",a)

