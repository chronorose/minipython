def setBitsCount(n):
    return recSetBitsCount(n, 0, True)


def checkNeg(n, flag):
    if n != -1 and n % 2 != 0:
        return False
    return flag


def recSetBitsCount(n, count, flag):
    flag = checkNeg(n, flag)
    if n == 0:
        return count
    if n == -1:
        return count + 1 + int(flag)
    return recSetBitsCount(n >> 1, count + (n & 1), flag)


n = int(input())

print(setBitsCount(n))
