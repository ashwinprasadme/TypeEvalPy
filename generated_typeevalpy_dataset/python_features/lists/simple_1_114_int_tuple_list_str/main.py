# Functions are assigned as elements of a list and then called.


def func1():
    return 45


def func2():
    return (6, 67, 21)


def func3():
    return [58, 11, 20]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'tlpgt'


b = ["Hello"]
b[0] = func4

f = b[0]()
