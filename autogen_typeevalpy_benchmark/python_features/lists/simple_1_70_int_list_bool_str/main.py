# Functions are assigned as elements of a list and then called.


def func1():
    return 79


def func2():
    return [54, 70, 20]


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'hcdrc'


b = ["Hello"]
b[0] = func4

f = b[0]()
