class shape:
    Area=0
    Cir=0
    h=0
    w=0
    def __init__(self,a,b):
        self.h=a
        self.w=b
    def getArea(self):
        print(self.Area)
    def getCir(self):
        print(self.Cir)

class Rectangle(shape):
    def ComputeArea(self):
        self.Area = self.h * self.w
        self.getArea()
    def ComputeCir(self):
        self.Cir = (self.h + self.w) * 2
        self.getCir()
class Triangle(shape):
    def ComputeArea(self):
        self.Area=self.h*self.w/2
        self.getArea()
class Rhombus(shape):
    def ComputeArea(self):
        self.Area=self.h*self.w/2
        self.getArea()

rec=Rectangle(5,6)
rec.ComputeArea()
rec.ComputeCir()
Tri=Triangle(4,9)
Tri.ComputeArea()
Rho=Rhombus(7,5)
Rho.ComputeArea()

