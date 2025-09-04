class School:
    school="Shakespeare matriculation school"
    
    @classmethod
    def new_method(cls,new_school):
        cls.new_school=new_school
        print(f"the new School is ",cls.new_school)
    @staticmethod
    def age(age):
        return age>18

School.new_method("john matriculation school")
print(School.age(21))
print(School.age(2))

