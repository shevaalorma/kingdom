class A:
    def __init__(self):
        print('A.init')
        self.a1 = 'a1'

    def __get__(self, instance, owner):
        print('A.__get__', self, instance, owner)

@classmethod
class B:
    x = A()

    def __init__(self):
        print('B.init')
        self.x = A()

print(B.x)
#print(B.x.a1)

print()

b =B()
print(B.x)
print('--------------------------')
print(b.x)

# print(b.__dict__)
# print(B.__dict__)