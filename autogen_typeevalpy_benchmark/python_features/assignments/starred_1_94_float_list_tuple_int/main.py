# Functions are assigned to variables via starred assignment
def func1():
    return 35.01


def func2():
    return [58, 35, 27]


def func3():
    return (44, 3, 74)


def func4():
    return 45

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
