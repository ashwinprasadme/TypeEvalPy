# A new list is created as a slice of another one containing functions.


def func1():
    return 'kiqxu'


def func2():
    return [69, 26, 19]


def func3():
    return 19.47


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
