# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'brknq'


def func2():
    return 22


def func3():
    return {'siaxr': 61, 'aabko': 74, 'wtaoa': 83}


def func4():
    return (50, 37, 88)


def func5():
    return [79, 50, 58]


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
