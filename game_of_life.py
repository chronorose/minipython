import numpy as np
import time

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
    for iteration in range(128):
        print(iteration)
        for i in range(size):
            for j in range(size):
                sum = checkNeighbours(matrix, i, j)
                if sum == 3 or (matrix[i][j] == 1 and sum == 2):
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0


def checkNeighbours(matrix, i, j):
    sum = checkCell(matrix, i + 1, j)
    sum += checkCell(matrix, i - 1, j)
    sum += checkCell(matrix, i, j + 1)
    sum += checkCell(matrix, i, j - 1)
    sum += checkCell(matrix, i + 1, j + 1)
    sum += checkCell(matrix, i - 1, j + 1)
    sum += checkCell(matrix, i + 1, j - 1)
    sum += checkCell(matrix, i - 1, j - 1)


def checkCell(matrix, i, j):
    return matrix[i % 1024][j % 1024]


matrix = []
size = 1024
for i in range(size):
    row = [0 for i in range(size)]
    matrix.append(row)

n_matrix = []
for i in range(size):
    n_row = [0 for i in range(size)]
    n_matrix.append(n_row)
n_matrix = np.array(n_matrix)
gameOfLife(n_matrix)
gameOfLife(matrix)
endgame_sum = 0
for i in range(size):
    for j in range(size):
        endgame_sum += matrix[i][j]

print(endgame_sum)
