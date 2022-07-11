class Figure:
    def __init__(self,color):
        self.color=color

class Circle(Figure):
    def __init__(self,radius,color):
        self.radius=radius
        super().__init__(color)

    def area(self):
        return 2*3.14*self.radius**2
    
    def len(self):
        return 2*3.14*self.radius

    def compare(self, r2):
        if self.area()> r2.area():
            print(f'first is bigger')
        else:
            print(f'Second is bigger')

class Square(Figure):
    def __init__(self,length,color):
        self.length=length
        super().__init__(color)

    def area(self):
        return self.length**2
    
    def per(self):
        return 4*self.length
    
    def compare(self, s2):
        if self.per()> s2.per():
            print(f'first is bigger')
        else:
            print(f'Second is bigger')
    
def compare(circle,square):
    if circle.area()>square.area():
        print('first')
    else:
        print('second')


c1=Circle(4,'black')
c2=Circle(5,'brown')
s1=Square(10,'white')
s2=Square(5,'white')

print(c1.compare(c2))

print(s1.compare(s2))