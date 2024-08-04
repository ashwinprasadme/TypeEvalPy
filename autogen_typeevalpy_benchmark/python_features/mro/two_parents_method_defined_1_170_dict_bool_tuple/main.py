# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'xxcmx': 99, 'qbuyx': 95, 'mrpgf': 79}


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (95, 44, 9)


c = C()
d = c.func()
