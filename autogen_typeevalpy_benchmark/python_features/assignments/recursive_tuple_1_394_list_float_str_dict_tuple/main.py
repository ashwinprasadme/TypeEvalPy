# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [1, 42, 44]


def func2():
    return 48.57


def func3():
    return 'nqltr'


def func4():
    return {'hhnqk': 38, 'qsdzr': 83, 'ykxus': 53}


def func5():
    return (20, 96, 1)


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
