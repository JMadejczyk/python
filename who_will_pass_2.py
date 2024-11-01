n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def calclate_average(i_, j_, matrix):
    score = matrix[i_][j_]
    n = len(matrix)
    numbers = [score]
    for i in range(n):
        curr_score = matrix[i][j_]
        if curr_score >= score and i != i_:
            numbers.append(curr_score)
    for j in range(n):
        curr_score = matrix[i_][j]
        if curr_score >= score and j != j_:
            numbers.append(curr_score)
    return sum(numbers)/len(numbers)

students = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] >=7 or calclate_average(i, j, matrix) >=7:
            students[i][j] = 1
        else: students[i][j] = 0
    
for line in students:
    print(*line)