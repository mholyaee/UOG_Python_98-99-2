def IsWeak(avg):
    if avg<=12:
        return True
    return False
def ComputingAvg(N):
    i=1
    Sum=0
    VSum=0
    while i<=N:
        grade=float(input("The grade:"))
        C=int(input("Vahed:"))
        Sum+=grade*C
        VSum+=C
        i+=1
    return Sum/VSum

NumberStu=int(input("Number of Students:"))
i=1
while i<=NumberStu:
    n=int(input("Number of Courses:"))
    avg=ComputingAvg(n)
    print("The average is:",avg)
    if IsWeak(avg):
        print(" The Average is lower than Normal")
    i+=1
