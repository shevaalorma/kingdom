class Animal:
    def __init__(self,name):
        self.__name = name


    def shout(self):
        print('{}shout'.format(self.__class__.__name__))

    def name(self):
        return self.__name

a = Animal('monster')
a.shout()

class Cat(Animal):
   pass

cat = Cat('garfield')
cat.shout()
print(cat.name)

class Dog(Animal):
    pass

dog = Dog('ahuang')
dog.shout()
print(dog.name)