# Functions are assigned to variables via starred assignment
def func1():
    return [15, 87, 86]


def func2():
    return 'yheff'


def func3():
    return {'kanss': 83, 'anbkl': 33, 'wtpzj': 45}


def func4():
    return 97.72

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
