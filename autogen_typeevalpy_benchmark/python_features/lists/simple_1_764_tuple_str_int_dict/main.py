# Functions are assigned as elements of a list and then called.


def func1():
    return (51, 89, 62)


def func2():
    return 'zfyon'


def func3():
    return 74


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cmzpb': 99, 'nhdtt': 15, 'iekhx': 9}


b = ["Hello"]
b[0] = func4

f = b[0]()
