# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 81.86


def func2():
    return [71, 71, 3]


def func3():
    return (48, 53, 37)


def func4():
    return 63


def func5():
    return {'jbiro': 89, 'ensrc': 88, 'laaka': 57}


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
