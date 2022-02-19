class Shape:
    def __init__(self,length,width):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
a,b=map(int,input().split())
s=Rectangle(a,b)
print(s.area())

