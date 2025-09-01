from abc import ABC,abstractmethod

class Payments(ABC):
    @abstractmethod
    def Onlinepayment(self):
        pass
    
    def greet(self):
        print("welcome to payment section")

class Debitcardpayment(Payments):
    
    def Onlinepayment(self):
        print("Online payment done using Debit card")
class Creditcard(Payments):
    
    def Onlinepayment(self):
        print("Online payment done using Credit card")
  
obj1=Debitcardpayment()
obj1.greet()
obj1.Onlinepayment()
obj2=Creditcard()
obj2.Onlinepayment()
