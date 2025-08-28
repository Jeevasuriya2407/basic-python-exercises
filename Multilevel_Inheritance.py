class Dog:
    def variant(self):
        print("im a dog")

class Breed(Dog):
    def breed(self):
        print("it is a dolmination")

class Age(Breed):
    def age(self):
        print("the age is 5")

obj1=Age()
obj1.breed()
obj1.variant()
