# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ortev': 48, 'zqetj': 84, 'bexzi': 7}


def func2():
    return 50


def func3():
    return 24.98


def func4():
    return (82, 93, 62)


def func5():
    return [32, 9, 83]


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
