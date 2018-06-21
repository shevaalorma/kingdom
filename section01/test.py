class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age

    def age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

tom = Person('Tom')



import random
class RandomNums:
    def __init__(self,ints=1,min=1,max=100,lots=1):
        self._ints = ints
        self._min= min
        self._max= max
        self._lots = lots

    def bring(self):
        return [random.randint(self._min,self._max) for i in range(self._ints)]

x = RandomNums
print(x(10,1,55))