# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [55, 23, 32]


def func2():
    return 'gvdvm'


def func3():
    return 1


def func4():
    return {'cotun': 67, 'baxuo': 6, 'cktce': 70}


def func5():
    return 2.3


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
