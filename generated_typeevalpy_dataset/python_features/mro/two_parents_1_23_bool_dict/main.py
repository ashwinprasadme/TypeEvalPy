# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return True


class B:
    def __init__(self):
        pass

    def func(self):
        return {'xmqik': 86, 'tnsbv': 40, 'tqrsh': 29}


class C(A, B):
    pass


c = C()
d = c.func()
