import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
# 713 seconds for numpy
# 251 seconds for default python


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
        for i in range(size):
            for j in range(size):
                sum = checkNeighbours(matrix, i, j)
                if sum == 3 or (matrix[i][j] == 1 and sum == 2):
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
        plt.imshow(matrix)


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

matrix[100][100] = 1
matrix[100][101] = 1
matrix[100][102] = 1
matrix[101][102] = 1
matrix[102][101] = 1
n_matrix = []
for i in range(size):
    n_row = [0 for i in range(size)]
    n_matrix.append(n_row)
n_matrix[100][100] = 1
n_matrix[100][101] = 1
n_matrix[100][102] = 1
n_matrix[101][102] = 1
n_matrix[102][101] = 1
n_matrix = np.array(n_matrix)


gameOfLife(n_matrix)
gameOfLife(matrix)

plt.axis('off')
fig = plt.figure()
anime = animation.FuncAnimation(fig, gameOfLife,
                                interval=50, save_count=50)
plt.show()
anime()

endgame_sum_python = 0
endgame_sum_numpy = 0
for i in range(size):
    for j in range(size):
        endgame_sum_python += matrix[i][j]
        endgame_sum_numpy += n_matrix[i][j]

print(endgame_sum_python == endgame_sum_numpy)
