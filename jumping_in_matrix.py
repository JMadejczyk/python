# n = int(input())
# i_s, j_s = [int(x) for x in input().split()]
# matrix = []

# for i in range(n):
#     matrix.append([int(x) for x in input().split()])

n = 3
i_s, j_s = 1, 1

matrix = [
    [9, 2, 3],
    [4, 5, 6],
    [3, 8, 1]
]
def find_smallest_in_row(i_s, j_s, matrix):
    min_ = min(matrix[i_s])
    i_s = matrix[i_s].index(min_)
    return j_s, i_s

def find_smallest_in_col(j_s, i_s, matrix):
    min_ = min(matrix[i_s])
    j_s = i_s
    i_s = matrix[i_s].index(min_)
    
    print(j_s)
    return i_s, j_s

transposed_matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        transposed_matrix[j][i] = matrix[i][j]


for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if i == i_s and j == j_s:
            print("'", end="")
            print(f"{matrix[i][j]}", end="")
        else:
            print(f" {matrix[i][j]} ", end="")
        if i == i_s and j == j_s:
            print("'", end="")

    print("")
print("\n")

last_i_s, last_j_s = None, None
while last_i_s != i_s and last_j_s != j_s:
    last_i_s, last_j_s = i_s, j_s
    i_s, j_s = find_smallest_in_row(i_s, j_s, matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i == i_s and j == j_s:
                print("'", end="")
                print(f"{matrix[i][j]}", end="")
            else:
                print(f" {matrix[i][j]} ", end="")
            if i == i_s and j == j_s:
                print("'", end="")

        print("")
    print("\n")
    
    i_s, j_s = find_smallest_in_col(i_s, j_s, matrix=transposed_matrix)
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i == i_s and j == j_s:
                print("'", end="")
                print(f"{matrix[i][j]}", end="")
            else:
                print(f" {matrix[i][j]} ", end="")
            if i == i_s and j == j_s:
                print("'", end="")

        print("")
    print("\n")


print(i_s, j_s)