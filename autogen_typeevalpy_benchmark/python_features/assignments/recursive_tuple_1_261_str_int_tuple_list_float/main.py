# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ksffe'


def func2():
    return 25


def func3():
    return (94, 85, 80)


def func4():
    return [47, 60, 71]


def func5():
    return 86.38


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
