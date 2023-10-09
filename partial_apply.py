import doctest


def sum(x, y):
    """
    >>> sum(1, 2)
    3
    >>> sum(8, 8)
    16
    """
    return x + y


def specialize(func, *args, **kwargs):
    """this is a function that performs partial application pattern
    :param func: function for you to perform partial application on
    :return: function that has new amount of arguments
    """
    def wrapper(*inside_args, **inside_kwargs):
        return func(*args, *inside_args, **kwargs, **inside_kwargs)
    return wrapper


if __name__ == "__main__":
    plus_one = specialize(sum, 1)
    sum_wrapper = specialize(sum)
    six = specialize(sum, 1, 5)
    print(plus_one(10))
    print(sum_wrapper(1, 5))
    print(six())
    doctest.testmod()
