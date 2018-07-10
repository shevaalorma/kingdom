class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def show(self):
        print(self.x, self.y)


# p = Point(4,5)
# print(p)
# print(p.__dict__)
# p.__dict__['y'] = 16
# print(p.__dict__)
# p.z = 10
# print(p.__dict__)
# print(dir(p))
# print(p.__dict__)

p1 = Point(4, 5)
p2 = Point(10, 10)
print(repr(p1), repr(p2), sep='\n')
print(p1.__dict__)
setattr(p1, "y", 16)
setattr(p1, "z", 10)
print(getattr(p1, '__dict__'))

if hasattr(p1, 'show'):
    getattr(p1, "show")

if not hasattr(Point, 'add'):
    setattr(Point, 'add', lambda self, other: Point((self.x + other.x), (self.y + other.y)))

if not hasattr(p1,'sub'):
    setattr(p1,'sub',lambda self , other: Point(self.x - other.x,self.y - other.y))


print("_"* 20)
print(Point.add)
print(p1.add)
print(p1.add(p2))

print("_"* 20)
print(p1.sub(p1,p1))
print(p1.sub)

print(p1.__dict__)
print(Point.__dict__)