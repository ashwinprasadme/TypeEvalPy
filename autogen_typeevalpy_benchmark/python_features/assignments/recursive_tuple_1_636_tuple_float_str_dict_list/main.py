# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (48, 73, 60)


def func2():
    return 69.92


def func3():
    return 'jwovz'


def func4():
    return {'bqnbw': 37, 'mxyyr': 96, 'ghqyb': 72}


def func5():
    return [78, 37, 89]


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
