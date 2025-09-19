class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c

    def disp(self):
        print("student number:",self.sno)
        print("student name:",self.sname)
        print("student age:",self.sage)


class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
       super().__init__(a,b,c)
       self.mark1=m1
       self.mark2=m2
       self.mark3=m3
    def disp(self):
        super().disp()
        print("mark1=",self.mark1)
        print("mark2=",self.mark2)
        print("mark3=",self.mark3)

obj=marks(1,'abc',98,73,87,98)
obj.disp()
    
