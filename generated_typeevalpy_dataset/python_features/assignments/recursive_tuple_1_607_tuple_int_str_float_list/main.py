# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (3, 97, 90)


def func2():
    return 100


def func3():
    return 'taqzv'


def func4():
    return 94.18


def func5():
    return [22, 61, 69]


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
