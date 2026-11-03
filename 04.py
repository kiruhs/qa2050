# dct = {'a': 1, 'b': {'c': {'d': {}}}}
# # dct = [4, 6, 7]
# def dict_depth(d):
#     if not isinstance(d, dict):
#         return 0
#     if not d:
#         return 1
#     return 1 + max(map(dict_depth, d.values()) if d else 0)
#
# print(dict_depth(dct))

# lst = [1, 2, 3, 1, 2, 4, 5, 6, 3, 7, 8]
#
# def first_non_repeatable_el(l):
#     ctr = {}
#     for i in l:
#         if i in ctr:
#             ctr[i] += 1
#         else:
#             ctr[i] = 1
#     for i in l:
#         if ctr[i] == 1:
#             return i
#
# print(first_non_repeatable_el(lst))

# numbers = [2, 5, 3, 1, -4]
# squares = map(lambda x: x**2, numbers)
# print(list(squares))

# interactive vocabulary
# words = {}
# print("This is a dictionary, that you create yourself, just enter a word in English\n"
#       "for exit input 'q' button ")
# while True:
#     s = input()
#     if s == 'q':
#         break
#     if s in words:
#         print("word", s, "is translated as", words[s])
#     else:
#         print("type the translation in Russian", s)
#         words[s] = input()
#     print("Enter another word in English")

# file handling

# f = open("02.py") # r, w, a, r+, w+, a+
# print(f.read())
# f.close()
# continuation

# with open("02.py") as f:
#     # st = f.read() # read until EOF - End Of File
#     for _ in range(3):
#         print(f.readline(), end="")
#
#     print(f.readline(), end="")
#     # print()
#     f.seek(7)
#     print(f.readline(), end="")
#     print(f.tell())
#     print(f.read(5))
#     f.seek(0)
#
#     txt = f.readlines()
#     print(f.tell())
#     print(f.readline())

# print(len(txt))

# with open("test01.txt", 'a') as txt:
#     txt.write("7. Hello\n")
#     txt.write("8. Hello\n")

# with open("new/test01.txt", 'a+') as txt:
#     for i in range(8):
#         txt.write(f"{i+1}. Hello\n")
#     txt.seek(0)
#     print(*txt.readlines()[3:7], sep='')
#     # txt.write("kuku")

# lst = ["This is Delhi\n", "This is Jerusalem\n", "This is London\n"]
#
# with open("new/test2.txt", 'a+') as file:
#     file.writelines(lst)
#     file.seek(0)
#     print(file.read())

from pprint import pprint

# def count_words(st):
#     words = {}
#     for w in st.split():
#         if w in words:
#             words[w] += 1
#         else:
#             words[w] = 1
#     return words
#
# def count_symbols(st):
#     symbols = {}
#     for c in st.lower():
#         if c in symbols:
#             symbols[c] += 1
#         else:
#             symbols[c] = 1
#     return symbols
#
# # with open("new/test2.txt") as file:
# #     txt = file.read()
#
# with open("war.htm") as file:
#     txt = file.read()
#
# # print(count_words(txt))
# print(dict(sorted(count_symbols(txt.lower()).items(), key=lambda item: item[1], reverse=True )))

# from random import randint
#
# lst = [randint(i,100) for i in range(100)]
# print(lst)
# pprint(lst)


# interactive vocabulary advanced
words = {}
with open("vocabulary.txt", 'a+', encoding="utf8") as file:
    file.seek(0)
    lst = file.readlines()
    for i in lst:
        k, v = i[:-1].split(":") # cat:кот
        words.update({k: v})

print("This is a dictionary, that you create yourself, just enter a word in English\n"
      "for exit input 'q' button ")
while True:
    s = input()
    if s == 'q':
        break
    if s in words:
        print("word", s, "is translated as", words[s])
    else:
        with open("vocabulary.txt", 'a+', encoding="utf8") as file:
                words[s] = input("type the translation in Russian: ")
                file.write(f"{s}:{words[s]}\n")

    print("Enter another word in English")

