class Father:
    def skills(self):
        print("Father: The skill is Driving")

class Mother:
    def skills(self):
        print("Mother: The skill is Cooking")

class Child(Father,Mother):
    def skills(self):
        super().skills()
        print("child:The child is Artist")

c=Child()
c.skills()
