# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 67


def func2():
    return 'wzkfh'


def func3():
    return [52, 97, 68]


def func4():
    return {'vxtzw': 61, 'ldkfm': 63, 'dmbrv': 80}


def func5():
    return 94.66


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
