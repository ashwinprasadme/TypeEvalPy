# Two variables are assigned a value via a tuple assignment.
def func1():
    return 86


def func2():
    return [91, 83, 100]


def func3():
    return 'frvyf'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
