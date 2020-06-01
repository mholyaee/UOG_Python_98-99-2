class book:
    name=""
    Author=""
    Topic=""
    Pages=0
    Publisher=""
    def __init__(self,n):
        self.name=n
    def edit(self):
        print("Enter the information of this book:")
        self.name=input("Name:")
        self.Author=input("Author:")
        self.Pages=int(input("PageNumber:"))
        self.Topic=input("Topic:")
        self.Publisher=input("Publisher:")
    def printName(self):
        print(self.name)
    def getTopic(self):
        return self.Topic
b1=book("Birad")
b2=book("Kashti Pahloo gerefte")
b3=book("Tanha davidan")
b4=book("Foroghe Abadiat")
b5=book("Kafsh baz")
b1.edit()
b2.edit()
b3.edit()
b4.edit()
b5.edit()
if b1.getTopic()=="Religion":
    b1.printName()
if b2.getTopic()=="Religion":
    b2.printName()
if b3.getTopic() == "Religion":
        b3.printName()
if b4.getTopic() == "Religion":
        b4.printName()
if b5.getTopic() == "Religion":
        b5.printName()

