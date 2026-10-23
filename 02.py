# map
# x = "hello"
# for i in x:
#     print(i)
# y = [3, 5, True, 45.07, "Hello", (1, 5, -4.3), [4, 8]]
# for j in y:
#     print(j)
# print(dir(y))
import math

# it = iter(y)
# print(it)
# print(dir(it))
# for j in y:
#     print(j)
# print(5 in it)
# print("========")
# print("hello" in it)
# for j in it:
#      print(j)

# map(function, iterable)

# num = [1, 2, 3, 4, 5]
# s_num = []
# for i in num:
#     s_num.append(i**2)
# print(s_num)
# def square(x):
#     return x**2
# squared_nums = list(map(square, num))

# squared_nums = list(map(lambda i: i**2, num))
# print(squared_nums)


# s = "1234567890"
# # print(s[6])
# symbols = list(s)
# print(symbols)
#
# int_symbols = list(map(int, symbols))
# print(int_symbols)
# x = '1'
# print(type(x))
# print(type(int(x)))


# string2 = "Hello world the languages of programming are different"
# length = max(map(len, string2.split()))
# print(length)
# new_list = string2.split()
# for l in new_list:
#     if len(l) == length:
#         print(l)
# print(max(string2.split(), key=len))


# lst = []
# for i in range(1,101):
#     lst.append(i**2)
# print(lst)

# print([i**2 for i in range(1, 101)])
# # print(lst2)
# import math
# ls1 = [f"{math.sqrt(i):.2f}" for i in range(1, 100001)]
# print(ls1[10])
#
# ls2 = map(lambda i: f"{math.sqrt(i):.2f}", range(1, 100001))
# # print(list(ls2))
# for i in range(10):
#     next(ls2)
# print(next(ls2))
# print(ls1.__sizeof__())
# print(ls2.__sizeof__())

# num1 = [1, 2, 3, 5]
# num2 = (10,20,40)
#
# summa = list(map(lambda n1, n2: n1 + n2, num1, num2))
# print(summa)

# dictionary
car = {'brand': 'Ford',
       'model': 'Mustang',
       'year': 1968,
       5: True,
       'year': 2000
       }

# print(len(car))
# print(car['year'])
# print(car.get('model'))
# print(car.get(5))

car['year'] = 2010

car['color'] = ('blue', 'red', 'yellow')
# print(car)

# print(car.keys())
# print(car.values())

# for v in car.values():
#     print(v)

# for i in car.items():
#     print(i)

# for k, v in car.items():
#     print(f"The key is {k}, The value is {v}")


# car = {'a': 'Mercedes-Benz', 'b': 'BMW', 'c': 'Ferrari', 'd': 'Lamborghini'}
# # name_2026
# car = dict(map(lambda x: (x[0], x[1]+'_2026'), car.items()))
# print(car)
#
# x = '1000'
# y = 'world'
# print(x + y)

# function filter

string1 = ('''This is the text for testing the function that used for finding all words 
that are compatible for filter function for lesson purposes''')
# print(string1)

# res = [x for x in string1.split() if x.lower().startswith('t')]
# print(res)

# fil = filter(lambda x: x.lower().startswith('t'), string1.split())
# print(next(fil))
# print(next(fil))
# print(next(fil))

# print(list(filter(lambda x: x%3 == 0, [i for i in range(1, 21)])))

# lst = [4, 7, -3, 5, 9, -16]
# print(list(map(math.sqrt, filter(lambda x: x >= 0, lst))))


# zip
from itertools import zip_longest

a = ("John", "Charles", "Mike", "Jakob", "Bill")
b = ("Jenny", "Christy", "Monika")

x = zip_longest(a, b, fillvalue='alone')
print(tuple(x))