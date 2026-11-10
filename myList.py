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

    def __str__(self):
        return f'<< {" ".join(map(str, self))} >>'

    def append(self, __object):
        if not isinstance(__object, (int, float, bool)):
            raise NotImplementedError
        super().append(__object)
        self.sort()


l = MyList(lst)
l.append(2)
print(l)

lst = [6, 0, -5]
print(lst.sort())
print(lst)