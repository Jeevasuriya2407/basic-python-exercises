class Vechicle:
    def engine(self):
        print("engine type BS6")

class Swift(Vechicle):
    def Launchedyear(self):
        print("Launched on 2006")

class Innova(Vechicle):
    def Launchedyear(self):
        print("Launched on 1990")

obj1=Innova()
obj2=Swift()

obj1.Launchedyear()
obj2.Launchedyear()

obj1.engine()
