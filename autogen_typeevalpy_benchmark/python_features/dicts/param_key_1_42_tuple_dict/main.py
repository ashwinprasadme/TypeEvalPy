# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return (56, 11, 82)


def func3():
    return {'ukrhb': 88, 'asfei': 98, 'jzsoc': 97}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
