import numpy as np
from random import randint
import matplotlib.pyplot as plt
import time
# 713 seconds for numpy
# 251 seconds for default python
size = 1024
plot = True


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        overall_time = end - start
        print(f"function took {overall_time} seconds to execute")
        return result
    return wrapper


@timer
def gameOfLife(matrix):
    if plot:
        fig, ax = plt.subplots()
        plt.ion()
    for _ in range(128):
        for i in range(size):
            for j in range(size):
                sum = checkNeighbours(matrix, i, j)
                if sum == 3 or (matrix[i][j] == 1 and sum == 2):
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
        if plot:
            ax.clear()
            ax.matshow(matrix)
            plt.pause(1)
    if plot:
        plt.close()


def checkNeighbours(matrix, i, j):
    return sum(matrix[(i + k) % len(matrix)][(j + h) % len(matrix)]
               for k in range(-1, 2) for h in range(-1, 2) if k != 0 or h != 0)


matrix = [[randint(0, 1) for _ in range(size)] for _ in range(size)]
n_matrix = np.random.choice(a=[0, 1], size=(size, size)).tolist()

gameOfLife(n_matrix)
gameOfLife(matrix)


endgame_sum_python = 0
endgame_sum_numpy = 0
for i in range(size):
    for j in range(size):
        endgame_sum_python += matrix[i][j]
        endgame_sum_numpy += n_matrix[i][j]

print(endgame_sum_python == endgame_sum_numpy)
