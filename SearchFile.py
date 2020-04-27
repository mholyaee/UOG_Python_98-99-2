try:
    fp=open("D:\MyClasses\Python Programming\sample.txt")
    str=input("Find:")
    for Line in fp:
        temp=Line.split()
        for t in temp:
            if t==str:
                print(Line)


except:
    print("there isnt such file!")