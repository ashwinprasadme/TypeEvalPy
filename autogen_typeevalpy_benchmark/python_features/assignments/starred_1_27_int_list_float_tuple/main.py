# Functions are assigned to variables via starred assignment
def func1():
    return 43


def func2():
    return [34, 76, 22]


def func3():
    return 98.86


def func4():
    return (64, 86, 17)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
