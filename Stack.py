class Stack:
    top=-1
    L=list()
    def push(self,a):
        self.L.append(a)
        self.top=self.top+1
    def pop(self):
        if not (self.IsEmpty()):
            m= self.L.pop(self.top)
            self.top=self.top-1
            return m
    def IsEmpty(self):
        if self.top==-1:
            print("Stack is empty")
            return 1
        return 0
    def StackSize(self):
        print(self.top+1)
s=Stack()
s.push(10)
s.push(15)
x=s.pop()
print(x)
s.StackSize()