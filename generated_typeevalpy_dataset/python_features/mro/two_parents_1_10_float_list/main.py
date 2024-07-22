# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 29.76


class B:
    def __init__(self):
        pass

    def func(self):
        return [6, 89, 77]


class C(A, B):
    pass


c = C()
d = c.func()
