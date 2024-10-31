m, n = 5, 4
matrix = [
    [4, 2, 5, 1, 2],
    [4, 5, 6, 2, 3],
    [0, 2, 3, 8, 1],
    [9, 9, 9, 1, 2]
]

def transpose(matrix, n, m):
    transposed = [[None for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed

transposed = transpose(matrix, n, m)

for i in range(0, len(transposed)):
    transposed[i].sort()

matrix = transpose(transposed, m, n)

for line in matrix:
    print(*line)