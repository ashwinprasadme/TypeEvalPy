# A new list is created as a slice of another one containing functions.


def func1():
    return [22, 89, 66]


def func2():
    return 59.35


def func3():
    return {'gfygr': 21, 'tfrtr': 61, 'nyech': 54}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
