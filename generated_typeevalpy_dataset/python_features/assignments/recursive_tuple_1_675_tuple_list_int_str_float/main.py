# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (81, 36, 55)


def func2():
    return [53, 62, 85]


def func3():
    return 29


def func4():
    return 'kebnp'


def func5():
    return 99.93


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
