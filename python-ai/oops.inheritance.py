class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class dog(Animal):
    def speak(self):
        print("bhow bhow")

class cat(Animal):
    def speak(self):
        print("meow meow")
        

d1 = dog("tommy",2)
print(d1.name,d1.age)
d1.speak()
c1 = cat("pussy",2)
print(c1.name,c1.age,)
c1.speak()
