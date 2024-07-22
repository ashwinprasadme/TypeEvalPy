# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [65, 88, 88]


def func2():
    return 24


def func3():
    return {'ulfje': 3, 'nhbqe': 79, 'cbxbh': 71}


def func4():
    return 'wyixz'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
