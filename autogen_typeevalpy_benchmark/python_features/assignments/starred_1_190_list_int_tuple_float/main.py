# Functions are assigned to variables via starred assignment
def func1():
    return [34, 39, 25]


def func2():
    return 82


def func3():
    return (40, 26, 81)


def func4():
    return 88.45

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
