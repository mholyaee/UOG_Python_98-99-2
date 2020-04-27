L1=list()
L2=list()
n1=int(input("Size of the first list:"))
for i in range(n1):
    L1.append(int(input("The measure:")))
n2=int(input("Size of the second list:"))
for i in range(n2):
    L2.append(int(input("The measure:")))
L1=L1+L2
print(L1)
for i in range(len(L1)):
    j=i+1
    while j<len(L1):
        if L1[i]==L1[j]:
            L1.pop(j)
        j+=1
print(L1)
