matrix = [[None for _ in range(n)] for _ in range(n)]
transposed_matrix = [[None for _ in range(n)] for _ in range(n)]
def transpose_matrix():
    for i in range(n):
        for j in range(n):
            transposed_matrix[j][i] = matrix[i][j]