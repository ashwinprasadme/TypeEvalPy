# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (73, 7, 8)


def func2():
    return 83


def func3():
    return {'efuul': 71, 'gqadp': 36, 'dvtfh': 14}


def func4():
    return 20.5


def func5():
    return [5, 81, 42]


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
