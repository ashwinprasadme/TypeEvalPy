# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (75, 7, 41)


def func2():
    return 72.55


def func3():
    return [16, 74, 95]


def func4():
    return {'cqnok': 78, 'zywkf': 64, 'ixofi': 34}


def func5():
    return 81


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
