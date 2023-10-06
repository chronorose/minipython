a = {(1, 2): "a", (3, 4): "a", (5, 6): "a", 5: "a", 4: "a",
     6: "b", 9: "b", 10: "c"}


def dict_swap_2(dict):
    new_dict = {}
    for key, val in dict.items():
        try:
            new_dict[val].append(key)
        except KeyError:
            new_dict[val] = [key]
    for key, val in new_dict.items():
        if len(new_dict[key]) == 1:
            new_dict[key] = val[0]
            continue
        new_dict[key] = tuple(new_dict[key])
    return new_dict


# def dict_swap(dict):
#     new_dict = {}
#     for i in dict.values():
#         if i in new_dict:
#             continue
#         list = []
#         for j in dict.keys():
#             if dict[j] == i:
#                 list.append(j)
#         if len(list) == 1:
#             new_dict[i] = list[0]
#         else:
#             new_entry = ()
#             for j in list:
#                 new_entry = new_entry + (j, )
#             new_dict[i] = new_entry
#     return new_dict


print(dict_swap_2(a))
