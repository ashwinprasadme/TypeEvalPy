# Two variables are assigned a value via a tuple assignment.
def func1():
    return 93


def func2():
    return (66, 36, 59)


def func3():
    return {'pthco': 19, 'dwxyb': 14, 'xlymh': 17}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
