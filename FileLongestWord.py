Longest=''
try:
    fp=open("D:\MyClasses\Python Programming\sample.txt")
    for Line in fp:
        temp=Line.split()
        for w in temp:
           if len(w)>len(Longest):
               Longest=w
    print("The longest word:",Longest)

except:
    print("there isnt such file!")