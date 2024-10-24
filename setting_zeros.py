n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]

matrix_copy = matrix.copy()

def set_row_to_zeros(matrix, i):
    matrix[i] = [0 for _ in range(len(matrix[0]))]
    return matrix

def set_col_to_zeros(matrix, j):
    for i in range(0, len(matrix)):
        matrix[i][j] = 0
    return matrix

for i in range(n):
    for j in range(m):
        if matrix[n][m] == 0:
            matrix_copy = set_row_to_zeros(matrix, i)
            matrix_copy = set_col_to_zeros(matrix_copy, j)

for line in matrix_copy:
    print(*line)