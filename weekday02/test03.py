class Animal:
    def shout(self):
        print('Animal shout')

class Cat(Animal):
    def shout(self):
        print('miao')

a = Animal()
a.shout()
c = Cat()
c.shout()

print(a.__dict__)
print(c.__dict__)
print(Animal.__dict__)
print(Cat.__dict__)

