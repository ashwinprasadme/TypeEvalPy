# Functions are assigned as elements of a list and then called.


def func1():
    return 'ddiks'


def func2():
    return {'ujcvz': 39, 'unbic': 65, 'veqht': 64}


def func3():
    return 6


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [95, 7, 73]


b = ["Hello"]
b[0] = func4

f = b[0]()
