# Two variables are assigned a value via a tuple assignment.
def func1():
    return (29, 1, 99)


def func2():
    return [59, 12, 94]


def func3():
    return 73


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
