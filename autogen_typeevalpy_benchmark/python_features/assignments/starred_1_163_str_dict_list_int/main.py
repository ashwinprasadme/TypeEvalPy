# Functions are assigned to variables via starred assignment
def func1():
    return 'mcpki'


def func2():
    return {'xtpau': 15, 'guaos': 91, 'mahir': 77}


def func3():
    return [58, 88, 7]


def func4():
    return 16

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
