def sum(x, y):
    return x + y


def specialize(func, *args, **kwargs):
    def wrapper(*args1, **kwargs1):
        return func(*args, *args1, **kwargs, **kwargs1)
    return wrapper


plus_one = specialize(sum, 1)
sum_wrapper = specialize(sum)
six = specialize(sum, 1, 5)
print(plus_one(10))
print(sum_wrapper(1, 5))
print(six())
