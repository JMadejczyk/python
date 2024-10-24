# m, n = 2, 3
# k = 1
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# operations = [["RR", "0"]]

# m - number of rows
# n - number of columns

m, n = [int(x) for x in input().split()]
matrix = []
for _ in range(m):
    matrix.append([int(x) for x in input().split()])

k = int(input())

operations = []
for _ in range(k):
    operations.append(input().split())



def reverse_row(matrix, change_row):
    matrix[change_row].reverse()
    return matrix

def reverse_column(matrix, change_col):
    m = len(matrix)

    col = []
    for i in range(m):
        col.append(matrix[i][change_col])
    col.reverse()

    for i in range(m):
        matrix[i][change_col] = col[i]

    return matrix

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])

    new_matrix = []
    for i in range(n):
        col = []
        for j in range(m):
            col.append(matrix[j][i])
        new_matrix.append(col)

    return new_matrix


# print(reverse_row(matrix, 1))
# print(reverse_column(matrix, 1))
# transpose(matrix)

for operation_ in operations: 
    operation = operation_[0]
    if len(operation_) > 1:
        operation_number = int(operation_[1])
    if operation == "RR":
        matrix = reverse_row(matrix, operation_number)
    if  operation == "RC":
        matrix = reverse_column(matrix, operation_number)
    elif operation == "T":
        matrix = transpose(matrix)

for row in matrix:
    print(*row)