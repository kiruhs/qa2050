# int - 3, 90, -43
# float 4.56, 100.1, -0.99
# str "doesn't metter what we write, 56, &$%"
# list [3, 4, 0.7. "342", [3, 0], 't']
# tuple (3, 5, '56')
# tpl = (3, 5, '56')
# print(tpl[2])
#
# print(tpl[2])
# print(tpl[2])
# tpl[2] = 6

# dct = {1: 'a', 2: 'k', 6: True}
# print(dct[6])

# lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# dct = {}

# for k, v in lst:
#     if k not in dct:
#         dct[k] = []
#     dct[k].append(v)

# for k, v in lst:
#     dct.setdefault(k, []).append(v)
#
#
# print(dct)

# def add10(a):
#     a += 10
#     return a
#
# x = 25
# print(add10(x))

# x = lambda a: a + 10
# print(x(25))
# print(x(567))

# def mul(a, b):
#     return a * b
#
# print(mul(5, 6))

# x = lambda a, b: a * b
#
# print(x(5, 6))

# lst = [35, 44, 91, 16, 10]
# print(sorted(lst))
#
# # def rest(x):
# #     return x%10
# print(sorted(lst, key=lambda x: x%10))

# lst = []
# for i in range(5):
#     lst.append(i)

# lst = [i**2 for i in range(500)]
# print(lst)
# tpl = (i**2 for i in range(500))
# t = tuple(tpl)
# print(t[100])
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# print(t.__sizeof__())
# st = {i**2 for i in range(5)}
# print(type(tpl))
# cnt = 0
# for i in tpl:
#     cnt += 1
#     if cnt == 101:
#         print(i)
#         break

import time

BIG_NUM = 999_995**2

lst = [i**2 for i in range(10_000_000)]
st  = {i**2 for i in range(10_000_000)}
print(lst.__sizeof__())
print(st.__sizeof__())
# print(lst)
# print(st)

# start = time.time_ns()
# if BIG_NUM in lst:
#     print("BIGNUM in lst")
# print(f" The time needed for finding the number in the list is {time.time_ns() - start}")
#
# start = time.time_ns()
# # st = set(lst)
# if BIG_NUM in st:
#     print("BIGNUM in st")
# print(f" The time needed for finding the number in the set is {time.time_ns() - start}")




