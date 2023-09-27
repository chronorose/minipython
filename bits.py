def isPow2Neg(n):
    if n >= 0:
        return False
    while n != -1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


def setBitsCount(n):
    count = 0
    if n == -1 or isPow2Neg(n):
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
