# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xzerl': 69, 'mgtld': 41, 'oitlb': 67}


def func2():
    return [15, 33, 54]


def func3():
    return (88, 37, 71)


def func4():
    return 34.02


def func5():
    return 'kqrdw'


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
