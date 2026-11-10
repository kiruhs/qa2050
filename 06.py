# class Point:
#     color = "red"
#     circle = 2
# a = Point()

# class Geom:
#     name = "Geom"
#     color = "black"
#     width = 2
#
# class Line(Geom):
#     length = 10
#
# l1 = Line()
# print(l1.length)
# l1.color = "red"
# print(l1.color)
# g1 = Geom()
# print(g1.length)

# class Point:
#     color = "red"
#     circle = 2
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# a = Point(1,2)
# b = Point(3,4)
# c = Point(5)
# d = Point()
#
# print(a.x)
# print(b.x)
# print(c.y)

# Наследование - Inheritance
# class Geom:
#     name = "Geom"
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#
# class Rect5(Geom):
#     def __str__(self):
#         return f"this is object of {self.__class__}"
#
#     def draw(self):
#         print("Rectangle drawing")

# class Square(Geom):
#     def draw(self):
#         print("Square drawing")
#
# r1 = Rect5()
# r1.set_coords(4, 3, 9,0)
# print(r1)

# print(r1.x1)
# s1 = Square()
# s1.set_coords(6, 7, 8, 9)

# s1.draw()

# print(issubclass(Square, Geom))
# print(isinstance(s1, Rect))
# print(issubclass(Square, object))
# print(Square.mro())

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
# v = Vector([1, 2, 3])
# print(v)
#
# print(issubclass(Vector, object))
# print(isinstance(v, Vector))
# print(Vector.mro())


# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, x2, y1, y2):
#         print(f"Initialization Geom for {self.__class__}")
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#
# class Line(Geom):
#     def draw(self):
#         print("Line drawing")
#
# class Rect(Geom):
#     def __init__(self, x1, x2, y1, y2, fill=None):
#         super().__init__(x1, x2, y1, y2)
#         self.fill = fill
#         print("Rect initialization")
#
#     def draw(self):
#         print("Rectangle drawing")
#
# l1 = Line(1,2, 3, 4)
# print(l1.__dict__)
# r1 = Rect(3,5,2, -8, "black solid")
# print(r1.__dict__)
# r1.draw()

# lst = list((1,2,3))
# print(type(lst))
#
# print(len(lst))
#
# lst.append(5)
# print(lst)
# for i in lst:
#     print(i)

# class Person:
#     def person_info(self, name, age):
#         print("Inside Person class")
#         print("Name:", name, "Age:", age)
#
# class Company:
#     def company_info(self, c_name, location):
#         print("Inside Company class")
#         print("Name:", c_name, "Location:", location)
#
#     def person_info(self, name, age):
#         print("Inside Company class")
#         print("Name:", name, "Age:", age)
#
# class Employee(Company, Person):
#     def employee_info(self, salary, skill):
#         print("Inside Employee class")
#         print("Salary:", salary, "Skill:", skill)
#
# emp = Employee()
# emp.person_info("John", 35)
# emp.company_info("Google", "Palo Alto")
# emp.employee_info(12000, "Machine learning")

# Инкапсуляция - encapsulation - levels of privacy


class Point:
    _color = "black" # protected
    # __size = 2 # private
    # length = __size ** 2

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, z):
        return type(z) in (int, float)

    def get_coord(self):
        return self.__x, self.__y

    def set_coord(self, x, y):
        try:
            if self.__check_value(x) and self.__check_value(y):
                self.__x = x
                self.__y = y
            else:
                raise ValueError("The coordinates should be numbers")
        except ValueError as v:
            print(v)


p1 = Point(10, 20)
p1._color = "white"
# print(p1._color)
# print(Point.__size)
# print(p1.__size)
# print(p1.length)
print(p1.get_coord())
p1.set_coord("-4", 2.2)
print(p1.get_coord())
# z = "80"
# print(type(z) in (int, float)) # if type(z) == int or type(z) == float: print(true) else: print(false)