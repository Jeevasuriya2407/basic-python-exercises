class Shape:
    def area(self):
        pass
class rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.res=self.l*self.b
        return self.res
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        self.res=3.14*self.r*self.r
        return self.res

lst=[rectangle(10,20),Circle(10)]

for i in lst:
    print("Area: ",i.area())
