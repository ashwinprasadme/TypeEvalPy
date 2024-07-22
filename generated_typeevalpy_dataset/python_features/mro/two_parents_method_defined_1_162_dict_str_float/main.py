# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'efscj': 19, 'gnvee': 81, 'lsmqv': 97}


class B:
    def func(self):
        return 'rvunf'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 80.04


c = C()
d = c.func()
