# Functions are assigned as elements of a list and then called.


def func1():
    return {'ribph': 3, 'oqpsh': 47, 'xgpid': 57}


def func2():
    return [47, 55, 79]


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ftdnv'


b = ["Hello"]
b[0] = func4

f = b[0]()
