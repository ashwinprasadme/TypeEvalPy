# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 53.07


def func2():
    return 'aeiqu'


def func3():
    return (88, 4, 75)


def func4():
    return {'liyon': 56, 'tpwld': 29, 'fcmhf': 69}


def func5():
    return 36


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
