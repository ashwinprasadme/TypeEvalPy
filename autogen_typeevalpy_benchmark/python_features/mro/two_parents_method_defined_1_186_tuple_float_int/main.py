# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (72, 64, 65)


class B:
    def func(self):
        return 63.78


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 38


c = C()
d = c.func()
