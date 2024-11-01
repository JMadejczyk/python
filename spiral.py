n = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
visited_matrix = [[False for _ in range(n)] for _ in range(n)]
answer = []
i, j = 0, 0
answer.append(matrix[i][j])
visited_matrix[i][j] = True
while 0 in sum(visited_matrix, []):
    while j + 1 < n and not visited_matrix[i][j + 1]:
        j = j + 1
        answer.append(matrix[i][j])
        visited_matrix[i][j] = True
    while i + 1 < n and not visited_matrix[i + 1][j]:
        i = i + 1
        answer.append(matrix[i][j])
        visited_matrix[i][j] = True
    while j - 1 >= 0 and not visited_matrix[i][j - 1]:
        j = j - 1
        answer.append(matrix[i][j])
        visited_matrix[i][j] = True
    while i - 1 >= 0 and not visited_matrix[i - 1][j]:
        i = i - 1
        answer.append(matrix[i][j])
        visited_matrix[i][j] = True
print(*answer)
