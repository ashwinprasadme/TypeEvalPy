# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'koqnh'

    def func2(self):
        return {'wxslm': 53, 'dehre': 61, 'qmytg': 21}

    def func3(self):
        return (58, 32, 32)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
