# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [15, 11, 94]


def func2():
    return 'ydvrk'


def func3():
    return 50


def func4():
    return 63.73


def func5():
    return (46, 40, 35)


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
