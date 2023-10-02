def into_tuple(el1, el2):
    return (el1, el2)


def zippy(lst1, lst2):
    ln = min(len(lst1), len(lst2))
    new_lst = []
    for i in range(ln):
        new_lst.append(into_tuple(lst1[i], lst2[i]))
    return new_lst


a = [1, 2, 3]
b = ["a", "b"]

print(zippy(a, b))
