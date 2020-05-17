class Mytime:
    h=0
    m=0
    s=0
    def SetTime(self,h,m,s):
        if h>=0 and h<=23:
            self.h=h
        else:
            self.h=0
        if m>=0 and m<=59:
            self.m=m
        else:
            self.m=0
        if s>=0 and s<60:
            self.s=s
        else:
            self.s=0
    def printTime12(self):
        if self.h<12:
            print(self.h,":",self.m,":",self.s," AM.")
        else:
            print(self.h-12, ":", self.m, ":", self.s, " PM.")
    def printTime24(self):
        print(self.h, ":", self.m, ":", self.s)
t=Mytime()
t.SetTime(23,45,56)
t.printTime12()
t.printTime24()
