# A new list is created as a slice of another one containing functions.


def func1():
    return [11, 12, 38]


def func2():
    return 90.6


def func3():
    return 22


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
