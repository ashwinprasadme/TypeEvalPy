# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.99


def func2():
    return (96, 49, 75)


def func3():
    return {'yidtp': 19, 'mqqvo': 73, 'eytuo': 27}


def func4():
    return 72


def func5():
    return 'rtzyw'


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
