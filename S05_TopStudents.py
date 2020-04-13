Max1=0
Max2=0
avg=0
for i in range(10):
    avg=float(input("Enter the Avg:"))
    if avg>Max1:
        Max2=Max1
        Max1=avg
    elif avg>Max2:
        Max2=avg
print(Max1,Max2)
