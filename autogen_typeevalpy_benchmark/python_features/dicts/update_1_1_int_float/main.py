# The update method of dictionaries is used.


def func1():
    return 11.56


def func2():
    return 53


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
