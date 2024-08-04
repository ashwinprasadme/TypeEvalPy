# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'hbsoc'


def func2():
    return [59, 66, 47]


def func3():
    return 6.49


def func4():
    return 73


(a, b), (c, d) = [(func1, func2), (func3, func4)]
