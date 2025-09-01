from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def describe(self):
        print("it is a shape")
class rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        self.area=self.l*self.b
        print(self.area)

rect=rectangle(10,20)
rect.describe()
rect.area()
