class Rectangle:
    h=0
    r=0
    def __init__(self,a,b):
        self.h=a
        self.r=b
    def Area(self):
        print("Area is:",self.h*self.r)
        return self.h*self.r
    def circum(self):
        print("Circum is:",2*(self.h+self.r))
r1=Rectangle(2,3)
r2=Rectangle(5,4)
a=r1.Area()
print(a)
r1.circum()
b=r2.Area()
r2.circum()

