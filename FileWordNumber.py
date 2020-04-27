Sum=0
try:
    fp=open("D:\MyClasses\Python Programming\sample.txt")
    for Line in fp:
        temp=Line.split()
        L=len(temp)
        Sum+=L
    print("The number of words:",Sum)

except:
    print("there isnt such file!")
    