# Functions are assigned as elements of a list and then called.


def func1():
    return 67


def func2():
    return 'ttkgt'


def func3():
    return [25, 49, 18]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kxkkf': 39, 'yrmbx': 87, 'lekxo': 24}


b = ["Hello"]
b[0] = func4

f = b[0]()
