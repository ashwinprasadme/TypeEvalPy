# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 70, 82]


def func2():
    return 'ciuna'


def func3():
    return 6.1


def func4():
    return 16


def func5():
    return (39, 65, 69)


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
