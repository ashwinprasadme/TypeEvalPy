# Functions are assigned to variables via starred assignment
def func1():
    return 78


def func2():
    return [91, 94, 37]


def func3():
    return 13.26


def func4():
    return 'vgvpl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
