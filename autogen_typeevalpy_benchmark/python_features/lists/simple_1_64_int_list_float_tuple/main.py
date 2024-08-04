# Functions are assigned as elements of a list and then called.


def func1():
    return 97


def func2():
    return [10, 44, 84]


def func3():
    return 10.54


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (18, 83, 88)


b = ["Hello"]
b[0] = func4

f = b[0]()
