# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 77


def func2():
    return (21, 70, 56)


def func3():
    return [49, 37, 85]


def func4():
    return 'rlhqy'


def func5():
    return 85.84


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
