class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

d1 = dog("tommy",2)
d2 = dog("jerry",3)

c1 = cat("pussy",2)
c2 = cat("kityyt" , 3)

print(d1.name,d1.age)
print(d2.name,d2.age)

print(c1.name,c1.age)
print(c2.name,c2.age)