# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 78

    def func2(self):
        return {'tyise': 25, 'vmbdg': 61, 'uvfdn': 34}

    def func3(self):
        return [54, 3, 21]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
