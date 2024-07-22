# Functions are assigned as elements of a list and then called.


def func1():
    return 74


def func2():
    return {'tbwzb': 18, 'lbrgk': 45, 'nmnnd': 68}


def func3():
    return 54.26


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (91, 60, 32)


b = ["Hello"]
b[0] = func4

f = b[0]()
