# Function which has a combined return type [int,str]
# The given code is context sensitive because it produces different results based on the context in which it is executed.
def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World!"
    return x


a = False
result = my_function(a)
a = "Hello"
result = my_function(a)
