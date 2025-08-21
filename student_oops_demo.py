class Student:
    
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("The name of the student is ",self.name)
        print("the age of the student is ",self.age)
        print("the mark of the student is ",self.marks)
    def result(self):
        if self.marks>=400:
            print("passed")
        else:
            print("failed")
            
obj1=Student('jeeva',17,496)
obj2=Student('suriya',17,400)
obj1.display()
obj2.display()
obj1.result()
