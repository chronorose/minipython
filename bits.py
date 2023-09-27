def setBitsCount(n):
    count = 0
    if n == -1 or (n < 0 and n % 2 == 0):
        return recSetBitsCount(n, count + 1)
    return recSetBitsCount(n, count)


def recSetBitsCount(n, count):
    if n == 0:
        return count
    if n == -1:
        return count + 1
    else:
        return recSetBitsCount(n >> 1, count + (n & 1))


n = int(input())

print(setBitsCount(n))
