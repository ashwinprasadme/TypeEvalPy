# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (47, 37, 53)


def func2():
    return 'ntovb'


def func3():
    return {'qvcza': 22, 'ovger': 96, 'fmmhw': 35}


def func4():
    return 20


def func5():
    return [33, 9, 45]


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
