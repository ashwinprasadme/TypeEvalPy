# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [7, 28, 79]


def func2():
    return (57, 66, 39)


def func3():
    return 44.0


def func4():
    return 'mvuhb'


def func5():
    return {'jonbd': 63, 'cojje': 44, 'aktmd': 12}


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
