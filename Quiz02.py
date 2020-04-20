n= int(input("Enter your number:"))

a=1
b=1
i=3
while i<=n:
    c=a+b
    a=b
    b=c
    i=i+1
print(n,"th element of fibonatchi is:",c)
