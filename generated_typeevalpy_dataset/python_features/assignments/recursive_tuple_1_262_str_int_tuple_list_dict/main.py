# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jhcjj'


def func2():
    return 84


def func3():
    return (84, 54, 41)


def func4():
    return [79, 100, 35]


def func5():
    return {'anxhm': 25, 'yqeol': 18, 'rrdym': 27}


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
