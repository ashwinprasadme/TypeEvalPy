# Functions are assigned to variables via starred assignment
def func1():
    return 42


def func2():
    return {'urgxs': 18, 'yprvq': 6, 'yojkb': 47}


def func3():
    return (59, 74, 31)


def func4():
    return 85.12

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
