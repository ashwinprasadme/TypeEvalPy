# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72


def func2():
    return (2, 20, 14)


def func3():
    return 'hekbk'


def func4():
    return [60, 86, 12]


def func5():
    return 35.54


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
