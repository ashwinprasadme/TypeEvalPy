# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [11, 33, 51]


def func2():
    return (2, 36, 24)


def func3():
    return 'fnzsw'


def func4():
    return 10


def func5():
    return 13.51


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
