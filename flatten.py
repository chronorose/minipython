a = [1, 2, 3, [1, 2], [3, [3, 4]]]


def flattening(elem, new_list, depth):
    """
    recursively calls itself to append only not-lists to the new list
    """
    if isinstance(elem, list) and depth != 0:
        for i in elem:
            i = flattening(i, new_list, depth - 1)
    else:
        new_list.append(elem)


def flatten(list, depth=-1):
    new_list = []
    for i in list:
        i = flattening(i, new_list, depth)
    return new_list


print(flatten(a))
print(flatten(a, 1))
