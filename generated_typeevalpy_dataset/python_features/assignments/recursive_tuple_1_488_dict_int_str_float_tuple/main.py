# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ynsmj': 23, 'bipys': 53, 'jsbvd': 7}


def func2():
    return 49


def func3():
    return 'gynlr'


def func4():
    return 75.99


def func5():
    return (71, 75, 27)


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
