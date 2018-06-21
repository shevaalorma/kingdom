class Animal:
    def shout(self):
        print('Animal shout')

class Cat(Animal):
    def shout(self):
        print('miao')

    def shout(self):
        print(super())
        print(super(Cat,self))
        super().shout()
        super(Cat,self).shout()
        self.__class__.__base__.shout(self)

a = Animal()
a.shout()
c = Cat()
c.shout()