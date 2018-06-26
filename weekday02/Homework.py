class Shape:
    @property
    def area(self):
        print('super method')


class Taiangle(Shape):
    def __init__(self, weight, height):
        super().__init__()
        self.__weight = weight
        self.__height = height

    @property
    def area(self):
        return (self.__weight * self.__height) / 2


class Round(Shape):
    @property
    def area(self):
        super().area()


class Rectangle(Shape): pass
