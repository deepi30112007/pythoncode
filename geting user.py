class student:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def display(self):
        print("student no:",self.sno)
        print("student name:",self.name)
        print("student age:",self.age)
        
x=int(input("enter your roll no:"))
y=input("enter your name:")
z=int(input("enter your age:"))

obj=student(x,y,z)
obj.display()
