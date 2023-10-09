def sum(x, y):
    return x + y


def specialize(func, *args, **kwargs):
    def wrapper(*args1, **kwargs1):
        return func(*args, *args1, **kwargs, **kwargs1)
    return wrapper


plus_one = specialize(sum, 1, 1)
print(plus_one())
