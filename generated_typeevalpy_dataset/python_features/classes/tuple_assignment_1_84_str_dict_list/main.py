# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'sdalj'

    def func2(self):
        return {'uljba': 89, 'ofjcy': 81, 'mlpsk': 99}

    def func3(self):
        return [92, 20, 98]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
