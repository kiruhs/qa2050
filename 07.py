# polymorphism

# class Geom:
#     name = "Geom"
#     color = "blue"
#     length = 30
#
#     def draw(self):
#         print("Some figure drawing")
#
#     def get_per(self):
#         try:
#             raise NotImplementedError("This method should be implemented in a child class")
#         except NotImplementedError as err:
#             return err
#
#
#
# g = Geom()
# print(g.color)
# print(g.length)
# # g.get_per()
#
# class Rectangle(Geom):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):   # overriding
#         return 2*(self.w+self.h)
#
#
# class Square(Geom):
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4*self.a
#
#
#
# class Triangle(Geom):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_per(self):
#         return self.a + self.b + self.c

# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1,2,3)
# t2 = Triangle(4,5,6)

# geom = [g, Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20), Triangle(1,2,3), Triangle(4,5,6)]
#
# for gg in geom:
#     print(gg.get_per())

# print(r1.get_per(), r2.get_per())
# print(s1.get_per(), s2.get_per())

# class Calculator:
#     def add(self, a=0, b=0, c=0):
#         print(a+b+c)
#
#
# calc = Calculator()
# calc.add(3, 4, 5)
# calc.add(2, 1)
# calc.add(10)
# calc.add()

# print("1", "2", True)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattribute__(self, item):
#         print("method __getattribute__()")
#         print("it is my method")
#         if item == "x":
#             raise ValueError("no access")
#         else:
#             # return super().__getattribute__(item)
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#
#         if key == 'z':
#             raise AttributeError("not allowed name")
#         # if key not in ("x", "y"):
#         #     print("New attributes are not allowed for this class")
#         else:
#             print("it is my __setattr__")
#             object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         print("__getattr__:", item)
#         return False
#
#     def __delattr__(self, item):
#         print(f"now the attribute {item} is deleted")
#         object.__delattr__(self,item)
#
# p1 = Point(2, 3)
# y = p1.y
# x = p1.x
# p1.y = 50
# y = p1.y
# print(y)
# p1.a = 10
# print(p1.hello)
# print(p1.__dict__)
# del p1.y
# print(p1.__dict__)


# print(dir(p1))


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):
#         # print("method works")
#         self.__counter += step
#         return self.__counter
#
# c = Counter()
# c(0)
# c(10)
# res = c(-40)
# print(res)
#
# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#     def __abs__(self):
#         return list(map(abs, self.__coord))
#
# p = Point(1, -2)
# p2 = Point(2, 4, -8, 4, 5, -76.908)
# print(len(p2))
# print(dir(p))

# print(abs(p))
# print(abs(p2))

# print(len([1,2,6]))
# print(len((1,2,6)))
# print(len(11111111))

# print(dir(object))
