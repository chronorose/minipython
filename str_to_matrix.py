def str_to_matrix(string):
    first_split = string.split('|')
    matrix = []
    for i in range(len(first_split)):
        to_append = first_split[i].split()
        for i in range(len(to_append)):
            to_append[i] = float(to_append[i])
        matrix.append(to_append)
    return matrix


a = "1 2.34 3 | 4 5 6 | 7 8 9 "
b = str_to_matrix(a)
print(b)
print(b[0][1])
