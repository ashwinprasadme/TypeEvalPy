# Functions are assigned as elements of a list and then called.


def func1():
    return 'yijsm'


def func2():
    return False


def func3():
    return {'ywvbt': 32, 'xogmy': 62, 'jcusq': 94}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 88.96


b = ["Hello"]
b[0] = func4

f = b[0]()
