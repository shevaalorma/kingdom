class Animal:
    def __init__(self,age):
        print('Animal init')
        self.__age = age

    def show(self):
        print(self.__age)

class Cat(Animal):
    def __init__(self,age,weight):

        print('Cat init')
        self.__age = age + 1
        self.__weight = weight

        super().__init__(age)


c = Cat(10,5)
c.show()

print(c.__dict__)