from abc import ABC,abstractmethod

class Company(ABC):
    @abstractmethod
    def salary_calculation(self):
        pass
    
    def greet(self):
        print("welcome to our company")

class Salary(Company):
    
    def __init__(self,sal,total_days,leave):
        self.sal=sal
        self.total_days=total_days
        self.leave=leave
    def salary_calculation(self):
        self.total_salary=self.sal*(self.total_days-self.leave)
        return self.total_salary

obj1=Salary(500,30,9)
obj1.greet()
salary=obj1.salary_calculation()
print(f"the total salary is {salary}")
        
        
