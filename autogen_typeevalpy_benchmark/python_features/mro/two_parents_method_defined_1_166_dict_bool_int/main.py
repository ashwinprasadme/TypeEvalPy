# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'jypfu': 3, 'icyos': 67, 'evwpu': 95}


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 95


c = C()
d = c.func()
