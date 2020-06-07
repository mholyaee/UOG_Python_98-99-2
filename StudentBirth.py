class Mydate:
    d=0
    m=0
    y=0
    def __init__(self,d,m,y):
        self.y=y
        self.m=m
        self.d=d
    def update(self):
        self.d=int(input("Day:"))
        self.m = int(input("Month:"))
        self.y = int(input("Year:"))
    def show(self):
        print(self.y,"/",self.m,"/",self.d)

class Student:
    Name=""
    Field=""
    def __init__(self):
        self.Birthday = Mydate(0, 0, 0)
        self.Name=input("Name:")
        self.Field=input("Field:")
        print("Birthday:")
        self.Birthday.update()
    def getName(self):
        return self.Name

St=list()
i=1
while i<=5:
    St.append(Student())
    i+=1
for s in St:
    if s.Field=="Computer":
        print(s.getName())
        s.Birthday.show()

