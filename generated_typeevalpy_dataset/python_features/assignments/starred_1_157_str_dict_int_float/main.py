# Functions are assigned to variables via starred assignment
def func1():
    return 'alnfa'


def func2():
    return {'ocepq': 65, 'vuyou': 92, 'nupci': 62}


def func3():
    return 80


def func4():
    return 45.0

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
