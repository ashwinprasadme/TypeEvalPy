# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'xsvhy': 42, 'egdvz': 22, 'grsjn': 89}

    def func2(self):
        return [87, 73, 53]

    def func3(self):
        return 73


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
