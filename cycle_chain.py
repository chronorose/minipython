def take(seq, n):
    res = []
    for i in range(n):
        res.append(next(seq))
    return res


def cycle(iterable):
    while True:
        yield from iterable


def chain(*iterables):
    for i in iterables:
        yield from i


print(take(cycle([1, 2, 3]), 10))
print(list(chain([1, 2, 3], ['a', 'b'], [42, 13, 7])))
