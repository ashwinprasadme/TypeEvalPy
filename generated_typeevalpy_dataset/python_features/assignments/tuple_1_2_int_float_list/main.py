# Two variables are assigned a value via a tuple assignment.
def func1():
    return 1


def func2():
    return 32.84


def func3():
    return [25, 25, 35]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
