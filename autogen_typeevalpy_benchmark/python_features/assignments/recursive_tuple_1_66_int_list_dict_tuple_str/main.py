# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 94


def func2():
    return [29, 90, 95]


def func3():
    return {'bwemk': 68, 'zrwzo': 94, 'irztk': 37}


def func4():
    return (37, 90, 25)


def func5():
    return 'sociu'


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
