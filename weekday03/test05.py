from functools import partial

class StaticMethod:
    def __init__(self,fn):
        print('Init')
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn


class A:

    @StaticMethod
    def foo():  # add = StaticMethod(add)
        print('StaticMethod')

    partial

f = A.foo
f()