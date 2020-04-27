try:
    fp=open("D:\MyClasses\Python Programming\sample2.txt")
    count=0
    for Line in fp:
        count+=1
    print("Numbe of lines:",count)
except:
    print("there isnt such file!")