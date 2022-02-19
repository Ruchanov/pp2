class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        return self.x,self.y
    
    def move(self,a,b):
        self.x=a
        self.y=b

    def dist(self,a,b):
        return ((a-self.x)**2+(b-self.y)**2)**0.5
s=Point(1,2)
print(s.dist(3,4))