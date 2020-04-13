counter=0
for i in range(10):
    income=int((input("Enter the income of family:")))
    if income<=200:
               counter+=1
print("Number of qualified family:",counter)
