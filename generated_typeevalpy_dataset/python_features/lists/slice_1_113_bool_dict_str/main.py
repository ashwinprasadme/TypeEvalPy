# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return {'cbkfo': 88, 'yxunn': 35, 'emupb': 83}


def func3():
    return 'uabvk'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
