# A simple inheritance scheme.


class A:
    def func(self):
        return [94, 84, 79]


class B(A):
    pass


b = B()
c = b.func()
