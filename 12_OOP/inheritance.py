class Parent:
    def __init__(self, nama, age):
        self.nama = nama
        self.age = age

    def getPerson(self):
        print(f"name : {self.nama} and age : {self.age}")

    def parentFunc(self):
        print("this is the parent func")

    def berjalan(self):
        print("berlari")

# inheritance class turunan
class Child(Parent):
    # def __init__(self):
    #     # print("this is the child class")
    #     pass

    def childFunc(self):
        print("this is the child func")

    def berjalan(self):
        print("santai")

# ------------------------------------------------

# inisialisasi object
p = Parent("danil", 26)
p.getPerson()
p.berjalan()

c = Child("udinn", 24)
c.getPerson()
c.berjalan()
# c.childFunc()
# c.parentFunc()