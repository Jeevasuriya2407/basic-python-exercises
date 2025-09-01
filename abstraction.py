from abc import ABC,abstractmethod

class Vechicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vechicle):
    def start(self):
        print("car starts with the help of key")
class Bike(Vechicle):
    def start(self):
        print("bike starts with the help of kick or button")

obj1=Car()
obj1.start()
obj2=Bike()
obj2.start()
