# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tsbad'


def func2():
    return 33


def func3():
    return {'xjfqk': 68, 'dhbef': 37, 'rlwbg': 72}


def func4():
    return (21, 19, 71)


def func5():
    return 96.45


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
