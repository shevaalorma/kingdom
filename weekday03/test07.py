class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):
        print("A.__get__{} {} {}".format(self, instance, owner))
        return self

    def __set__(self, instance, value):
        print("A.__get__{} {} {} ".format(self, instance, value))
        self.data = value


class B:
    x = A()

    def __init__(self):
        print('B.init')
        self.b ='self .x'


print('-' * 20)
print(B.x)
print(B.x.a1)  # a1

print('=' * 20)
b = B()
print(b.x)
print(b.x.a1)

b.x = 500
# print('bbbb   '+b.x.a1)
print()
print(B.__dict__)
print(b.__dict__)

