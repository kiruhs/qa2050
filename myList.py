lst = [3, 4, 1, -5]
# build the class that will be child of list class, but always sorted and presented in << brackets >> without semicolon
# should contain numbers only
# << -5 2 3 4 >>

class MyList(list):
    """================================
This class is a mutation of list class, that can get only numeric list, returns sorted list in << brackets >>
without semicolons. Most of list's methods and attributes remind the same, part of it will be changed
================================    """
    
    def __init__(self, it):
        for i in it:
            if not isinstance(i, (int, float, bool)):
                raise NotImplementedError
        super().__init__(sorted(it))
        self.index = 0

    def __str__(self):
        return f'<< {" ".join(map(str, self))} >>'

    def append(self, __object):
        if not isinstance(__object, (int, float, bool)):
            raise NotImplementedError
        super().append(__object)
        self.sort()

    def __getitem__(self, item):
        if isinstance(item, slice):
            return MyList(super().__getitem__(item))
        return super().__getitem__(item)

    def __len__(self):
        cnt = 0
        for i in self:
            if i > 0:
                cnt +=1
        return cnt

    # def __add__(self, other):
    #     if isinstance(other, list):
    #         return MyList(super().__add__(other))

    def __radd__(self, other):
        if isinstance(other, list):
            # return MyList(super().__add__(other))
            ls = [i for i in other]
            for i in self:
                ls.append(i)
            return MyList(ls)

    @property
    def length(self):
        return super().__len__()

    def __sub__(self, other):
        if not isinstance(other, int) or other < 0:
            raise TypeError

        if other > self.length:
            print("The number is greater than list length")
            return None
        for _ in range(other):
            self.pop()

        return self

    def __gt__(self, other):
        if self.length > MyList(other).length:
            return True
        return False

    def __lt__(self, other):
        if self.length < MyList(other).length:
            return True
        return False

    def __le__(self, other):
        if self.length <= MyList(other).length:
            return True
        return False

    def __eq__(self, other):
        if super().__eq__(other):
            return True
        return False

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        value = self[self.index]
        self.index += 1
        return value

l = MyList(lst)
l.append(-100)
# print(l)
# print(l[1:3])
print(len(l))
print(l)
lst1 = [-100, -5, 1, 3, 4]
# lst1.sort()
# print(lst1)
lst2 = MyList([-9, 5, 0])
# print(lst1 + lst2)

# class My_int(int):
#     def __len__(self):
#         return self
#
# x = My_int(4)
# print(len(x))
# print(l - 5)

# print(l <= lst1)
# print(l != lst1)
# print(next(lst2))
# print(next(lst2))
# print(next(lst2))
# print(next(lst2))