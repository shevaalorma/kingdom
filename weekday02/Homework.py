class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age



tom = Person('Tom')
print(tom.age)
tom.age = 20
print(tom.age)