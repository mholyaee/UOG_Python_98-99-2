class Mydate:
    d=0
    m=0
    y=0
    def __init__(self,y,m,d):
        self.d=d
        self.m=m
        self.y=y
    def update(self):
        self.d=int(input("Day:"))
        self.m = int(input("Month:"))
        self.y = int(input("Year:"))
    def Subtract(self,cd):
        days=0
        if self.d>cd.d:
            cd.m-=1
            cd.d+=30
        days=cd.d-self.d
        if self.m>cd.m:
            cd.y-=1
            cd.m+=12
        days+=(cd.m-self.m)*30
        days+=(cd.y-self.y)*365
        return days
    def show(self):
        print(self.y,"/",self.m,"/",self.d)
class dairy:
    Name = ""
    def __init__(self, N):
        self.ProductionDate = Mydate(0, 0, 0)
        self.Name = N
        self.ProductionDate.update()

    def GetName(self):
        return self.Name

    def GetProductTime(self):
        return self.ProductionDate
import datetime
ProductList=list()
i=1;
while i<=5:
    Pname=input("Product Name:")
    ProductList.append(dairy(Pname))
    i+=1
Current=datetime.datetime.now().date()
Today=Mydate(Current.year,Current.month,Current.day)
print("Today:")
Today.show()
for l in ProductList:
    if l.GetProductTime().Subtract(Today)>30:
        print("Expired:",l.Name)

