h, w, y, x = 3, 4, 2, 3
i_m, j_m, i_p, j_p = h, w, y, x
matrix = [
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
]

def check():
    for i in range(i_m):
        for j in range(j_m):
            if check_if_painting_fits(i, j, i_p, j_p, matrix):
                return True
    return False

def check_if_painting_fits(start_i, start_j, painting_i, painting_j, matrix):
    good = True
    for i in range(painting_i):
        for j in range(painting_j):
            if start_i + i < len(matrix) and start_j + j < len(matrix[0]):
                if matrix[start_i + i][start_j + j] == 1:
                    good = False
            else:
                good = False
    return good

print(check())