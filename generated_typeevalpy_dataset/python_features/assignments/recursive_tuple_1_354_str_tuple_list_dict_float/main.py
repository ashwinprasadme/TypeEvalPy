# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jewsq'


def func2():
    return (40, 84, 27)


def func3():
    return [36, 60, 57]


def func4():
    return {'jbvhc': 4, 'zjson': 82, 'ewrom': 90}


def func5():
    return 39.52


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
