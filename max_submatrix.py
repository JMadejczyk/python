big_n, n = 5, 2
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

def get_row(matrix, x):
    return matrix[x]

def get_col(matrix, x):
    return [matrix[i][x] for i in range(len(matrix))]

def sum_of_cross_products(matrix):
    n = len(matrix)
    summ = 0
    for i in range(n):
        row = get_row(matrix, i)
        for j in range(n):
            col = get_col(matrix, j)
            summ += sum(row[k] * col[k] for k in range(len(col)))
    return summ

def select_n_submatrix(matrix, i_, j_, n):
    return [row[j_:j_ + n] for row in matrix[i_:i_ + n]]

largest = 0
for i in range(big_n - n + 1):
    for j in range(big_n - n + 1):
        submatrix = select_n_submatrix(matrix, i, j, n)
        summ = sum_of_cross_products(submatrix)
        if summ > largest:
            largest = summ

print(largest)
