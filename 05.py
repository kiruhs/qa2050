# lst=[10, 20, 30, 40, 50, 30, 30, 20, 40, 45, 70, 80, 93, 99]
# lst = [3, 8, 4, 5, 12,7, 1]

# def longest_subsequence(l):
#     if not isinstance(l, list):
#         return None
#     if not l:
#         return 0
#     n = len(l)
#     arr = [1] * n
#     for i in range(1, n):
#         for j in range(i):
#             if l[i] > l[j]:
#                 arr[i] = max(arr[i], arr[j]+1)
#     return max(arr)
#
# print(longest_subsequence(lst))


# def sequence(l):
#     if not isinstance(l,list):
#         return None
#     if not l:
#         return 0
#     dct={1:l[0]}
#     for i in range(1,len(l)):
#         for key, value in reversed(list(dct.items())): # (3, 40), (4, 45)
#
#             if l[i]>value:
#                 dct[key+1]=l[i]
#                 break
#             if (key==1)and(l[i]<value): dct[key]=l[i]
#             print(key, value)
#     return list(dct.keys())[-1]
#
# print(f"Length of the longest increasing sub-sequence in the said list{lst}: {sequence(lst)}")


lst=[10, 20, 30, 40, 50, 30, 30, 20, 40, 45, 70, 3, 80, 93, 96, 99]
# lst = [3, 8, 4, 5, 12,7, 1]

# def len_long_contin_increas_subseq(l):
#     if not l:
#         return 0
#     max_len = 1
#     cur_len = 1
#
#     for i in range(1, len(l)):
#         if l[i] > l[i-1]:
#             cur_len += 1
#             if cur_len > max_len:
#                 max_len = cur_len
#         else:
#             cur_len = 1
#     return max_len
# print(len_long_contin_increas_subseq(lst))
# while True:
#     try:
#         x = int(input("Enter some natural number: "))
#         res = x**2
#         print(x)
#         break
#     except ValueError as error:
#         print(error)

# print("this block should work anyway")
# y = 5
# z = 8
# def max2(n1, n2):
#     if n1 > n2:
#         return n1
#     return n2
# print(y, z)

# def division(x, y):
#     if y != 0:
#         res = x/y
#         print(res)
#     else:
#         print("Division by zero")
# #
#
# num1 = 5
# num2 = 2
# division(num1, num2)
# #
# print("Continue")

# if "test02.txt":
#     print("The is no such file")

# try:
#     with open("test02.txt") as f:
#         x = f.read()
#         print(x)
# except FileNotFoundError as f:
#     print(f)

try:
    try:
        x = int(input("Enter the temperature value between 20 and 50 degrees: "))

    except (ValueError, NameError) as er:
        print(er)
    else:
        if x < 20 or x > 50:
            raise ValueError ("entered the wrong temperature value")
        print("Good guy! You entered the valid temperature")
except ValueError as e:
    print(e)

print(x)