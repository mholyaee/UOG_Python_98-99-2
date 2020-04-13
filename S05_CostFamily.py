i=1
Max=0
j=0
while i<=12:
    cost=int(input("The cost:"))
    if Max<cost:
        Max=cost
        j=i
    i+=1
print("The max cost is:",Max," The number of month is:",j)
