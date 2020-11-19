class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getProfile(self):
        print(f"your name is : {self.name} and your age is {self.age}")


p = Person("danil",26) #inisialisasi object
p.getProfile()

p2 = Person("haykal", 2) #inisialisasi object
p2.getProfile()