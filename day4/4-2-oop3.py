class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s正在喊叫！" % self.name)


class Dog(Animal):
    def guard_home(self):
        print("%s可以看家" % self.name)


dog = Dog("田园犬", 2)
print(dog.eat())
print(dog.guard_home)
