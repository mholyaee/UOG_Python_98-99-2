def fact(n):
    i=1
    f=1
    while i<=n:
        f*=i
        i+=1
    return f
n,r= input("Enter 2 numbers:").split()
n=int(n)
r=int(r)
fn=fact(n)
fr=fact(r)
fd=fact(n-r)
print(fn/(fd*fr))
