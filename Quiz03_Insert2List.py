#Quiz 3
# inserting to a descending sorted list

L=list()
i=0
print("Input 10 numbers which are sorted")
while i<10:                  
    L.append(int(input()))
    i+=1
x=int(input("Enter X:"))
L.append(x)
ind=len(L)-1                       
while ind>0:
    if L[ind]>L[ind-1]:
        L[ind],L[ind-1]=L[ind-1],L[ind]
    ind-=1

print(L)


