class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def set_grade(self):
        return self.grade



s1 = Student("pramod",22,"A")

print(s1.name)
print(s1.age)
print(s1.set_grade())
