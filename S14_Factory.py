class person:
    name=""
    family=""
    def __init__(self,n,f):
        self.name=n
        self.family=f
    def get_Info(self):
        print("name is:",self.name)
        print("Family:",self.family)
class employee(person):
    rank=0
    salary=0
    def Set_rank(self,r):
        self.rank=r
    def Compute_salary(self):
        self.salary=1/self.rank*3000
        self.get_Info()
        print("Wage is:",self.salary)
class contractor(person):
    hour=0
    wage=0
    def Set_hour(self,h):
        self.hour=h
    def Compute_wage(self):
        self.wage=self.hour*15
        self.get_Info()
        print("Wage is:",self.wage)
e1=employee("Mina","Yaghobi")
e1.Set_rank(3)
e1.Compute_salary()
e2=employee("Sajad","Ahmadi")
e2.Set_rank(2)
e2.Compute_salary()
c1=contractor("Ehsan","Asgari")
c1.Set_hour(100)
c1.Compute_wage()
