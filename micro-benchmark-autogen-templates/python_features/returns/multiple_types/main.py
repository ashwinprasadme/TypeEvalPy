# Returning multiple types from a function using type hinting.


def func(x):
    if x > 0:
        return x
    else:
        return "Invalid input"


a = func(<value1>)
b = func(-<value1>)
