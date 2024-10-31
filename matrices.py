n = 3
matrix1 = [
    ['a', 'b', 'cd'],
    ['e', 'f', 'gh'],
    ['i', 'j', 'kl']
]
matrix2 = [
    ['e', 'gh'],
    ['i', 'kl']
]

def remove_row(matrix, row_id):
    new_matrix = []
    for index, row in enumerate(matrix):
        if index != row_id:
            new_matrix.append(row)
    return new_matrix

def remove_col(matrix, col):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            if j != col:
                row.append(matrix[i][j])
        new_matrix.append(row)
    return new_matrix

possible_matrices = []

for i in range(n):
    for j in range(n):
        matrix = remove_row(matrix1, i)
        matrix = remove_col(matrix, j)
        possible_matrices.append(matrix)

for line in matrix2:
        print(*line)
print()

for possible in possible_matrices:
    for line in possible:
        print(*line)
    print()


def check():
    for matrix in possible_matrices:
        if matrix == matrix2:
            return True
    return False


print(check())
