a = [1, 2, 3, [1, 2], [3, [3, 4]]]


def flattening(elem, new_list):
    """
    recursively calls itself to append only not-lists to the new list
    """
    if isinstance(elem, list):
        for i in elem:
            i = flattening(i, new_list)
    else:
        new_list.append(elem)


def flatten(list):
    new_list = []
    for i in list:
        i = flattening(i, new_list)
    return new_list


print(flatten(a))
