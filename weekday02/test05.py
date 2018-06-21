class Animal:
    @classmethod
    def class_method(cls):
        print('class_method_animal')

    @staticmethod
    def static_method():
        print('static_method_animal')


class Cat(Animal):
    @classmethod
    def class_method(cls):
        print('class_method_cat')

    @staticmethod
    def static_method():
        print('static_method_cat')

c = Cat()
c.class_method()
c.static_method()