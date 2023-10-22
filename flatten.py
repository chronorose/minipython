a = [1, 2, 3, [1, 2], [3, [3, 4]]]


def flattening(list, depth):
    for i in list:
        if depth != 0:
            try:
                yield from flattening(i, depth - 1)
            except TypeError:
                yield i
        else:
            yield i


def flatten(list_to_flatten, depth=-1):
    """
    function that returns list made out of
    list from input that is flattened with the specified depth
    (or until there are no sub-lists left)
    :param list: list to flatten
    :param depth: depth of flattening, -1 by default,
    flattens until no sub-lists left on any negative depths
    """
    return list(flattening(list_to_flatten, depth))


print((flatten(a)))
print(flatten(a, depth=1))
print(flatten(a, depth=0))
