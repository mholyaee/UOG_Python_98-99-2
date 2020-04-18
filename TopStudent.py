i=1
Max1=0
Max2=0
Max3=0
while i<=10:
    print("Major and Average:")
    M,avg=input().split()
    avg=float(avg)
    if avg>Max1:
        Max1=avg
    if M=="Computer" and avg>Max2:
        Max2=avg
    if M=="Electronic" and avg> Max3:
        Max3=avg
    i+=1
print(" Top student of Computer:",Max2)
print(" Top sudent of Electronic:", Max3)
print (" Top of College:",Max1)