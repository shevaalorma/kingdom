class Animal:
    __COUNT = 0
    HEIGHT = 0

    def __init__(self,age,weight,height):
        self.__COUNT += 1
        self.age = age
        self.__weight = weight
        self.HEIGHT = height

    def eat(self):
        print('{}'.format(self.__class__.__name__))

    def __getweight(self):
        print(self.__weight)

    @classmethod
    def showcount1(cls):
        print(cls.__COUNT)

    @classmethod
    def __showcount2(cls):
        print(cls.__COUNT)

class Cat(Animal):
    NAME = 'CAT'

#c = Cat()
c = Cat(3,5,15)
c.eat()
print(c.HEIGHT)
print(Animal.__dict__)