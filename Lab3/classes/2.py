class Shape:
    def __init__(self,length):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length=length
        super().__init__(length)
    def area(self):
        return self.length**2
a=Square(2)
print(a.area())
