# A class called Len is defined that has a member variable 'text' and a nested class called 'Nested'.
# The 'Nested' class also has a member variable 'value'.
# The 'Len' class is field-sensitive, allowing 'text' and 'Nested.value' to store different types of values in different contexts.
# The class has a method called 'compute_length' which returns the length of the 'text' member variable or 'Nested.value'.


class Len:
    def __init__(self, text):
        self.text = text
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    def compute_length(self):
        if isinstance(self.text, str):
            return len(self.text)
        elif isinstance(self.nested.value, str):
            return len(self.nested.value)
        else:
            return None


context1 = Len("Hello")
context2 = Len(12345)
context2.nested.value = "World"
result1 = context1.compute_length()
result2 = context2.compute_length()
