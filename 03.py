# zip
# from itertools import zip_longest
# a = [1, 2, 4]
# zipped = zip(a, a)
# print(list(zipped))
# print(list(zip_longest(range(37), range(30), fillvalue=0)))
from matplotlib.pyplot import xlabel


# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# print(*zip(*pairs))
# numbers, letters = zip(*pairs)
# print(numbers)
# print(letters)


# x, y = 5, 10
# print(x)
# print(y)

# z = x
# x = y
# y = z
# x, y = y, x # swap to variable in python only
# the following algorithm for swap two variables without third one for numbers only

# x = x + y # x becomes a sum of two variables
# y = x - y # y becomes a source x value
# x = x - y # x becomes a source y value
#
# print("---------")
# print(x)
# print(y)

# total_sales = [52000, 51000, 48000]
# prod_cost = [46800, 45900, 43200]
#
# for sales, costs in zip(total_sales, prod_cost):
#     profit = sales - costs
#     print(f"Total profit: {profit}")

# number = "1234569"
#
# def is_digits_ascending(number):
#     num_str = str(number)
#
#     # go over each symbol and compare to the previous one
#     for i in range(0, len(num_str)-1):
#         if num_str[i] >= num_str[i + 1]:
#             return False
#     return True
#
#
# print(is_digits_ascending(number))

# z = 100

# def max2(x, y):
#     # global z
#     # z += 5
#     # x += 2
#     if x > y:
#         return x
#     return y

# print(max2(4, 7))
# print(z)

# def max3(x, y, z):
#     return max2(max2(x, y), z)

# print(max3(85, -100, 45))

# def my_country(country="Israel", x=0):
#     print(f" I'm from {country}, live there {x} years")
# cntr = "USA"
# years = 3
# my_country()

# def call_child(*args, **kwargs):
#     return *args, *kwargs
#
#
# print("My child's names are", *call_child("Mary", "Lisa", "John"))
# print(f"My child's names are {call_child("Jane", "Michael")}")
#
# def personal_info(*args, **kwargs):
#     return *args, *kwargs, *kwargs.values()
#
# y = personal_info("John", "Jack", "mary", surname="Connor", age= 17)
# print(*y, end="\n" "hello world!")

# factorial 6! = 1*2*3*4*5*6 = 720    n! = (n-1)! * n

# num = 50
# general function
# def fact(n):
#     fct = 1
#     for i in range(1, n+1):
#         fct *= i
#     return fct
#
# print(fact(num))

# recursive function

# def fact_rec(n):
#     if n == 1:
#         return 1
#     return fact_rec(n - 1) * n
# print(fact_rec(num))

# fibonacci 1, 1, 2, 3, 5, 8, 13, 21, 34

num = 10
#
# lst = [1, 1]
# def fibo(x):
#     for i in range(2, x):
#         lst.append(lst[i-2] + lst[i-1])
#
#     return lst[x-1]
#
# print(fibo(num))
# #
# def fibo_rec(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo_rec(x-1) + fibo_rec(x-2)
#
# print(fibo_rec(num))

# def fibo_memo_rec(n, memo = {}):
#     if n in memo:
#         return memo[n]
#
#     if n < 2:
#         return n
#
#     memo[n] = fibo_memo_rec(n-1, memo) + fibo_memo_rec(n-2, memo)
#     return memo[n]
#
# print(fibo_memo_rec(num))


st = "Hello group qa2050, we are learning the Python, one of the powerful programming languages"

dct = {}
for i in st.lower():
    if not i.isalpha():
        continue
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

print(dct)