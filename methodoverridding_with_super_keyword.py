class vechicle:
    
    def engine(self):
        print("350 cc engine")
class car(vechicle):
    
    def engine(self):
        super().engine()
        print("with turbo upgrade")
    def model(self):
        print("swift")

obj1=car()
obj1.engine()
