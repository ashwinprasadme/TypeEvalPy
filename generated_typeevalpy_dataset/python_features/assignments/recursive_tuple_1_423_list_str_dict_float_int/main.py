# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [88, 49, 64]


def func2():
    return 'otizs'


def func3():
    return {'yiqql': 27, 'bpbjk': 20, 'tdpzp': 83}


def func4():
    return 27.18


def func5():
    return 97


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
