# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jgbue'


def func2():
    return [53, 15, 72]


def func3():
    return 4.94


def func4():
    return (26, 19, 39)


def func5():
    return 18


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
