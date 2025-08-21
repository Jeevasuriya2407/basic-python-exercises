class Circle:
    
    def __init__(self,rad):
        self.rad=rad
    
    def result(self):
        self.circumfrence=2*3.14*self.rad
        self.area=3.14*self.rad*self.rad
        
    def display(self):
        print("the circumfrence of a circle is",self.circumfrence)
        print("the area of a circle is ",self.area)

obj1=Circle(30)
obj1.result()
obj1.display()
