class PartyAnimal:
   x = 0
   __a=20
   def party(self) :
     self.x = self.x + 1
     #x=x+1
     print("So far",self.x)
     print("So far", self.__a)
     #print(x)

an = PartyAnimal()
an.party()
an.party()
an.party()
print(an.x)
#print(an.__a) error



