n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

grades_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        summ = 0
        counter = 0
        if summ >= 3:
            grades_matrix[i][j] = 1

        else:
            if i-1 >= 0:
                summ += matrix[i-1][j]
                counter += 1
                if j-1 >= 0:
                    summ += matrix[i-1][j-1]
                    counter += 1

            if j-1 >= 0:
                summ += matrix[i][j-1]
                counter += 1
                if i + 1 < n:
                    summ += matrix[i+1][j-1]
                    counter += 1

            if i + 1 < n:
                summ += matrix[i+1][j]
                counter += 1
                if j + 1 < n:
                    summ += matrix[i+1][j+1]
                    counter += 1
                
            if j + 1 < n:
                summ += matrix[i][j+1]
                counter += 1
                if i - 1 >= 0:
                    summ += matrix[i-1][j+1]
                    counter += 1

            if summ / counter >= 3:
                grades_matrix[i][j] = 1

for line in grades_matrix:
    print(*line)