# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jwwrm'


def func2():
    return (36, 56, 7)


def func3():
    return 33


def func4():
    return [1, 56, 60]


def func5():
    return 16.7


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
