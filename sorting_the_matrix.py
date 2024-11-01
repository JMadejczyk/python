n, m = 4, 3
matrix = [
    [4, 1, 3],
    [2, 5, 7],
    [9, 8, 6],
    [10, 11, 12]
]

flattened = []
for row in matrix:
    for el in row:
        flattened.append(el)
flattened.sort()

for j in range(m):
    for i in range(n):
        matrix[i][j] = flattened.pop(0)

for line in matrix:
    print(*line)