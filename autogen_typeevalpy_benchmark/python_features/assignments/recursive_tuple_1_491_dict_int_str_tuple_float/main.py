# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fpqji': 4, 'anspi': 100, 'gdepj': 45}


def func2():
    return 63


def func3():
    return 'uhhqu'


def func4():
    return (37, 62, 1)


def func5():
    return 71.39


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
