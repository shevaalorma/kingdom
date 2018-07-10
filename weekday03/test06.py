class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):
        print("A.__get__{} {} {}".format(self,instance,owner))
        return self


class B:
    x = A()

    def __init__(self):
        print('B.init')
        self.b = A()


print('-' * 20)
print(B.x)
print(B.x.a1)  #a1

print('='*20)
b = B()
print(b.x)
print(b.x.a1)

print(b.b)
print(B.__dict__)
print(b.__dict__)


