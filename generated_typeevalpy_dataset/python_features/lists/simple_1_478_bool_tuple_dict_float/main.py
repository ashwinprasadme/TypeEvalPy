# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return (54, 95, 85)


def func3():
    return {'unxad': 6, 'todtg': 87, 'nbgrm': 67}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77.16


b = ["Hello"]
b[0] = func4

f = b[0]()
